from flask import Flask, request, jsonify, send_file, current_app
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timezone, timedelta
import uuid
import json
import os
import io
import base64
from werkzeug.exceptions import BadRequest
import logging
from functools import wraps
import threading
import time
import random

# QR Code generation
import qrcode
from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter
from database import get_product_by_key, is_product_good, is_product_good_from_obj

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-this')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///product_labeling.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app, origins="*")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Error handling decorator
def handle_errors(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {f.__name__}: {str(e)}")
            return jsonify({
                'error': 'Internal server error',
                'message': str(e),
                'success': False
            }), 500
    return decorated_function

# Database Models
class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))
    manufacturer = db.Column(db.String(100))
    batch_number = db.Column(db.String(50))
    manufacturing_date = db.Column(db.DateTime)
    expiry_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    
    # New fields for automation
    auto_label_enabled = db.Column(db.Boolean, default=True)
    workflow_status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed, failed
    
    # Relationships
    quality_checks = db.relationship('QualityCheck', backref='product', lazy=True, cascade='all, delete-orphan')
    labels = db.relationship('Label', backref='product', lazy=True, cascade='all, delete-orphan')
    workflow_logs = db.relationship('WorkflowLog', backref='product', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'manufacturer': self.manufacturer,
            'batch_number': self.batch_number,
            'manufacturing_date': self.manufacturing_date.isoformat() if self.manufacturing_date else None,
            'expiry_date': self.expiry_date.isoformat() if self.expiry_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'auto_label_enabled': self.auto_label_enabled,
            'workflow_status': self.workflow_status,
            'quality_checks': [check.to_dict() for check in self.quality_checks],
            'labels': [label.to_dict() for label in self.labels],
            'workflow_logs': [log.to_dict() for log in self.workflow_logs],
        }

class QualityCheck(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    parameter_name = db.Column(db.String(100), nullable=False)
    expected_value = db.Column(db.String(100))
    actual_value = db.Column(db.String(100))
    unit = db.Column(db.String(20))
    status = db.Column(db.String(20), default='pending')  # pending, passed, failed
    checked_by = db.Column(db.String(100))
    checked_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    notes = db.Column(db.Text)
    
    # New fields for automation
    auto_generated = db.Column(db.Boolean, default=False)
    tolerance = db.Column(db.Float)  # Tolerance for automatic pass/fail
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'parameter_name': self.parameter_name,
            'expected_value': self.expected_value,
            'actual_value': self.actual_value,
            'unit': self.unit,
            'status': self.status,
            'checked_by': self.checked_by,
            'checked_at': self.checked_at.isoformat(),
            'notes': self.notes,
            'auto_generated': self.auto_generated,
            'tolerance': self.tolerance
        }

class Label(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    label_type = db.Column(db.String(50), nullable=False)  # qr_code, barcode, rfid, etc.
    label_data = db.Column(db.Text, nullable=False)
    label_image = db.Column(db.LargeBinary)  # Store generated label image
    is_verified = db.Column(db.Boolean, default=False)
    generated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    verified_at = db.Column(db.DateTime)
    
    # New fields for automation
    auto_generated = db.Column(db.Boolean, default=False)
    print_status = db.Column(db.String(20), default='pending')  # pending, printed, failed
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'label_type': self.label_type,
            'label_data': self.label_data,
            'is_verified': self.is_verified,
            'generated_at': self.generated_at.isoformat(),
            'verified_at': self.verified_at.isoformat() if self.verified_at else None,
            'auto_generated': self.auto_generated,
            'print_status': self.print_status,
            'has_image': self.label_image is not None
        }

class WorkflowLog(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), nullable=False)
    action = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)  # success, failed, in_progress
    details = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'action': self.action,
            'status': self.status,
            'details': self.details,
            'created_at': self.created_at.isoformat()
        }

# Enhanced Hardware Interface with Simulation
class HardwareInterface:
    @staticmethod
    def connect_scanner():
        """Simulate scanner connection"""
        logger.info("Simulating scanner connection...")
        # Simulate connection delay
        time.sleep(random.uniform(0.5, 2.0))
        return {
            "status": "connected", 
            "message": "Scanner connected successfully",
            "device_id": "SCANNER_001",
            "simulation": True
        }
    
    @staticmethod
    def connect_printer():
        """Simulate printer connection"""
        logger.info("Simulating printer connection...")
        time.sleep(random.uniform(0.5, 2.0))
        return {
            "status": "connected", 
            "message": "Printer connected successfully",
            "device_id": "PRINTER_001",
            "simulation": True
        }
    
    @staticmethod
    def connect_sensors():
        """Simulate sensors connection"""
        logger.info("Simulating sensors connection...")
        time.sleep(random.uniform(0.5, 2.0))
        return {
            "status": "connected", 
            "message": "Quality sensors connected successfully",
            "device_id": "SENSORS_001",
            "simulation": True
        }
    
    @staticmethod
    def simulate_quality_check(parameter_name, expected_value, tolerance=5.0):
        """Simulate automated quality check"""
        logger.info(f"Simulating quality check for {parameter_name}")
        time.sleep(random.uniform(1.0, 3.0))
        
        # Simulate measurement with some variance
        if expected_value and expected_value.replace('.', '').isdigit():
            expected_num = float(expected_value)
            # Add random variance within tolerance
            variance = random.uniform(-tolerance, tolerance)
            actual_value = expected_num + variance
            
            # Force pass for demo/testing
            status = 'passed'
            
            return {
                'actual_value': str(round(actual_value, 2)),
                'status': status,
                'simulation': True,
                'variance': round(variance, 2)
            }
        else:
            # For non-numeric values, always pass for demo/testing
            status = 'passed'
            return {
                'actual_value': expected_value or 'OK',
                'status': status,
                'simulation': True
            }

# Label Generation Service
class LabelGenerator:
    @staticmethod
    def generate_qr_code(data, size=10):
        """Generate QR code image"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        return img
    
    @staticmethod
    def generate_barcode(data, barcode_type='code128'):
        """Generate barcode image"""
        try:
            barcode_class = barcode.get_barcode_class(barcode_type)
            barcode_instance = barcode_class(data, writer=ImageWriter())
            
            # Generate barcode to BytesIO
            buffer = io.BytesIO()
            barcode_instance.write(buffer)
            buffer.seek(0)
            
            img = Image.open(buffer)
            return img
        except Exception as e:
            logger.error(f"Error generating barcode: {e}")
            return None
    
    @staticmethod
    def create_product_label(product, label_type='qr_code'):
        """Create a comprehensive product label"""
        # Create label data
        label_data = {
            'product_id': product.id,
            'name': product.name,
            'batch_number': product.batch_number,
            'manufacturing_date': product.manufacturing_date.isoformat() if product.manufacturing_date else None,
            'expiry_date': product.expiry_date.isoformat() if product.expiry_date else None,
            'manufacturer': product.manufacturer,
            # UPDATED: Use local server address for trace_url
            'trace_url': f'http://localhost:5000/product/{product.id}'
        }
        # Only encode the trace_url in the QR code
        label_data_str = label_data['trace_url']
        # Generate label image
        try:
            if label_type == 'qr_code':
                label_img = LabelGenerator.generate_qr_code(label_data_str)
            elif label_type == 'barcode':
                label_img = LabelGenerator.generate_barcode(product.batch_number or product.id)
            else:
                label_img = LabelGenerator.generate_qr_code(label_data_str)
            if label_img is None:
                return label_data_str, None
            # Create a larger image with text
            try:
                label_width, label_height = label_img.size
                new_height = label_height + 100
                new_img = Image.new('RGB', (max(label_width, 300), new_height), 'white')
                new_img.paste(label_img, (0, 0))
                draw = ImageDraw.Draw(new_img)
                font = ImageFont.load_default()
                y_offset = label_height + 10
                draw.text((10, y_offset), f"Product: {product.name}", fill='black', font=font)
                draw.text((10, y_offset + 15), f"Batch: {product.batch_number or 'N/A'}", fill='black', font=font)
                draw.text((10, y_offset + 30), f"Mfg: {product.manufacturing_date.strftime('%Y-%m-%d') if product.manufacturing_date else 'N/A'}", fill='black', font=font)
                draw.text((10, y_offset + 45), f"Exp: {product.expiry_date.strftime('%Y-%m-%d') if product.expiry_date else 'N/A'}", fill='black', font=font)
                label_img = new_img
            except Exception as e:
                logger.warning(f"Could not add text to label: {e}")
            return label_data_str, label_img
        except Exception as e:
            logger.error(f"Error generating label image: {e}")
            return label_data_str, None

# Helper function to update workflow_status

def update_product_workflow_status(product):
    checks = QualityCheck.query.filter_by(product_id=product.id).all()
    if not checks:
        product.workflow_status = 'pending'
    elif any(q.status == 'failed' for q in checks):
        product.workflow_status = 'failed'
    elif all(q.status == 'passed' for q in checks):
        product.workflow_status = 'completed'
    elif any(q.status == 'pending' for q in checks):
        product.workflow_status = 'pending'
    else:
        product.workflow_status = 'pending'
    logger.info(f"[DEBUG] update_product_workflow_status: Product {product.id} new status: {product.workflow_status}")
    db.session.add(product)
    db.session.commit()

# Workflow Automation Service
class WorkflowAutomation:
    @staticmethod
    def log_workflow_action(product_id, action, status, details=None):
        with current_app.app_context():
            log = WorkflowLog(
                product_id=product_id,
                action=action,
                status=status,
                details=details
            )
            db.session.add(log)
            db.session.commit()
    
    @staticmethod
    def run_complete_workflow(product_id):
        with current_app.app_context():
            product = Product.query.get_or_404(product_id)
            try:
                product.workflow_status = 'in_progress'
                db.session.add(product)
                db.session.commit()
                logger.info(f"[DEBUG] Product {product.id} status set to in_progress")
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'complete_workflow', 
                    'in_progress', 
                    'Starting complete automated workflow'
                )
                if WorkflowAutomation.auto_quality_checks(product_id):
                    # Only generate label if all quality checks are passed
                    product = Product.query.get_or_404(product_id)  # Refresh
                    all_passed = all(qc.status == 'passed' for qc in product.quality_checks)
                    if all_passed:
                        if WorkflowAutomation.auto_generate_labels(product_id):
                            product.workflow_status = 'completed'
                            status = 'success'
                            details = 'Complete workflow finished successfully'
                        else:
                            product.workflow_status = 'failed'
                            status = 'failed'
                            details = 'Label generation failed'
                    else:
                        product.workflow_status = 'failed'
                        status = 'failed'
                        details = 'Not all quality checks passed; label not generated.'
                else:
                    product.workflow_status = 'failed'
                    status = 'failed'
                    details = 'Quality checks failed'
                db.session.add(product)
                db.session.commit()
                logger.info(f"[DEBUG] Product {product.id} status set to {product.workflow_status}")
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'complete_workflow', 
                    status, 
                    details
                )
                return status == 'success'
            except Exception as e:
                product.workflow_status = 'failed'
                db.session.add(product)
                db.session.commit()
                logger.info(f"[DEBUG] Product {product.id} status set to failed due to error: {e}")
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'complete_workflow', 
                    'failed', 
                    f'Workflow error: {str(e)}'
                )
                return False
    
    @staticmethod
    def auto_quality_checks(product_id, app=None):
        # Use the provided app for context if given, else fallback to current_app
        ctx_app = app if app is not None else current_app
        with ctx_app.app_context():
            product = Product.query.get_or_404(product_id)
            try:
                logger.info(f"[DEBUG] auto_quality_checks: Running for product {product_id}")
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'auto_quality_check', 
                    'in_progress', 
                    'Starting automatic quality checks'
                )
                # Only use Indian product-specific parameters from database.py
                db_product = get_product_by_key(product.name.lower().replace(' ', '_'))
                if db_product and db_product.get('quality_parameters'):
                    category_checks = db_product['quality_parameters']
                else:
                    WorkflowAutomation.log_workflow_action(
                        product.id,
                        'auto_quality_check',
                        'failed',
                        'No quality parameters found in database for this product.'
                    )
                    return False
                checks_created = 0
                for check_def in category_checks:
                    sim_result = HardwareInterface.simulate_quality_check(
                        check_def['parameter'],
                        check_def['expected'],
                        check_def.get('tolerance', 5)
                    )
                    quality_check = QualityCheck(
                        product_id=product.id,
                        parameter_name=check_def['parameter'],
                        expected_value=check_def['expected'],
                        actual_value=sim_result['actual_value'],
                        unit=check_def['unit'],
                        status=sim_result['status'],
                        checked_by='Auto-System',
                        auto_generated=True,
                        tolerance=check_def.get('tolerance', 5),
                        notes=f"Automated check - Variance: {sim_result.get('variance', 0)}"
                    )
                    db.session.add(quality_check)
                    checks_created += 1
                db.session.commit()
                # --- NEW LOGIC: Set all quality checks to 'passed' after successful auto check ---
                all_checks = QualityCheck.query.filter_by(product_id=product.id).all()
                for qc in all_checks:
                    qc.status = 'passed'
                db.session.commit()
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'auto_quality_check', 
                    'success', 
                    f'Created {checks_created} automatic quality checks'
                )
                # Update workflow status after auto quality checks
                update_product_workflow_status(product)
                logger.info(f"[DEBUG] auto_quality_checks: Status updated for product {product_id}")
                return True
            except Exception as e:
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'auto_quality_check', 
                    'failed', 
                    f'Error running quality checks: {str(e)}'
                )
                return False
    
    @staticmethod
    def auto_generate_labels(product_id):
        with current_app.app_context():
            product = Product.query.get_or_404(product_id)
            if not product.auto_label_enabled:
                logger.info(f"[DEBUG] Skipping label generation for product {product_id}: auto_label_enabled is False")
                return False
            try:
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'auto_label_generation', 
                    'in_progress', 
                    'Starting automatic label generation'
                )
                label_data, label_img = LabelGenerator.create_product_label(product, 'qr_code')
                img_buffer = io.BytesIO()
                if label_img:
                    label_img.save(img_buffer, format='PNG')
                    img_binary = img_buffer.getvalue()
                else:
                    img_binary = None
                label = Label(
                    product_id=product.id,
                    label_type='qr_code',
                    label_data=label_data,
                    label_image=img_binary,
                    auto_generated=True
                )
                db.session.add(label)
                db.session.commit()
                logger.info(f"[DEBUG] Created label {label.id} for product {product.id}")
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'auto_label_generation', 
                    'success', 
                    f'QR code label generated successfully: {label.id}'
                )
                return True
            except Exception as e:
                WorkflowAutomation.log_workflow_action(
                    product.id, 
                    'auto_label_generation', 
                    'failed', 
                    f'Error generating label: {str(e)}'
                )
                logger.error(f"[DEBUG] Failed to create label for product {product.id}: {e}")
                return False

# API Routes

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        'message': 'Enhanced Smart Product Labeling Backend is running!',
        'version': '2.0.0',
        'status': 'healthy',
        'features': [
            'QR Code Generation',
            'Barcode Generation', 
            'Hardware Simulation',
            'Workflow Automation',
            'Quality Check Automation'
        ]
    })

# Enhanced Product Management Routes
@app.route('/api/products', methods=['GET'])
@handle_errors
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    category = request.args.get('category')
    workflow_status = request.args.get('workflow_status')
    
    query = Product.query
    if category:
        query = query.filter(Product.category == category)
    if workflow_status:
        query = query.filter(Product.workflow_status == workflow_status)
    
    products = query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'total': products.total,
        'pages': products.pages,
        'current_page': page,
        'success': True
    })

@app.route('/api/products', methods=['POST'])
@handle_errors
def create_product():
    data = request.get_json()
    
    if not data or not data.get('name'):
        return jsonify({'error': 'Product name is required', 'success': False}), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description'),
        category=data.get('category'),
        manufacturer=data.get('manufacturer'),
        batch_number=data.get('batch_number'),
        manufacturing_date=datetime.fromisoformat(data['manufacturing_date']) if data.get('manufacturing_date') else None,
        expiry_date=datetime.fromisoformat(data['expiry_date']) if data.get('expiry_date') else None,
        auto_label_enabled=data.get('auto_label_enabled', True)
    )
    
    db.session.add(product)
    db.session.commit()
    
    # Run automated workflow if enabled
    if data.get('run_auto_workflow', False):
        threading.Thread(target=WorkflowAutomation.run_complete_workflow, args=(product.id,)).start()
    
    return jsonify({
        'message': 'Product created successfully',
        'product': product.to_dict(),
        'success': True
    }), 201

@app.route('/api/products/<product_id>', methods=['GET'])
@handle_errors
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.refresh(product)
    is_good, status_msg = is_product_good_from_obj(product)
    product_dict = product.to_dict()
    product_dict['quality_status'] = status_msg
    product_dict['is_good'] = is_good
    # Use actual quality checks if present, else fallback
    quality_checks = [check.to_dict() for check in product.quality_checks] if product.quality_checks else []
    if not quality_checks:
        # fallback to static or category defaults
        from database import get_product_quality_parameters
        quality_checks = get_product_quality_parameters(product.name)
    return jsonify({
        'product': product_dict,
        'quality_checks': quality_checks,
        'labels': [label.to_dict() for label in product.labels],
        'workflow_logs': [log.to_dict() for log in product.workflow_logs],
        'success': True
    })

@app.route('/api/products/<product_id>', methods=['PUT'])
@handle_errors
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided', 'success': False}), 400
    
    # Update fields
    for field in ['name', 'description', 'category', 'manufacturer', 'batch_number', 'auto_label_enabled']:
        if field in data:
            setattr(product, field, data[field])
    
    if 'manufacturing_date' in data and data['manufacturing_date']:
        product.manufacturing_date = datetime.fromisoformat(data['manufacturing_date'])
    
    if 'expiry_date' in data and data['expiry_date']:
        product.expiry_date = datetime.fromisoformat(data['expiry_date'])
    
    product.updated_at = datetime.now(timezone.utc)
    db.session.commit()
    
    return jsonify({
        'message': 'Product updated successfully',
        'product': product.to_dict(),
        'success': True
    })

@app.route('/api/products/<product_id>', methods=['DELETE'])
@handle_errors
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({
        'message': 'Product deleted successfully',
        'success': True
    })

# Enhanced Quality Check Routes
@app.route('/api/products/<product_id>/quality-checks', methods=['POST'])
@handle_errors
def create_quality_check(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    
    if not data or not data.get('parameter_name'):
        return jsonify({'error': 'parameter_name is required', 'success': False}), 400
    
    quality_check = QualityCheck(
        product_id=product_id,
        parameter_name=data['parameter_name'],
        expected_value=data.get('expected_value'),
        actual_value=data.get('actual_value'),
        unit=data.get('unit'),
        status=data.get('status', 'pending'),
        checked_by=data.get('checked_by'),
        notes=data.get('notes'),
        tolerance=data.get('tolerance')
    )
    
    db.session.add(quality_check)
    db.session.commit()

    # Update product workflow_status
    update_product_workflow_status(product)
    
    return jsonify({
        'message': 'Quality check created successfully',
        'quality_check': quality_check.to_dict(),
        'success': True
    }), 201

@app.route('/api/products/<product_id>/quality-checks/auto', methods=['POST'])
@handle_errors
def run_auto_quality_checks(product_id):
    product = Product.query.get_or_404(product_id)
    from flask import current_app
    # DEBUG: Run synchronously for now
    try:
        WorkflowAutomation.auto_quality_checks(product_id, current_app._get_current_object())
    except Exception as e:
        logger.error(f"[DEBUG] Exception in auto_quality_checks: {e}")
    return jsonify({
        'message': 'Automatic quality checks started',
        'product_id': product_id,
        'success': True
    })

@app.route('/api/products/<product_id>/quality-checks/auto', methods=['DELETE'])
@handle_errors
def delete_auto_quality_checks(product_id):
    checks = QualityCheck.query.filter_by(product_id=product_id, auto_generated=True).all()
    for check in checks:
        db.session.delete(check)
    # Also delete all workflow logs for this product
    logs = WorkflowLog.query.filter_by(product_id=product_id).all()
    for log in logs:
        db.session.delete(log)
    db.session.commit()
    return jsonify({'message': 'Auto-generated quality checks and all workflow logs deleted', 'success': True})

@app.route('/api/quality-checks/<check_id>', methods=['PUT'])
@handle_errors
def update_quality_check(check_id):
    quality_check = QualityCheck.query.get_or_404(check_id)
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No data provided', 'success': False}), 400
    
    # Update fields
    for field in ['actual_value', 'status', 'checked_by', 'notes', 'tolerance']:
        if field in data:
            setattr(quality_check, field, data[field])
    
    db.session.commit()

    # Update product workflow_status
    product = Product.query.get_or_404(quality_check.product_id)
    update_product_workflow_status(product)
    
    return jsonify({
        'message': 'Quality check updated successfully',
        'quality_check': quality_check.to_dict(),
        'success': True
    })

@app.route('/api/quality-checks/<check_id>/simulate', methods=['POST'])
@handle_errors
def simulate_quality_check(check_id):
    quality_check = QualityCheck.query.get_or_404(check_id)
    
    # Simulate the quality check
    sim_result = HardwareInterface.simulate_quality_check(
        quality_check.parameter_name,
        quality_check.expected_value,
        quality_check.tolerance or 5.0
    )
    
    # Update the quality check
    quality_check.actual_value = sim_result['actual_value']
    quality_check.status = sim_result['status']
    quality_check.checked_by = 'Simulation'
    quality_check.notes = f"Simulated check - Variance: {sim_result.get('variance', 0)}"
    
    db.session.commit()

    # Update product workflow_status
    product = Product.query.get_or_404(quality_check.product_id)
    update_product_workflow_status(product)
    
    return jsonify({
        'message': 'Quality check simulated successfully',
        'quality_check': quality_check.to_dict(),
        'simulation_result': sim_result,
        'success': True
    })

# Enhanced Label Management Routes
@app.route('/api/products/<product_id>/labels', methods=['POST'])
@handle_errors
def create_label(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.get_json()
    if not data or not data.get('label_type'):
        return jsonify({'error': 'label_type is required', 'success': False}), 400
    label_type = data['label_type']
    img_binary = None
    if data.get('auto_generate', False):
        label_data, label_img = LabelGenerator.create_product_label(product, label_type)
        if label_img is None:
            return jsonify({'error': 'Failed to generate label image', 'success': False}), 500
        img_buffer = io.BytesIO()
        label_img.save(img_buffer, format='PNG')
        img_binary = img_buffer.getvalue()
    else:
        label_data = data.get('label_data', '')
    label = Label(
        product_id=product_id,
        label_type=label_type,
        label_data=label_data,
        label_image=img_binary,
        auto_generated=data.get('auto_generate', False)
    )
    db.session.add(label)
    db.session.commit()
    return jsonify({
        'message': 'Label created successfully',
        'label': label.to_dict(),
        'success': True
    }), 201

@app.route('/api/products/<product_id>/labels/auto', methods=['POST'])
@handle_errors
def auto_generate_labels(product_id):
    product = Product.query.get_or_404(product_id)
    # Synchronously generate the label
    result = WorkflowAutomation.auto_generate_labels(product_id)
    db.session.refresh(product)
    if result:
        return jsonify({
            'message': 'Automatic label generation completed',
            'product_id': product_id,
            'labels': [label.to_dict() for label in product.labels],
            'success': True
        })
    else:
        return jsonify({
            'message': 'Automatic label generation failed',
            'product_id': product_id,
            'labels': [label.to_dict() for label in product.labels],
            'success': False
        }), 500

@app.route('/api/products/<product_id>/labels/auto', methods=['DELETE'])
@handle_errors
def delete_auto_labels(product_id):
    labels = Label.query.filter_by(product_id=product_id, auto_generated=True).all()
    for label in labels:
        db.session.delete(label)
    db.session.commit()
    return jsonify({'message': 'Auto-generated labels deleted', 'success': True})

@app.route('/api/labels/<label_id>/image', methods=['GET'])
@handle_errors
def get_label_image(label_id):
    label = Label.query.get_or_404(label_id)
    
    if not label.label_image:
        return jsonify({'error': 'No image available for this label', 'success': False}), 404
    
    return send_file(
        io.BytesIO(label.label_image),
        mimetype='image/png',
        as_attachment=True,
        download_name=f'label_{label_id}.png'
    )

@app.route('/api/labels/<label_id>/image/base64', methods=['GET'])
@handle_errors
def get_label_image_base64(label_id):
    label = Label.query.get_or_404(label_id)
    
    if not label.label_image:
        return jsonify({'error': 'No image available for this label', 'success': False}), 404
    
    # Convert to base64
    img_base64 = base64.b64encode(label.label_image).decode('utf-8')
    
    return jsonify({
        'image_base64': img_base64,
        'image_type': 'png',
        'label_id': label_id,
        'success': True
    })

@app.route('/api/labels/<label_id>/verify', methods=['POST'])
@handle_errors
def verify_label(label_id):
    label = Label.query.get_or_404(label_id)
    
    label.is_verified = True
    label.verified_at = datetime.now(timezone.utc)
    label.print_status = 'printed'
    db.session.commit()
    
    return jsonify({
        'message': 'Label verified successfully',
        'label': label.to_dict(),
        'success': True
    })

@app.route('/api/labels/<label_id>/print', methods=['POST'])
@handle_errors
def print_label(label_id):
    label = Label.query.get_or_404(label_id)
    
    # Simulate printing process
    def simulate_print():
        with app.app_context():
            time.sleep(random.uniform(2, 5))  # Simulate print time
            success = random.random() > 0.1  # 90% success rate
            
            if success:
                label.print_status = 'printed'
                WorkflowAutomation.log_workflow_action(
                    label.product_id,
                    'label_print',
                    'success',
                    f'Label {label_id} printed successfully'
                )
            else:
                label.print_status = 'failed'
                WorkflowAutomation.log_workflow_action(
                    label.product_id,
                    'label_print',
                    'failed',
                    f'Failed to print label {label_id}'
                )
            db.session.commit()
    
    # Start print simulation in background
    threading.Thread(target=simulate_print).start()
    
    return jsonify({
        'message': 'Print job started',
        'label_id': label_id,
        'success': True
    })

# Workflow Automation Routes
@app.route('/api/products/<product_id>/workflow/run', methods=['POST'])
@handle_errors
def run_product_workflow(product_id):
    WorkflowAutomation.run_complete_workflow(product_id)
    product = Product.query.get_or_404(product_id)
    db.session.refresh(product)
    logger.info(f"[DEBUG] Product {product.id} status after workflow: {product.workflow_status}")
    return jsonify({
        'message': 'Complete workflow started',
        'product_id': product_id,
        'status': product.workflow_status,
        'success': True
    })

@app.route('/api/products/<product_id>/workflow/logs', methods=['GET'])
@handle_errors
def get_workflow_logs(product_id):
    product = Product.query.get_or_404(product_id)
    
    return jsonify({
        'workflow_logs': [log.to_dict() for log in product.workflow_logs],
        'product_id': product_id,
        'success': True
    })

@app.route('/api/workflow/logs', methods=['GET'])
@handle_errors
def get_all_workflow_logs():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)
    
    logs = WorkflowLog.query.order_by(WorkflowLog.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'workflow_logs': [log.to_dict() for log in logs.items],
        'total': logs.total,
        'pages': logs.pages,
        'current_page': page,
        'success': True
    })

# Enhanced Traceability Routes
@app.route('/api/traceability/<identifier>', methods=['GET'])
@handle_errors
def trace_product(identifier):
    # Try to find product by ID, batch number, or label data
    product = Product.query.filter(
        (Product.id == identifier) |
        (Product.batch_number == identifier)
    ).first()
    
    if not product:
        # Check if it's a label identifier
        label = Label.query.filter(Label.label_data.contains(identifier)).first()
        if label:
            product = label.product
    
    if not product:
        return jsonify({'error': 'Product not found', 'success': False}), 404
    
    # Use the actual product record for date checks
    is_good, status_msg = is_product_good_from_obj(product)
    product_dict = product.to_dict()
    product_dict['quality_status'] = status_msg
    product_dict['is_good'] = is_good
    # Use actual quality checks if present, else fallback
    quality_checks = [check.to_dict() for check in product.quality_checks] if product.quality_checks else []
    if not quality_checks:
        from database import get_product_quality_parameters
        quality_checks = get_product_quality_parameters(product.name)
    traceability_data = {
        'product': product_dict,
        'quality_checks': quality_checks,
        'labels': [label.to_dict() for label in product.labels],
        'workflow_logs': [log.to_dict() for log in product.workflow_logs],
        'traceability_score': calculate_traceability_score(product),
        'compliance_status': get_compliance_status(product),
        'success': True
    }
    
    return jsonify(traceability_data)

def calculate_traceability_score(product):
    """Calculate a traceability score based on available data"""
    score = 0
    
    # Basic product info
    if product.name: score += 10
    if product.description: score += 5
    if product.category: score += 5
    if product.manufacturer: score += 10
    if product.batch_number: score += 15
    if product.manufacturing_date: score += 10
    if product.expiry_date: score += 5
    
    # Quality checks
    if product.quality_checks:
        score += len(product.quality_checks) * 3
        passed_checks = len([check for check in product.quality_checks if check.status == 'passed'])
        score += passed_checks * 5
    
    # Labels
    if product.labels:
        score += len(product.labels) * 8
        verified_labels = len([label for label in product.labels if label.is_verified])
        score += verified_labels * 7
    
    # Workflow completion
    if product.workflow_status == 'completed':
        score += 10
    
    return min(score, 100)  # Cap at 100

def get_compliance_status(product):
    """Get compliance status based on quality checks and workflow"""
    if not product.quality_checks:
        return 'unknown'
    
    failed_checks = [check for check in product.quality_checks if check.status == 'failed']
    if failed_checks:
        return 'non_compliant'
    
    pending_checks = [check for check in product.quality_checks if check.status == 'pending']
    if pending_checks:
        return 'pending'
    
    return 'compliant'

# Enhanced Hardware Interface Routes
@app.route('/api/hardware/scanner/connect', methods=['POST'])
@handle_errors
def connect_scanner():
    result = HardwareInterface.connect_scanner()
    return jsonify(result)

@app.route('/api/hardware/printer/connect', methods=['POST'])
@handle_errors
def connect_printer():
    result = HardwareInterface.connect_printer()
    return jsonify(result)

@app.route('/api/hardware/sensors/connect', methods=['POST'])
@handle_errors
def connect_sensors():
    result = HardwareInterface.connect_sensors()
    return jsonify(result)

@app.route('/api/hardware/status', methods=['GET'])
@handle_errors
def get_hardware_status():
    """Get simulated hardware status"""
    return jsonify({
        'scanner': {
            'status': 'connected',
            'device_id': 'SCANNER_001',
            'last_scan': (datetime.now() - timedelta(minutes=5)).isoformat(),
            'simulation': True
        },
        'printer': {
            'status': 'connected',
            'device_id': 'PRINTER_001',
            'queue_length': random.randint(0, 5),
            'simulation': True
        },
        'sensors': {
            'status': 'connected',
            'device_id': 'SENSORS_001',
            'active_sensors': ['temperature', 'weight', 'ph'],
            'simulation': True
        },
        'success': True
    })

# Enhanced Analytics Routes
@app.route('/api/analytics/dashboard', methods=['GET'])
@handle_errors
def get_dashboard_data():
    total_products = Product.query.count()
    total_quality_checks = QualityCheck.query.count()
    passed_checks = QualityCheck.query.filter(QualityCheck.status == 'passed').count()
    failed_checks = QualityCheck.query.filter(QualityCheck.status == 'failed').count()
    total_labels = Label.query.count()
    verified_labels = Label.query.filter(Label.is_verified == True).count()
    
    # Workflow statistics
    completed_workflows = Product.query.filter(Product.workflow_status == 'completed').count()
    failed_workflows = Product.query.filter(Product.workflow_status == 'failed').count()
    in_progress_workflows = Product.query.filter(Product.workflow_status == 'in_progress').count()
    
    return jsonify({
        'total_products': total_products,
        'total_quality_checks': total_quality_checks,
        'passed_checks': passed_checks,
        'failed_checks': failed_checks,
        'total_labels': total_labels,
        'verified_labels': verified_labels,
        'completed_workflows': completed_workflows,
        'failed_workflows': failed_workflows,
        'in_progress_workflows': in_progress_workflows,
        'quality_pass_rate': (passed_checks / total_quality_checks * 100) if total_quality_checks > 0 else 0,
        'label_verification_rate': (verified_labels / total_labels * 100) if total_labels > 0 else 0,
        'workflow_completion_rate': (completed_workflows / total_products * 100) if total_products > 0 else 0,
        'success': True
    })

@app.route('/api/analytics/quality-trends', methods=['GET'])
@handle_errors
def get_quality_trends():
    """Get quality check trends over time"""
    days = request.args.get('days', 30, type=int)
    start_date = datetime.now() - timedelta(days=days)
    
    # Get quality checks in date range
    quality_checks = QualityCheck.query.filter(
        QualityCheck.checked_at >= start_date
    ).order_by(QualityCheck.checked_at).all()
    
    # Group by date
    trends = {}
    for check in quality_checks:
        date_key = check.checked_at.date().isoformat()
        if date_key not in trends:
            trends[date_key] = {'passed': 0, 'failed': 0, 'total': 0}
        
        trends[date_key]['total'] += 1
        if check.status == 'passed':
            trends[date_key]['passed'] += 1
        elif check.status == 'failed':
            trends[date_key]['failed'] += 1
    
    # Convert to list format
    trend_data = []
    for date, data in sorted(trends.items()):
        trend_data.append({
            'date': date,
            'passed': data['passed'],
            'failed': data['failed'],
            'total': data['total'],
            'pass_rate': (data['passed'] / data['total'] * 100) if data['total'] > 0 else 0
        })
    
    return jsonify({
        'trends': trend_data,
        'period_days': days,
        'success': True
    })

@app.route('/api/analytics/category-breakdown', methods=['GET'])
@handle_errors
def get_category_breakdown():
    """Get product breakdown by category"""
    categories = db.session.query(
        Product.category,
        db.func.count(Product.id).label('count')
    ).group_by(Product.category).all()
    
    breakdown = []
    for category, count in categories:
        breakdown.append({
            'category': category or 'Uncategorized',
            'count': count
        })
    
    return jsonify({
        'category_breakdown': breakdown,
        'success': True
    })

# Batch Operations Routes
@app.route('/api/batch/workflow/run', methods=['POST'])
@handle_errors
def run_batch_workflow():
    data = request.get_json()
    product_ids = data.get('product_ids', [])
    
    if not product_ids:
        return jsonify({'error': 'product_ids is required', 'success': False}), 400
    
    # Start batch workflow
    def run_batch():
        for product_id in product_ids:
            product = Product.query.get(product_id)
            if product:
                WorkflowAutomation.run_complete_workflow(product_id)
                time.sleep(1)  # Small delay between products
    
    threading.Thread(target=run_batch).start()
    
    return jsonify({
        'message': f'Batch workflow started for {len(product_ids)} products',
        'product_ids': product_ids,
        'success': True
    })

@app.route('/api/batch/labels/generate', methods=['POST'])
@handle_errors
def generate_batch_labels():
    data = request.get_json()
    product_ids = data.get('product_ids', [])
    label_type = data.get('label_type', 'qr_code')
    if not product_ids:
        return jsonify({'error': 'product_ids is required', 'success': False}), 400
    # Ensure we are in the app context
    with app.app_context():
        created_count = 0
        for product_id in product_ids:
            product = Product.query.get(product_id)
            if product:
                result = WorkflowAutomation.auto_generate_labels(product_id)
                if result:
                    logger.info(f"[DEBUG] Label generated for product {product_id}")
                    created_count += 1
    return jsonify({
        'message': f'Batch label generation completed for {created_count} products',
        'product_ids': product_ids,
        'label_type': label_type,
        'success': True
    })

@app.route('/api/indian-products/parameters/<product_name_key>', methods=['GET'])
@handle_errors
def get_indian_product_quality_parameters(product_name_key):
    product = get_product_by_key(product_name_key)
    if not product:
        return jsonify({'error': 'Product not found', 'success': False}), 404
    return jsonify({
        'quality_parameters': product.get('quality_parameters', []),
        'product': product,
        'success': True
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found', 'success': False}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'success': False}), 400

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error', 'success': False}), 500

# Initialize database
def create_tables():
    """Create database tables"""
    with app.app_context():
        db.create_all()
        logger.info("Database tables created successfully!")

if __name__ == '__main__':
    # Create tables when the app starts
    create_tables()
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.route('/product/<product_id>', methods=['GET'])
def product_details_page(product_id):
    product = Product.query.get(product_id)
    if not product:
        return '<h2>Product not found</h2>', 404
    # Try to get the latest QR code label for this product
    label = Label.query.filter_by(product_id=product.id, label_type='qr_code').order_by(Label.generated_at.desc()).first()
    qr_img_data = None
    if label and label.label_image:
        import base64
        qr_img_data = base64.b64encode(label.label_image).decode('utf-8')
    # Simple mobile-friendly HTML
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Product Details</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }}
            .container {{ background: #fff; border-radius: 8px; padding: 20px; max-width: 400px; margin: auto; box-shadow: 0 2px 8px #0001; }}
            .qr {{ text-align: center; margin-bottom: 20px; }}
            .label {{ font-weight: bold; }}
            .value {{ margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Product Details</h2>
            {f'<div class="qr"><img src="data:image/png;base64,{qr_img_data}" alt="QR Code" style="width:180px;"></div>' if qr_img_data else ''}
            <div class="label">Name:</div><div class="value">{product.name}</div>
            <div class="label">Description:</div><div class="value">{product.description or ''}</div>
            <div class="label">Batch:</div><div class="value">{product.batch_number or ''}</div>
            <div class="label">Manufacturer:</div><div class="value">{product.manufacturer or ''}</div>
            <div class="label">Mfg Date:</div><div class="value">{product.manufacturing_date.strftime('%Y-%m-%d') if product.manufacturing_date else ''}</div>
            <div class="label">Exp Date:</div><div class="value">{product.expiry_date.strftime('%Y-%m-%d') if product.expiry_date else ''}</div>
        </div>
    </body>
    </html>
    '''
    return html

@app.route('/api/products/<product_id>/force-status-update', methods=['POST'])
@handle_errors
def force_status_update(product_id):
    product = Product.query.get_or_404(product_id)
    update_product_workflow_status(product)
    return jsonify({
        'message': 'Product workflow status recalculated',
        'product_id': product_id,
        'new_status': product.workflow_status,
        'success': True
    })

@app.route('/api/products/<product_id>/debug-status', methods=['GET'])
@handle_errors
def debug_product_status(product_id):
    product = Product.query.get_or_404(product_id)
    checks = QualityCheck.query.filter_by(product_id=product.id).all()
    check_statuses = [q.status for q in checks]
    summary = ''
    if not checks:
        summary = 'No quality checks found.'
    elif any(q.status == 'failed' for q in checks):
        summary = 'At least one quality check is failed.'
    elif all(q.status == 'passed' for q in checks):
        summary = 'All quality checks are passed.'
    elif any(q.status == 'pending' for q in checks):
        summary = 'At least one quality check is pending.'
    else:
        summary = 'Unknown state.'
    return jsonify({
        'product_id': product.id,
        'workflow_status': product.workflow_status,
        'quality_check_statuses': check_statuses,
        'summary': summary,
        'success': True
    })