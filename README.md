
# Smart Label Product System

## Overview

The Smart Label Product System is a web-based platform designed to enhance product traceability, quality assurance, and supply chain transparency using QR code technology. This solution enables manufacturers, distributors, retailers, and consumers to track products in real time, verify authenticity, and access detailed product information at every stage of the supply chain.

> **Note:** This project is specifically focused on **Indian food products**, ensuring compliance with regional food quality standards and parameters.

## Features

* QR Code-Based Labeling: Generate unique QR codes for each product or batch, linking to detailed product data.
* Real-Time Traceability: Track products from manufacturing to end-user, ensuring transparency and accountability.
* Automated Quality Checks: Record and monitor quality assurance workflows for every product or batch.
* Analytics Dashboard: Visualize product movement, batch status, and quality trends with interactive charts and reports.
* Counterfeit Prevention: Instantly verify product authenticity by scanning QR codes.
* User-Friendly Interface: Manage products, batches, and analytics through an intuitive web dashboard.

## Quality Check System

The platform includes a flexible quality evaluation system that supports both **manual** and **automated** parameter checks. This is essential for verifying product compliance with standards such as Moisture Content, Protein Content, Shelf Life, and more.

### How Are Quality Parameters Evaluated?

Each quality parameter is assessed by comparing its **actual value** to an **expected value**, along with a defined **tolerance range**. The system determines whether the parameter passes or fails accordingly.

#### 1. Automated Quality Checks (Simulated Mode)

When the Run Auto Quality Checks button is used:
* The backend simulates actual values close to the expected ones.
* These values are marked as `Checked By: Auto-System`.
* This is useful for demo, testing, or non-production environments where sensor or lab integration isn't available.

#### 2. Manual Entry

Using the **“Add Quality Check”** feature:
* Users can input actual measured values for each parameter.
* The system checks these against the expected value and tolerance limits.
* The result is labeled with the user’s name and pass/fail status is assigned.

#### 3. Backend Evaluation Logic

For each quality parameter:
* If a manual value is provided, it is used for evaluation.
* If no manual value exists and auto-check is triggered, a simulated value is generated.
* The system evaluates the difference between actual and expected values and determines compliance based on the allowed tolerance.

### Why This Matters

In production systems, actual values are sourced from:
* Laboratory results  
* IoT-based sensors  
* Manual entries by quality inspectors  

In prototypes or pilot demos, simulated values ensure that the entire quality check process can still be tested and demonstrated end-to-end.

### Controlling Behavior

| Mode                          | Description                                      | Triggered By                 |
|------------------------------|--------------------------------------------------|------------------------------|
| Manual Quality Check          | Inspector enters actual value                    | User                         |
| Auto-Generated (Simulated)    | Value is generated programmatically              | Backend (Auto-System)        |
| IoT / Real Sensor Integration | Value is fetched from connected hardware/sensors | External API/device (Future) |

To switch between modes:
* Disable simulation by removing or commenting out the auto-check logic.
* Integrate real sensors by connecting the backend to an IoT API or sensor input stream.

## Applications

* Manufacturing and industrial supply chains  
* Pharmaceutical and food safety compliance  
* Retail and consumer goods authenticity  
* Logistics and inventory management  

## System Architecture

* **Frontend**: React.js, Material-UI  
* **Backend**: Python (Flask), RESTful APIs  
* **Database**: SQLite (development) / PostgreSQL or MySQL (production)  
* **QR Code**: Python `qrcode` for generation, `jsQR` for scanning  

## Installation

### Prerequisites

* Python 3.x  
* Node.js and npm  
* (Optional) SQLite, PostgreSQL, or MySQL for database  

### Backend Setup

bash
git clone <your-repo-url>
cd <project-directory>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd migrations
alembic upgrade head
cd ..
python app.py

### Frontend Setup

bash
cd smart-label-frontend
npm install
npm start

## Usage

* Register products and batches via the dashboard.
* Generate and print QR code labels for each product or batch.
* Scan QR codes at any point in the supply chain to access product details and update workflow status.
* Use the analytics dashboard to monitor product movement, quality checks, and compliance.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## Author

Team Name: AI Tech

### Team Members

1. Prabhudev
   Email: mathpati8055@gmail.com

2. Prajwal
   Email: prajwalpankaj123@gmail.com

3. Surag
   Email: surudev29@gmail.com
   
5. Veeresh
   Email: pasareveeresh0908@gmail.com
   
7. Zaffar
   Email: mohammedZaffar072@gmail.com

