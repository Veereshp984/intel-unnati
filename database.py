"""
Comprehensive database of Indian-specific products with quality parameters
This file contains detailed information about various Indian products and their quality checks
"""

INDIAN_PRODUCTS_DATABASE = {
    # FOOD & BEVERAGES
    "basmati_rice": {
        "name": "Basmati Rice",
        "category": "food",
        "subcategory": "grains",
        "description": "Premium aromatic long grain rice",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "12.5", "unit": "%", "tolerance": 1.0, "min_value": 11.0, "max_value": 14.0},
            {"parameter": "Grain Length", "expected": "6.8", "unit": "mm", "tolerance": 0.3, "min_value": 6.5, "max_value": 7.5},
            {"parameter": "Broken Grains", "expected": "2.0", "unit": "%", "tolerance": 1.0, "min_value": 0.0, "max_value": 5.0},
            {"parameter": "Aroma Score", "expected": "8.5", "unit": "points", "tolerance": 0.5, "min_value": 8.0, "max_value": 10.0},
            {"parameter": "Chalk Content", "expected": "1.0", "unit": "%", "tolerance": 0.5, "min_value": 0.0, "max_value": 2.0},
            {"parameter": "Gelatinization Temp", "expected": "72", "unit": "°C", "tolerance": 2.0, "min_value": 70, "max_value": 75}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["BIS", "FSSAI", "Agmark"],
        "certifications": ["Organic", "Export Quality"]
    },
    "masala_chai": {
        "name": "Masala Chai Powder",
        "category": "food",
        "subcategory": "beverages",
        "description": "Traditional Indian spiced tea blend",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "8.0", "unit": "%", "tolerance": 1.0, "min_value": 6.0, "max_value": 10.0},
            {"parameter": "Total Ash", "expected": "6.5", "unit": "%", "tolerance": 0.5, "min_value": 5.5, "max_value": 7.5},
            {"parameter": "Caffeine Content", "expected": "3.2", "unit": "%", "tolerance": 0.3, "min_value": 2.5, "max_value": 4.0},
            {"parameter": "Tannin Content", "expected": "12.0", "unit": "%", "tolerance": 1.0, "min_value": 10.0, "max_value": 15.0},
            {"parameter": "Color Value", "expected": "85", "unit": "points", "tolerance": 5, "min_value": 80, "max_value": 95},
            {"parameter": "Flavor Score", "expected": "9.0", "unit": "points", "tolerance": 0.5, "min_value": 8.0, "max_value": 10.0}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 365,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Organic"]
    },
    "ghee": {
        "name": "Pure Desi Ghee",
        "category": "food",
        "subcategory": "dairy",
        "description": "Clarified butter made from cow/buffalo milk",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "0.3", "unit": "%", "tolerance": 0.2, "min_value": 0.0, "max_value": 0.5},
            {"parameter": "Free Fatty Acid", "expected": "0.8", "unit": "%", "tolerance": 0.3, "min_value": 0.0, "max_value": 1.5},
            {"parameter": "Peroxide Value", "expected": "0.5", "unit": "meq/kg", "tolerance": 0.5, "min_value": 0.0, "max_value": 1.0},
            {"parameter": "Iodine Value", "expected": "32", "unit": "g/100g", "tolerance": 3, "min_value": 28, "max_value": 38},
            {"parameter": "Saponification Value", "expected": "230", "unit": "mg KOH/g", "tolerance": 5, "min_value": 220, "max_value": 235},
            {"parameter": "Butyro Refractometer", "expected": "42.5", "unit": "°C", "tolerance": 1.0, "min_value": 40.0, "max_value": 45.0}
        ],
        "storage_conditions": {"temperature": "15-25°C", "humidity": "40%"},
        "shelf_life_days": 365,
        "regulatory_standards": ["FSSAI", "BIS", "Agmark"],
        "certifications": ["FSSAI License", "Organic", "Agmark"]
    },
    "turmeric_powder": {
        "name": "Turmeric Powder (Haldi)",
        "category": "food",
        "subcategory": "spices",
        "description": "Ground turmeric rhizome powder",
        "quality_parameters": [
            {"parameter": "Curcumin Content", "expected": "3.5", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 5.0},
            {"parameter": "Moisture Content", "expected": "10.0", "unit": "%", "tolerance": 1.0, "min_value": 8.0, "max_value": 12.0},
            {"parameter": "Total Ash", "expected": "6.0", "unit": "%", "tolerance": 1.0, "min_value": 4.0, "max_value": 8.0},
            {"parameter": "Acid Insoluble Ash", "expected": "1.0", "unit": "%", "tolerance": 0.5, "min_value": 0.0, "max_value": 2.0},
            {"parameter": "Volatile Oil", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 3.0, "max_value": 8.0},
            {"parameter": "Lead Content", "expected": "0.5", "unit": "ppm", "tolerance": 0.3, "min_value": 0.0, "max_value": 1.0}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 545,
        "regulatory_standards": ["FSSAI", "Spice Board", "BIS"],
        "certifications": ["Organic", "Export Quality"]
    },
    "coconut_oil": {
        "name": "Virgin Coconut Oil",
        "category": "food",
        "subcategory": "oils",
        "description": "Cold-pressed virgin coconut oil",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "0.2", "unit": "%", "tolerance": 0.1, "min_value": 0.0, "max_value": 0.5},
            {"parameter": "Free Fatty Acid", "expected": "0.3", "unit": "%", "tolerance": 0.2, "min_value": 0.0, "max_value": 0.5},
            {"parameter": "Peroxide Value", "expected": "1.0", "unit": "meq/kg", "tolerance": 0.5, "min_value": 0.0, "max_value": 2.0},
            {"parameter": "Iodine Value", "expected": "8.5", "unit": "g/100g", "tolerance": 1.0, "min_value": 7.0, "max_value": 10.0},
            {"parameter": "Saponification Value", "expected": "256", "unit": "mg KOH/g", "tolerance": 5, "min_value": 250, "max_value": 265},
            {"parameter": "Lauric Acid", "expected": "48", "unit": "%", "tolerance": 2, "min_value": 45, "max_value": 52}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["FSSAI", "BIS", "Agmark"],
        "certifications": ["Organic", "Cold Pressed"]
    },
    "filter_coffee": {
        "name": "South Indian Filter Coffee",
        "category": "food",
        "subcategory": "beverages",
        "description": "Traditional filter coffee blend",
        "quality_parameters": [
            {"parameter": "Coffee Content", "expected": "80", "unit": "%", "tolerance": 5, "min_value": 70, "max_value": 90},
            {"parameter": "Chicory Content", "expected": "20", "unit": "%", "tolerance": 5, "min_value": 10, "max_value": 30},
            {"parameter": "Moisture Content", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 3.0, "max_value": 7.0},
            {"parameter": "Caffeine Content", "expected": "1.2", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.8},
            {"parameter": "Grind Size", "expected": "0.8", "unit": "mm", "tolerance": 0.1, "min_value": 0.6, "max_value": 1.2},
            {"parameter": "Aroma Score", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 365,
        "regulatory_standards": ["FSSAI", "Coffee Board"],
        "certifications": ["Organic", "Fair Trade"]
    },
    "masala_papad": {
        "name": "Masala Papad",
        "category": "food",
        "subcategory": "snacks",
        "description": "Spiced lentil wafers",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "8.0", "unit": "%", "tolerance": 1.0, "min_value": 6.0, "max_value": 10.0},
            {"parameter": "Protein Content", "expected": "18", "unit": "%", "tolerance": 2, "min_value": 15, "max_value": 22},
            {"parameter": "Salt Content", "expected": "2.5", "unit": "%", "tolerance": 0.5, "min_value": 2.0, "max_value": 3.5},
            {"parameter": "Oil Content", "expected": "12", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 16},
            {"parameter": "Crispiness", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Spice Level", "expected": "3.5", "unit": "grade", "tolerance": 0.5, "min_value": 3.0, "max_value": 4.5}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "40%"},
        "shelf_life_days": 180,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Traditional Recipe"]
    },
    "mango_pickle": {
        "name": "Mango Pickle (Aam ka Achar)",
        "category": "food",
        "subcategory": "condiments",
        "description": "Traditional spicy mango pickle",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "20.0", "unit": "%", "tolerance": 2.0, "min_value": 15.0, "max_value": 25.0},
            {"parameter": "Salt Content", "expected": "10.0", "unit": "%", "tolerance": 1.0, "min_value": 8.0, "max_value": 12.0},
            {"parameter": "Oil Content", "expected": "15.0", "unit": "%", "tolerance": 2.0, "min_value": 12.0, "max_value": 18.0},
            {"parameter": "pH Value", "expected": "3.5", "unit": "pH", "tolerance": 0.3, "min_value": 3.0, "max_value": 4.0},
            {"parameter": "Spice Intensity", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0},
            {"parameter": "Microbial Count", "expected": "100", "unit": "CFU/g", "tolerance": 50, "min_value": 0, "max_value": 200}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 365,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Traditional Recipe"]
    },
    "jaggery": {
        "name": "Organic Jaggery (Gur)",
        "category": "food",
        "subcategory": "sweeteners",
        "description": "Unrefined cane sugar",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 3.0, "max_value": 7.0},
            {"parameter": "Sucrose Content", "expected": "70", "unit": "%", "tolerance": 5, "min_value": 65, "max_value": 80},
            {"parameter": "Total Ash", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.0, "max_value": 3.0},
            {"parameter": "Insoluble Impurities", "expected": "0.5", "unit": "%", "tolerance": 0.2, "min_value": 0.0, "max_value": 1.0},
            {"parameter": "Color Intensity", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "50%"},
        "shelf_life_days": 545,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["Organic", "FSSAI License"]
    },
    # NEW FOOD & BEVERAGES
    "parle_g_biscuits": {
        "name": "Parle-G Biscuits",
        "category": "food",
        "subcategory": "biscuits",
        "description": "Classic Indian glucose biscuits",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "4.0", "unit": "%", "tolerance": 0.5, "min_value": 3.0, "max_value": 5.0},
            {"parameter": "Sugar Content", "expected": "25", "unit": "%", "tolerance": 2, "min_value": 20, "max_value": 30},
            {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 1, "min_value": 13, "max_value": 17},
            {"parameter": "Crispiness", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Microbial Count", "expected": "100", "unit": "CFU/g", "tolerance": 50, "min_value": 0, "max_value": 200}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "40%"},
        "shelf_life_days": 180,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Vegetarian"]
    },
    "marie_biscuits": {
        "name": "Marie Biscuits",
        "category": "food",
        "subcategory": "biscuits",
        "description": "Light and crisp digestive biscuits",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "3.5", "unit": "%", "tolerance": 0.5, "min_value": 3.0, "max_value": 4.5},
            {"parameter": "Sugar Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
            {"parameter": "Fat Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 8, "max_value": 12},
            {"parameter": "Crispiness", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0},
            {"parameter": "Microbial Count", "expected": "100", "unit": "CFU/g", "tolerance": 50, "min_value": 0, "max_value": 200}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "40%"},
        "shelf_life_days": 180,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Vegetarian"]
    },
    "lassi": {
        "name": "Lassi",
        "category": "food",
        "subcategory": "beverages",
        "description": "Traditional Indian yogurt-based drink",
        "quality_parameters": [
            {"parameter": "pH Value", "expected": "4.2", "unit": "pH", "tolerance": 0.3, "min_value": 3.8, "max_value": 4.5},
            {"parameter": "Total Solids", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
            {"parameter": "Sugar Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 8, "max_value": 12},
            {"parameter": "Viscosity", "expected": "1500", "unit": "cPs", "tolerance": 200, "min_value": 1200, "max_value": 1800},
            {"parameter": "Microbial Count", "expected": "1000", "unit": "CFU/ml", "tolerance": 500, "min_value": 0, "max_value": 2000}
        ],
        "storage_conditions": {"temperature": "4°C", "humidity": "50%"},
        "shelf_life_days": 7,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Vegetarian"]
    },
    "jaljeera": {
        "name": "Jaljeera Powder",
        "category": "food",
        "subcategory": "beverages",
        "description": "Spiced cumin-flavored drink mix",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "6.0", "unit": "%", "tolerance": 1.0, "min_value": 5.0, "max_value": 7.0},
            {"parameter": "Cumin Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 12, "max_value": 18},
            {"parameter": "Salt Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
            {"parameter": "pH Value", "expected": "3.8", "unit": "pH", "tolerance": 0.3, "min_value": 3.5, "max_value": 4.2},
            {"parameter": "Flavor Score", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 365,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Vegetarian"]
    },
    "khakhra": {
        "name": "Khakhra",
        "category": "food",
        "subcategory": "snacks",
        "description": "Crispy Gujarati wheat flatbread",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 4.0, "max_value": 6.0},
            {"parameter": "Oil Content", "expected": "10", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 12},
            {"parameter": "Salt Content", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5},
            {"parameter": "Crispiness", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Microbial Count", "expected": "100", "unit": "CFU/g", "tolerance": 50, "min_value": 0, "max_value": 200}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "40%"},
        "shelf_life_days": 180,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Vegetarian"]
    },
    "gulab_jamun": {
        "name": "Gulab Jamun",
        "category": "food",
        "subcategory": "sweets",
        "description": "Traditional Indian milk-based sweet",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "30", "unit": "%", "tolerance": 2, "min_value": 28, "max_value": 32},
            {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 3, "min_value": 35, "max_value": 45},
            {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17},
            {"parameter": "Texture Score", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Microbial Count", "expected": "1000", "unit": "CFU/g", "tolerance": 500, "min_value": 0, "max_value": 2000}
        ],
        "storage_conditions": {"temperature": "4°C", "humidity": "50%"},
        "shelf_life_days": 30,
        "regulatory_standards": ["FSSAI", "BIS"],
        "certifications": ["FSSAI License", "Vegetarian"]
    },
    "coriander_powder": {
        "name": "Coriander Powder (Dhania)",
        "category": "food",
        "subcategory": "spices",
        "description": "Ground coriander seed powder",
        "quality_parameters": [
            {"parameter": "Moisture Content", "expected": "9.0", "unit": "%", "tolerance": 1.0, "min_value": 8.0, "max_value": 10.0},
            {"parameter": "Volatile Oil", "expected": "0.5", "unit": "%", "tolerance": 0.2, "min_value": 0.3, "max_value": 0.8},
            {"parameter": "Total Ash", "expected": "7.0", "unit": "%", "tolerance": 1.0, "min_value": 6.0, "max_value": 8.0},
            {"parameter": "Acid Insoluble Ash", "expected": "1.0", "unit": "%", "tolerance": 0.5, "min_value": 0.5, "max_value": 1.5},
            {"parameter": "Flavor Score", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 545,
        "regulatory_standards": ["FSSAI", "Spice Board", "BIS"],
        "certifications": ["Organic", "Export Quality"]
    },
    # AYURVEDIC & HERBAL PRODUCTS
    "ashwagandha": {
        "name": "Ashwagandha Powder",
        "category": "ayurvedic",
        "subcategory": "herbs",
        "description": "Withania somnifera root powder",
        "quality_parameters": [
            {"parameter": "Withanolides", "expected": "2.5", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 5.0},
            {"parameter": "Moisture Content", "expected": "8.0", "unit": "%", "tolerance": 1.0, "min_value": 6.0, "max_value": 10.0},
            {"parameter": "Total Ash", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 3.0, "max_value": 7.0},
            {"parameter": "Acid Insoluble Ash", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.0, "max_value": 3.0},
            {"parameter": "Heavy Metals", "expected": "5.0", "unit": "ppm", "tolerance": 2.0, "min_value": 0.0, "max_value": 10.0},
            {"parameter": "Microbial Count", "expected": "1000", "unit": "CFU/g", "tolerance": 500, "min_value": 0, "max_value": 5000}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["AYUSH", "WHO-GMP", "BIS"],
        "certifications": ["Organic", "AYUSH Licensed"]
    },
    "triphala": {
        "name": "Triphala Churna",
        "category": "ayurvedic",
        "subcategory": "formulations",
        "description": "Three fruit powder blend",
        "quality_parameters": [
            {"parameter": "Tannin Content", "expected": "15.0", "unit": "%", "tolerance": 2.0, "min_value": 12.0, "max_value": 20.0},
            {"parameter": "Moisture Content", "expected": "8.0", "unit": "%", "tolerance": 1.0, "min_value": 6.0, "max_value": 10.0},
            {"parameter": "Total Ash", "expected": "6.0", "unit": "%", "tolerance": 1.0, "min_value": 4.0, "max_value": 8.0},
            {"parameter": "Gallic Acid", "expected": "1.2", "unit": "%", "tolerance": 0.3, "min_value": 0.8, "max_value": 2.0},
            {"parameter": "pH Value", "expected": "3.5", "unit": "pH", "tolerance": 0.3, "min_value": 3.0, "max_value": 4.0},
            {"parameter": "Particle Size", "expected": "80", "unit": "mesh", "tolerance": 10, "min_value": 60, "max_value": 100}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 545,
        "regulatory_standards": ["AYUSH", "WHO-GMP"],
        "certifications": ["AYUSH Licensed", "Organic"]
    },
    "tulsi_drops": {
        "name": "Tulsi Drops",
        "category": "ayurvedic",
        "subcategory": "extracts",
        "description": "Concentrated holy basil extract",
        "quality_parameters": [
            {"parameter": "Eugenol Content", "expected": "2.0", "unit": "%", "tolerance": 0.3, "min_value": 1.5, "max_value": 2.5},
            {"parameter": "Moisture Content", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 3.0, "max_value": 7.0},
            {"parameter": "Total Ash", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.0, "max_value": 4.0},
            {"parameter": "pH Value", "expected": "4.5", "unit": "pH", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Microbial Count", "expected": "500", "unit": "CFU/ml", "tolerance": 200, "min_value": 0, "max_value": 1000}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["AYUSH", "WHO-GMP"],
        "certifications": ["Organic", "AYUSH Licensed"]
    },
    # NEW AYURVEDIC & HERBAL PRODUCTS
    "amla_juice": {
        "name": "Amla Juice",
        "category": "ayurvedic",
        "subcategory": "beverages",
        "description": "Indian gooseberry health drink",
        "quality_parameters": [
            {"parameter": "Vitamin C Content", "expected": "600", "unit": "mg/L", "tolerance": 50, "min_value": 500, "max_value": 700},
            {"parameter": "pH Value", "expected": "3.0", "unit": "pH", "tolerance": 0.3, "min_value": 2.7, "max_value": 3.3},
            {"parameter": "Total Solids", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 12, "max_value": 18},
            {"parameter": "Microbial Count", "expected": "500", "unit": "CFU/ml", "tolerance": 200, "min_value": 0, "max_value": 1000},
            {"parameter": "Taste Score", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "4°C", "humidity": "50%"},
        "shelf_life_days": 180,
        "regulatory_standards": ["AYUSH", "FSSAI"],
        "certifications": ["Organic", "AYUSH Licensed"]
    },
    # TEXTILES
    "cotton_fabric": {
        "name": "Pure Cotton Fabric",
        "category": "textile",
        "subcategory": "natural_fiber",
        "description": "100% cotton woven fabric",
        "quality_parameters": [
            {"parameter": "Cotton Content", "expected": "100", "unit": "%", "tolerance": 0, "min_value": 98, "max_value": 100},
            {"parameter": "GSM Weight", "expected": "150", "unit": "g/m²", "tolerance": 10, "min_value": 120, "max_value": 200},
            {"parameter": "Thread Count", "expected": "80", "unit": "TPI", "tolerance": 5, "min_value": 70, "max_value": 100},
            {"parameter": "Shrinkage", "expected": "3.0", "unit": "%", "tolerance": 1.0, "min_value": 0.0, "max_value": 5.0},
            {"parameter": "Color Fastness", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Tensile Strength", "expected": "300", "unit": "N", "tolerance": 30, "min_value": 250, "max_value": 400}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "65%"},
        "shelf_life_days": 1825,
        "regulatory_standards": ["BIS", "Textile Committee"],
        "certifications": ["GOTS", "Organic Cotton"]
    },
    "silk_saree": {
        "name": "Pure Silk Saree",
        "category": "textile",
        "subcategory": "silk",
        "description": "Traditional silk saree",
        "quality_parameters": [
            {"parameter": "Silk Content", "expected": "100", "unit": "%", "tolerance": 0, "min_value": 95, "max_value": 100},
            {"parameter": "Denier", "expected": "20", "unit": "D", "tolerance": 2, "min_value": 18, "max_value": 25},
            {"parameter": "Luster Grade", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Tensile Strength", "expected": "450", "unit": "N", "tolerance": 50, "min_value": 350, "max_value": 550},
            {"parameter": "Elongation", "expected": "18", "unit": "%", "tolerance": 2, "min_value": 15, "max_value": 22},
            {"parameter": "Zari Purity", "expected": "95", "unit": "%", "tolerance": 3, "min_value": 90, "max_value": 100}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "55%"},
        "shelf_life_days": 3650,
        "regulatory_standards": ["BIS", "Silk Mark"],
        "certifications": ["Silk Mark", "Handwoven"]
    },
    "khadi_fabric": {
        "name": "Khadi Fabric",
        "category": "textile",
        "subcategory": "natural_fiber",
        "description": "Hand-spun and handwoven cotton fabric",
        "quality_parameters": [
            {"parameter": "Cotton Content", "expected": "100", "unit": "%", "tolerance": 0, "min_value": 98, "max_value": 100},
            {"parameter": "GSM Weight", "expected": "120", "unit": "g/m²", "tolerance": 10, "min_value": 100, "max_value": 150},
            {"parameter": "Thread Count", "expected": "60", "unit": "TPI", "tolerance": 5, "min_value": 50, "max_value": 80},
            {"parameter": "Shrinkage", "expected": "4.0", "unit": "%", "tolerance": 1.0, "min_value": 2.0, "max_value": 6.0},
            {"parameter": "Color Fastness", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0},
            {"parameter": "Tensile Strength", "expected": "250", "unit": "N", "tolerance": 25, "min_value": 200, "max_value": 300}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 1825,
        "regulatory_standards": ["BIS", "Khadi Mark"],
        "certifications": ["Khadi Mark", "Handwoven"]
    },
    # COSMETICS & PERSONAL CARE
    "neem_face_wash": {
        "name": "Neem Face Wash",
        "category": "cosmetics",
        "subcategory": "skincare",
        "description": "Natural neem-based face cleanser",
        "quality_parameters": [
            {"parameter": "pH Value", "expected": "6.5", "unit": "pH", "tolerance": 0.5, "min_value": 5.5, "max_value": 7.5},
            {"parameter": "Neem Extract", "expected": "5.0", "unit": "%", "tolerance": 0.5, "min_value": 4.0, "max_value": 6.0},
            {"parameter": "Foam Quality", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0},
            {"parameter": "Viscosity", "expected": "2500", "unit": "cPs", "tolerance": 200, "min_value": 2000, "max_value": 3000},
            {"parameter": "Microbial Count", "expected": "100", "unit": "CFU/g", "tolerance": 50, "min_value": 0, "max_value": 500},
            {"parameter": "Preservative Efficacy", "expected": "99.9", "unit": "%", "tolerance": 0.1, "min_value": 99.0, "max_value": 100.0}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["BIS", "CDSCO"],
        "certifications": ["Cruelty Free", "Paraben Free"]
    },
    "coconut_hair_oil": {
        "name": "Coconut Hair Oil",
        "category": "cosmetics",
        "subcategory": "hair_care",
        "description": "Natural coconut oil for hair",
        "quality_parameters": [
            {"parameter": "Coconut Oil Content", "expected": "95", "unit": "%", "tolerance": 2, "min_value": 90, "max_value": 100},
            {"parameter": "Free Fatty Acid", "expected": "0.5", "unit": "%", "tolerance": 0.2, "min_value": 0.0, "max_value": 1.0},
            {"parameter": "Peroxide Value", "expected": "1.0", "unit": "meq/kg", "tolerance": 0.5, "min_value": 0.0, "max_value": 2.0},
            {"parameter": "Saponification Value", "expected": "256", "unit": "mg KOH/g", "tolerance": 5, "min_value": 250, "max_value": 265},
            {"parameter": "Vitamin E", "expected": "15", "unit": "mg/100g", "tolerance": 3, "min_value": 10, "max_value": 20},
            {"parameter": "Fragrance Score", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["BIS", "CDSCO"],
        "certifications": ["Natural", "Organic"]
    },
    "ayurvedic_soap": {
        "name": "Ayurvedic Soap",
        "category": "cosmetics",
        "subcategory": "skincare",
        "description": "Herbal soap with neem and turmeric",
        "quality_parameters": [
            {"parameter": "pH Value", "expected": "9.0", "unit": "pH", "tolerance": 0.5, "min_value": 8.5, "max_value": 9.5},
            {"parameter": "Moisture Content", "expected": "12.0", "unit": "%", "tolerance": 1.0, "min_value": 10.0, "max_value": 15.0},
            {"parameter": "Total Fatty Matter", "expected": "75", "unit": "%", "tolerance": 5, "min_value": 70, "max_value": 80},
            {"parameter": "Foam Quality", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Herbal Content", "expected": "5.0", "unit": "%", "tolerance": 1.0, "min_value": 3.0, "max_value": 7.0}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["BIS", "CDSCO"],
        "certifications": ["Ayurvedic", "Cruelty Free"]
    },
    # HANDICRAFTS
    "brass_utensils": {
        "name": "Brass Utensils",
        "category": "handicraft",
        "subcategory": "metalware",
        "description": "Traditional brass kitchen utensils",
        "quality_parameters": [
            {"parameter": "Copper Content", "expected": "70", "unit": "%", "tolerance": 3, "min_value": 65, "max_value": 75},
            {"parameter": "Zinc Content", "expected": "30", "unit": "%", "tolerance": 3, "min_value": 25, "max_value": 35},
            {"parameter": "Lead Content", "expected": "0.05", "unit": "%", "tolerance": 0.03, "min_value": 0.0, "max_value": 0.1},
            {"parameter": "Surface Finish", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Thickness", "expected": "1.2", "unit": "mm", "tolerance": 0.2, "min_value": 1.0, "max_value": 2.0},
            {"parameter": "Weight Accuracy", "expected": "500", "unit": "g", "tolerance": 25, "min_value": 450, "max_value": 550}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "50%"},
        "shelf_life_days": 10950,
        "regulatory_standards": ["BIS", "Export Quality"],
        "certifications": ["Handmade", "GI Tag"]
    },
    "terracotta_pottery": {
        "name": "Terracotta Pottery",
        "category": "handicraft",
        "subcategory": "pottery",
        "description": "Handcrafted terracotta pots",
        "quality_parameters": [
            {"parameter": "Clay Purity", "expected": "95", "unit": "%", "tolerance": 2, "min_value": 90, "max_value": 100},
            {"parameter": "Firing Temperature", "expected": "900", "unit": "°C", "tolerance": 50, "min_value": 850, "max_value": 950},
            {"parameter": "Water Absorption", "expected": "10", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 12},
            {"parameter": "Surface Finish", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0},
            {"parameter": "Crack Resistance", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "50%"},
        "shelf_life_days": 10950,
        "regulatory_standards": ["BIS", "Export Quality"],
        "certifications": ["Handmade", "Eco-Friendly"]
    },
    # INCENSE & FRAGRANCE
    "sandalwood_incense": {
        "name": "Sandalwood Incense Sticks",
        "category": "fragrance",
        "subcategory": "incense",
        "description": "Pure sandalwood incense sticks",
        "quality_parameters": [
            {"parameter": "Sandalwood Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 10, "max_value": 20},
            {"parameter": "Moisture Content", "expected": "8.0", "unit": "%", "tolerance": 1.0, "min_value": 6.0, "max_value": 10.0},
            {"parameter": "Burning Time", "expected": "45", "unit": "minutes", "tolerance": 5, "min_value": 35, "max_value": 55},
            {"parameter": "Fragrance Intensity", "expected": "4.5", "unit": "grade", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0},
            {"parameter": "Ash Content", "expected": "15", "unit": "%", "tolerance": 3, "min_value": 10, "max_value": 20},
            {"parameter": "Smoke Quality", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["BIS", "Export Quality"],
        "certifications": ["Natural", "Handmade"]
    },
    "dhoop_cones": {
        "name": "Dhoop Cones",
        "category": "fragrance",
        "subcategory": "incense",
        "description": "Traditional Indian dhoop incense cones",
        "quality_parameters": [
            {"parameter": "Herbal Content", "expected": "20", "unit": "%", "tolerance": 3, "min_value": 15, "max_value": 25},
            {"parameter": "Moisture Content", "expected": "7.0", "unit": "%", "tolerance": 1.0, "min_value": 5.0, "max_value": 9.0},
            {"parameter": "Burning Time", "expected": "30", "unit": "minutes", "tolerance": 5, "min_value": 25, "max_value": 35},
            {"parameter": "Fragrance Intensity", "expected": "4.0", "unit": "grade", "tolerance": 0.5, "min_value": 3.5, "max_value": 5.0},
            {"parameter": "Ash Content", "expected": "10", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 12}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "50%"},
        "shelf_life_days": 730,
        "regulatory_standards": ["BIS", "Export Quality"],
        "certifications": ["Natural", "Handmade"]
    },
    # ELECTRONICS
    "led_bulb": {
        "name": "LED Bulb (Indian Make)",
        "category": "electronics",
        "subcategory": "lighting",
        "description": "Energy efficient LED bulb",
        "quality_parameters": [
            {"parameter": "Luminous Efficacy", "expected": "120", "unit": "lm/W", "tolerance": 10, "min_value": 100, "max_value": 140},
            {"parameter": "Power Consumption", "expected": "9", "unit": "W", "tolerance": 0.5, "min_value": 8, "max_value": 10},
            {"parameter": "Color Temperature", "expected": "3000", "unit": "K", "tolerance": 200, "min_value": 2700, "max_value": 6500},
            {"parameter": "Power Factor", "expected": "0.9", "unit": "PF", "tolerance": 0.05, "min_value": 0.85, "max_value": 1.0},
            {"parameter": "Life Hours", "expected": "25000", "unit": "hours", "tolerance": 2000, "min_value": 20000, "max_value": 50000},
            {"parameter": "Input Voltage", "expected": "230", "unit": "V", "tolerance": 20, "min_value": 180, "max_value": 280}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 1825,
        "regulatory_standards": ["BIS", "ISI Mark"],
        "certifications": ["Energy Star", "BEE Rating"]
    },
    "solar_lantern": {
        "name": "Solar Lantern (Indian Make)",
        "category": "electronics",
        "subcategory": "renewable_energy",
        "description": "Portable solar-powered lantern",
        "quality_parameters": [
            {"parameter": "Luminous Flux", "expected": "200", "unit": "lm", "tolerance": 20, "min_value": 180, "max_value": 220},
            {"parameter": "Battery Capacity", "expected": "2000", "unit": "mAh", "tolerance": 200, "min_value": 1800, "max_value": 2200},
            {"parameter": "Solar Panel Efficiency", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 12, "max_value": 18},
            {"parameter": "Charging Time", "expected": "6", "unit": "hours", "tolerance": 1, "min_value": 5, "max_value": 7},
            {"parameter": "Operating Temperature", "expected": "25", "unit": "°C", "tolerance": 5, "min_value": 20, "max_value": 30}
        ],
        "storage_conditions": {"temperature": "25°C", "humidity": "60%"},
        "shelf_life_days": 1825,
        "regulatory_standards": ["BIS", "MNRE"],
        "certifications": ["Energy Efficient", "Eco-Friendly"]
    },
    # PHARMACEUTICAL
    "ayurvedic_tablet": {
        "name": "Ayurvedic Immunity Tablet",
        "category": "pharmaceutical",
        "subcategory": "ayurvedic",
        "description": "Herbal immunity booster tablets",
        "quality_parameters": [
            {"parameter": "Active Ingredients", "expected": "250", "unit": "mg", "tolerance": 15, "min_value": 225, "max_value": 275},
            {"parameter": "Hardness", "expected": "8.0", "unit": "kP", "tolerance": 1.0, "min_value": 6.0, "max_value": 12.0},
            {"parameter": "Friability", "expected": "0.5", "unit": "%", "tolerance": 0.3, "min_value": 0.0, "max_value": 1.0},
            {"parameter": "Disintegration Time", "expected": "15", "unit": "minutes", "tolerance": 3, "min_value": 10, "max_value": 20},
            {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.0, "max_value": 4.0},
            {"parameter": "Microbial Limit", "expected": "1000", "unit": "CFU/g", "tolerance": 200, "min_value": 0, "max_value": 5000}
        ],
        "storage_conditions": {"temperature": "20°C", "humidity": "45%"},
        "shelf_life_days": 1095,
        "regulatory_standards": ["AYUSH", "WHO-GMP", "CDSCO"],
        "certifications": ["AYUSH Licensed", "GMP"]
    }
}

# Helper functions to work with the database
def get_product_by_key(product_key):
    """Get product information by key"""
    return INDIAN_PRODUCTS_DATABASE.get(product_key)

def get_products_by_category(category):
    """Get all products in a specific category"""
    return {key: product for key, product in INDIAN_PRODUCTS_DATABASE.items() 
            if product.get('category') == category}

def get_all_categories():
    """Get all available categories"""
    return list(set(product.get('category') for product in INDIAN_PRODUCTS_DATABASE.values()))

def get_all_subcategories():
    """Get all available subcategories"""
    return list(set(product.get('subcategory') for product in INDIAN_PRODUCTS_DATABASE.values()))

def search_products(query):
    """Search products by name or description"""
    query = query.lower()
    results = {}
    for key, product in INDIAN_PRODUCTS_DATABASE.items():
        if (query in product.get('name', '').lower() or 
            query in product.get('description', '').lower() or
            query in key.lower()):
            results[key] = product
    return results

def get_random_product():
    """Get a random product from the database"""
    import random
    key = random.choice(list(INDIAN_PRODUCTS_DATABASE.keys()))
    return key, INDIAN_PRODUCTS_DATABASE[key]

def get_product_quality_parameters(product_key):
    """Get quality parameters for a specific product"""
    product = get_product_by_key(product_key)
    return product.get('quality_parameters', []) if product else []