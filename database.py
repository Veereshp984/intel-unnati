"""
Comprehensive database of Indian-specific products with quality parameters
This file contains detailed information about various Indian products and their quality checks
"""

import datetime

INDIAN_PRODUCTS_DATABASE = {
    "products": {
        "basmati_rice": {
            "name": "Basmati Rice",
            "category": "food",
            "subcategory": "rice",
            "description": "Premium long-grain aromatic rice",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Grain Length", "expected": "7.0", "unit": "mm", "tolerance": 0.5, "min_value": 6.5, "max_value": 7.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "sona_masoori_rice": {
            "name": "Sona Masoori Rice",
            "category": "food",
            "subcategory": "rice",
            "description": "Medium-grain rice for daily use",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Broken Grains", "expected": "5", "unit": "%", "tolerance": 1, "min_value": 4, "max_value": 6}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "kolam_rice": {
            "name": "Kolam Rice",
            "category": "food",
            "subcategory": "rice",
            "description": "Short-grain rice for South Indian dishes",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Broken Grains", "expected": "5", "unit": "%", "tolerance": 1, "min_value": 4, "max_value": 6}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "gobindo_bhog_rice": {
            "name": "Gobindo Bhog Rice",
            "category": "food",
            "subcategory": "rice",
            "description": "Aromatic short-grain rice for special dishes",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Grain Length", "expected": "4.5", "unit": "mm", "tolerance": 0.5, "min_value": 4.0, "max_value": 5.0}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "red_rice": {
            "name": "Red Rice",
            "category": "food",
            "subcategory": "rice",
            "description": "Nutritious unpolished red rice",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Fiber Content", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "black_rice": {
            "name": "Black Rice",
            "category": "food",
            "subcategory": "rice",
            "description": "Antioxidant-rich black rice",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Anthocyanin Content", "expected": "100", "unit": "mg/100g", "tolerance": 10, "min_value": 90, "max_value": 110}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "whole_wheat_atta": {
            "name": "Whole Wheat Flour (Atta)",
            "category": "food",
            "subcategory": "flour",
            "description": "Whole wheat flour for rotis",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 90,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "multigrain_atta": {
            "name": "Multigrain Atta",
            "category": "food",
            "subcategory": "flour",
            "description": "Blend of grains for nutritious rotis",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Fiber Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 90,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "chakki_atta": {
            "name": "Chakki Atta",
            "category": "food",
            "subcategory": "flour",
            "description": "Stone-ground whole wheat flour",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 90,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "toor_dal": {
            "name": "Toor Dal",
            "category": "food",
            "subcategory": "pulses",
            "description": "Split pigeon peas for dal",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "22", "unit": "%", "tolerance": 2, "min_value": 20, "max_value": 24}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "moong_dal": {
            "name": "Moong Dal",
            "category": "food",
            "subcategory": "pulses",
            "description": "Split mung beans for soups and khichdi",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "24", "unit": "%", "tolerance": 2, "min_value": 22, "max_value": 26}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "chana_dal": {
            "name": "Chana Dal",
            "category": "food",
            "subcategory": "pulses",
            "description": "Split chickpeas for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "urad_dal": {
            "name": "Urad Dal",
            "category": "food",
            "subcategory": "pulses",
            "description": "Split black gram for idli and dosa",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "24", "unit": "%", "tolerance": 2, "min_value": 22, "max_value": 26}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "masoor_dal": {
            "name": "Masoor Dal",
            "category": "food",
            "subcategory": "pulses",
            "description": "Red lentils for quick-cooking dal",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "25", "unit": "%", "tolerance": 2, "min_value": 23, "max_value": 27}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "rajma": {
            "name": "Rajma (Kidney Beans)",
            "category": "food",
            "subcategory": "pulses",
            "description": "Kidney beans for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "22", "unit": "%", "tolerance": 2, "min_value": 20, "max_value": 24}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "black_eyed_peas": {
            "name": "Black-Eyed Peas",
            "category": "food",
            "subcategory": "pulses",
            "description": "Nutritious beans for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "23", "unit": "%", "tolerance": 2, "min_value": 21, "max_value": 25}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "bajra_millet": {
            "name": "Bajra (Pearl Millet)",
            "category": "food",
            "subcategory": "millets",
            "description": "Nutritious millet for rotis",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "11", "unit": "%", "tolerance": 1, "min_value": 10, "max_value": 12}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "ragi_millet": {
            "name": "Ragi (Finger Millet)",
            "category": "food",
            "subcategory": "millets",
            "description": "Calcium-rich millet for porridges",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Calcium Content", "expected": "350", "unit": "mg/100g", "tolerance": 20, "min_value": 330, "max_value": 370}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "jowar_millet": {
            "name": "Jowar (Sorghum)",
            "category": "food",
            "subcategory": "millets",
            "description": "Gluten-free millet for rotis",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "foxtail_millet": {
            "name": "Foxtail Millet",
            "category": "food",
            "subcategory": "millets",
            "description": "Nutritious millet for rice dishes",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13},
                {"parameter": "Protein Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "besan_flour": {
            "name": "Besan (Chickpea Flour)",
            "category": "food",
            "subcategory": "flour",
            "description": "Chickpea flour for snacks and curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "maida_flour": {
            "name": "Maida (Refined Flour)",
            "category": "food",
            "subcategory": "flour",
            "description": "Refined wheat flour for baking",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "13", "unit": "%", "tolerance": 1, "min_value": 12, "max_value": 14},
                {"parameter": "Gluten Content", "expected": "8", "unit": "%", "tolerance": 1, "min_value": 7, "max_value": 9}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "sattu_flour": {
            "name": "Sattu (Roasted Gram Flour)",
            "category": "food",
            "subcategory": "flour",
            "description": "Roasted gram flour for drinks and snacks",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "8", "unit": "%", "tolerance": 1, "min_value": 7, "max_value": 9},
                {"parameter": "Protein Content", "expected": "22", "unit": "%", "tolerance": 2, "min_value": 20, "max_value": 24}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "cumin_seeds": {
            "name": "Cumin Seeds",
            "category": "food",
            "subcategory": "spices",
            "description": "Whole cumin seeds for seasoning",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "2.5", "unit": "%", "tolerance": 0.5, "min_value": 2.0, "max_value": 3.0}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "coriander_seeds": {
            "name": "Coriander Seeds",
            "category": "food",
            "subcategory": "spices",
            "description": "Whole coriander seeds for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "0.5", "unit": "%", "tolerance": 0.1, "min_value": 0.4, "max_value": 0.6}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "mustard_seeds": {
            "name": "Mustard Seeds",
            "category": "food",
            "subcategory": "spices",
            "description": "Whole mustard seeds for tempering",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "cloves": {
            "name": "Cloves",
            "category": "food",
            "subcategory": "spices",
            "description": "Whole cloves for aromatic flavor",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "cardamom_green": {
            "name": "Green Cardamom",
            "category": "food",
            "subcategory": "spices",
            "description": "Whole green cardamom for sweets and curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "4.0", "unit": "%", "tolerance": 0.5, "min_value": 3.5, "max_value": 4.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "cardamom_black": {
            "name": "Black Cardamom",
            "category": "food",
            "subcategory": "spices",
            "description": "Whole black cardamom for savory dishes",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "cinnamon": {
            "name": "Cinnamon",
            "category": "food",
            "subcategory": "spices",
            "description": "Cinnamon sticks for flavoring",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "star_anise": {
            "name": "Star Anise",
            "category": "food",
            "subcategory": "spices",
            "description": "Star-shaped spice for aromatic dishes",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "8.0", "unit": "%", "tolerance": 1, "min_value": 7, "max_value": 9}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "fennel_seeds": {
            "name": "Fennel Seeds",
            "category": "food",
            "subcategory": "spices",
            "description": "Sweet seeds for digestion and flavor",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.5", "unit": "%", "tolerance": 0.3, "min_value": 1.2, "max_value": 1.8}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "fenugreek_seeds": {
            "name": "Fenugreek Seeds",
            "category": "food",
            "subcategory": "spices",
            "description": "Bitter seeds for curries and health",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "25", "unit": "%", "tolerance": 2, "min_value": 23, "max_value": 27}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "turmeric_powder": {
            "name": "Turmeric Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Ground turmeric for curries and health",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Curcumin Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "red_chili_powder": {
            "name": "Red Chili Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Ground chili for spicy flavor",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Capsaicin Content", "expected": "0.5", "unit": "%", "tolerance": 0.1, "min_value": 0.4, "max_value": 0.6}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "coriander_powder": {
            "name": "Coriander Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Ground coriander for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "0.5", "unit": "%", "tolerance": 0.1, "min_value": 0.4, "max_value": 0.6}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "cumin_powder": {
            "name": "Cumin Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Ground cumin for seasoning",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "2.5", "unit": "%", "tolerance": 0.5, "min_value": 2.0, "max_value": 3.0}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "garam_masala": {
            "name": "Garam Masala",
            "category": "food",
            "subcategory": "spices",
            "description": "Blended spice mix for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "amchur_powder": {
            "name": "Amchur (Dried Mango Powder)",
            "category": "food",
            "subcategory": "spices",
            "description": "Tangy powder for curries",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Acidity", "expected": "5.0", "unit": "%", "tolerance": 0.5, "min_value": 4.5, "max_value": 5.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "kashmiri_chili_powder": {
            "name": "Kashmiri Chili Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Mild red chili powder for color",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Capsaicin Content", "expected": "0.3", "unit": "%", "tolerance": 0.1, "min_value": 0.2, "max_value": 0.4}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "chole_masala": {
            "name": "Chole Masala",
            "category": "food",
            "subcategory": "spices",
            "description": "Spice blend for chickpea curry",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "pav_bhaji_masala": {
            "name": "Pav Bhaji Masala",
            "category": "food",
            "subcategory": "spices",
            "description": "Spice blend for pav bhaji",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "biryani_masala": {
            "name": "Biryani Masala",
            "category": "food",
            "subcategory": "spices",
            "description": "Spice blend for biryani",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "tandoori_masala": {
            "name": "Tandoori Masala",
            "category": "food",
            "subcategory": "spices",
            "description": "Spice blend for tandoori dishes",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "sambar_powder": {
            "name": "Sambar Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Spice blend for South Indian sambar",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "rasam_powder": {
            "name": "Rasam Powder",
            "category": "food",
            "subcategory": "spices",
            "description": "Spice blend for South Indian rasam",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Volatile Oil", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "50%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License"]
        },
        "haldirams_aloo_bhujia": {
            "name": "Haldiram's Aloo Bhujia",
            "category": "food",
            "subcategory": "snacks",
            "description": "Spicy potato-based snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 150,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "haldirams_bhujia_sev": {
            "name": "Haldiram's Bhujia Sev",
            "category": "food",
            "subcategory": "snacks",
            "description": "Crispy gram flour snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "22", "unit": "%", "tolerance": 2, "min_value": 20, "max_value": 24}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 150,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "haldirams_moong_dal_namkeen": {
            "name": "Haldiram's Moong Dal Namkeen",
            "category": "food",
            "subcategory": "snacks",
            "description": "Fried moong dal snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 150,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "haldirams_khatta_meetha": {
            "name": "Haldiram's Khatta Meetha",
            "category": "food",
            "subcategory": "snacks",
            "description": "Sweet and tangy namkeen mix",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Sugar Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 150,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "haldirams_boondi": {
            "name": "Haldiram's Boondi",
            "category": "food",
            "subcategory": "snacks",
            "description": "Crispy gram flour balls",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 150,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "lays_magic_masala": {
            "name": "Lay's Magic Masala",
            "category": "food",
            "subcategory": "snacks",
            "description": "Spicy flavored potato chips",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5},
                {"parameter": "Fat Content", "expected": "30", "unit": "%", "tolerance": 2, "min_value": 28, "max_value": 32}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "balaji_wafers": {
            "name": "Balaji Wafers",
            "category": "food",
            "subcategory": "snacks",
            "description": "Crispy potato wafers",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5},
                {"parameter": "Fat Content", "expected": "30", "unit": "%", "tolerance": 2, "min_value": 28, "max_value": 32}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "bingo_mad_angles": {
            "name": "Bingo! Mad Angles",
            "category": "food",
            "subcategory": "snacks",
            "description": "Triangular crunchy snacks",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "25", "unit": "%", "tolerance": 2, "min_value": 23, "max_value": 27}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "murukku": {
            "name": "Murukku",
            "category": "food",
            "subcategory": "snacks",
            "description": "South Indian crispy rice flour snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "chakli": {
            "name": "Chakli",
            "category": "food",
            "subcategory": "snacks",
            "description": "Spiral-shaped rice flour snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "thattai": {
            "name": "Thattai",
            "category": "food",
            "subcategory": "snacks",
            "description": "South Indian flat rice snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "poha_chivda": {
            "name": "Poha Chivda",
            "category": "food",
            "subcategory": "snacks",
            "description": "Spiced flattened rice snack",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "3.0", "unit": "%", "tolerance": 0.5, "min_value": 2.5, "max_value": 3.5},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 120,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "sabudana_papad": {
            "name": "Sabudana Papad",
            "category": "food",
            "subcategory": "snacks",
            "description": "Sago-based crispy papad",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "onion_bhaji": {
            "name": "Onion Bhaji",
            "category": "food",
            "subcategory": "snacks",
            "description": "Fried onion fritters",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "vegetable_pakora": {
            "name": "Vegetable Pakora",
            "category": "food",
            "subcategory": "snacks",
            "description": "Mixed vegetable fritters",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "paneer_pakora": {
            "name": "Paneer Pakora",
            "category": "food",
            "subcategory": "snacks",
            "description": "Fried paneer fritters",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mccain_samosa": {
            "name": "McCain Frozen Samosa",
            "category": "food",
            "subcategory": "snacks",
            "description": "Frozen samosas with spiced filling",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "-18°C", "humidity": "NA"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "haldirams_samosa": {
            "name": "Haldiram's Frozen Samosa",
            "category": "food",
            "subcategory": "snacks",
            "description": "Frozen samosas with potato filling",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "-18°C", "humidity": "NA"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "dal_kachori": {
            "name": "Dal Kachori",
            "category": "food",
            "subcategory": "snacks",
            "description": "Fried pastry with lentil filling",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "pyaaz_kachori": {
            "name": "Pyaaz Kachori",
            "category": "food",
            "subcategory": "snacks",
            "description": "Fried pastry with onion filling",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mtr_gulab_jamun": {
            "name": "MTR Gulab Jamun",
            "category": "food",
            "subcategory": "sweets",
            "description": "Soft milk-based sweet in syrup",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55},
                {"parameter": "Moisture Content", "expected": "30", "unit": "%", "tolerance": 3, "min_value": 27, "max_value": 33}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "haldirams_rasgulla": {
            "name": "Haldiram's Rasgulla",
            "category": "food",
            "subcategory": "sweets",
            "description": "Spongy cheese balls in sugar syrup",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55},
                {"parameter": "Moisture Content", "expected": "30", "unit": "%", "tolerance": 3, "min_value": 27, "max_value": 33}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "jalebi": {
            "name": "Jalebi",
            "category": "food",
            "subcategory": "sweets",
            "description": "Crispy fried sweet in syrup",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "soan_papdi": {
            "name": "Soan Papdi",
            "category": "food",
            "subcategory": "sweets",
            "description": "Flaky layered sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 90,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "kaju_barfi": {
            "name": "Kaju Barfi",
            "category": "food",
            "subcategory": "sweets",
            "description": "Cashew-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "besan_barfi": {
            "name": "Besan Barfi",
            "category": "food",
            "subcategory": "sweets",
            "description": "Chickpea flour-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "milk_barfi": {
            "name": "Milk Barfi",
            "category": "food",
            "subcategory": "sweets",
            "description": "Milk-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mysore_pak": {
            "name": "Mysore Pak",
            "category": "food",
            "subcategory": "sweets",
            "description": "Rich ghee-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "30", "unit": "%", "tolerance": 3, "min_value": 27, "max_value": 33}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "peda": {
            "name": "Peda",
            "category": "food",
            "subcategory": "sweets",
            "description": "Milk-based sweet rounds",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "malpua": {
            "name": "Malpua",
            "category": "food",
            "subcategory": "sweets",
            "description": "Sweet pancakes in syrup",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "balushahi": {
            "name": "Balushahi",
            "category": "food",
            "subcategory": "sweets",
            "description": "Flaky fried sweet in syrup",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "khaja": {
            "name": "Khaja",
            "category": "food",
            "subcategory": "sweets",
            "description": "Layered fried sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "chhena_poda": {
            "name": "Chhena Poda",
            "category": "food",
            "subcategory": "sweets",
            "description": "Baked cheese dessert",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "30", "unit": "%", "tolerance": 5, "min_value": 25, "max_value": 35},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "gajar_ka_halwa": {
            "name": "Gajar ka Halwa",
            "category": "food",
            "subcategory": "sweets",
            "description": "Carrot-based sweet dessert",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "30", "unit": "%", "tolerance": 5, "min_value": 25, "max_value": 35},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "sooji_halwa": {
            "name": "Sooji Halwa",
            "category": "food",
            "subcategory": "sweets",
            "description": "Semolina-based sweet dessert",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "30", "unit": "%", "tolerance": 5, "min_value": 25, "max_value": 35},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "moong_dal_halwa": {
            "name": "Moong Dal Halwa",
            "category": "food",
            "subcategory": "sweets",
            "description": "Lentil-based sweet dessert",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "30", "unit": "%", "tolerance": 5, "min_value": 25, "max_value": 35},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
    
        "amul_milk_cake": {
            "name": "Amul Milk Cake",
            "category": "food",
            "subcategory": "sweets",
            "description": "Rich milk-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "bikaneri_laddoo": {
            "name": "Bikaneri Laddoo",
            "category": "food",
            "subcategory": "sweets",
            "description": "Gram flour-based sweet balls",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "motichoor_laddoo": {
            "name": "Motichoor Laddoo",
            "category": "food",
            "subcategory": "sweets",
            "description": "Fine gram flour sweet balls",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "kheer_kadam": {
            "name": "Kheer Kadam",
            "category": "food",
            "subcategory": "sweets",
            "description": "Layered milk-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "sandesh": {
            "name": "Sandesh",
            "category": "food",
            "subcategory": "sweets",
            "description": "Bengali milk-based sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "30", "unit": "%", "tolerance": 5, "min_value": 25, "max_value": 35},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "rasmalai": {
            "name": "Rasmalai",
            "category": "food",
            "subcategory": "sweets",
            "description": "Cheese balls in sweetened milk",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 7,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "petha": {
            "name": "Petha",
            "category": "food",
            "subcategory": "sweets",
            "description": "Ash gourd-based translucent sweet",
            "quality_parameters": [
                {"parameter": "Sugar Content", "expected": "60", "unit": "%", "tolerance": 5, "min_value": 55, "max_value": 65},
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 3, "min_value": 17, "max_value": 23}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 60,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "amul_ghee": {
            "name": "Amul Ghee",
            "category": "food",
            "subcategory": "dairy",
            "description": "Clarified butter for cooking",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "99.7", "unit": "%", "tolerance": 0.2, "min_value": 99.5, "max_value": 99.9},
                {"parameter": "Moisture Content", "expected": "0.3", "unit": "%", "tolerance": 0.1, "min_value": 0.2, "max_value": 0.4}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 270,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mother_dairy_ghee": {
            "name": "Mother Dairy Ghee",
            "category": "food",
            "subcategory": "dairy",
            "description": "Pure clarified butter",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "99.7", "unit": "%", "tolerance": 0.2, "min_value": 99.5, "max_value": 99.9},
                {"parameter": "Moisture Content", "expected": "0.3", "unit": "%", "tolerance": 0.1, "min_value": 0.2, "max_value": 0.4}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 270,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "amul_butter": {
            "name": "Amul Butter",
            "category": "food",
            "subcategory": "dairy",
            "description": "Creamy salted butter",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "80", "unit": "%", "tolerance": 2, "min_value": 78, "max_value": 82},
                {"parameter": "Moisture Content", "expected": "16", "unit": "%", "tolerance": 2, "min_value": 14, "max_value": 18}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mother_dairy_butter": {
            "name": "Mother Dairy Butter",
            "category": "food",
            "subcategory": "dairy",
            "description": "Smooth salted butter",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "80", "unit": "%", "tolerance": 2, "min_value": 78, "max_value": 82},
                {"parameter": "Moisture Content", "expected": "16", "unit": "%", "tolerance": 2, "min_value": 14, "max_value": 18}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "amul_paneer": {
            "name": "Amul Paneer",
            "category": "food",
            "subcategory": "dairy",
            "description": "Fresh Indian cottage cheese",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Moisture Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mother_dairy_paneer": {
            "name": "Mother Dairy Paneer",
            "category": "food",
            "subcategory": "dairy",
            "description": "Soft Indian cottage cheese",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Moisture Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 30,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "amul_dahi": {
            "name": "Amul Dahi",
            "category": "food",
            "subcategory": "dairy",
            "description": "Creamy Indian yogurt",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "3.5", "unit": "%", "tolerance": 0.5, "min_value": 3.0, "max_value": 4.0},
                {"parameter": "Moisture Content", "expected": "85", "unit": "%", "tolerance": 5, "min_value": 80, "max_value": 90}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mother_dairy_dahi": {
            "name": "Mother Dairy Dahi",
            "category": "food",
            "subcategory": "dairy",
            "description": "Thick Indian yogurt",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "3.5", "unit": "%", "tolerance": 0.5, "min_value": 3.0, "max_value": 4.0},
                {"parameter": "Moisture Content", "expected": "85", "unit": "%", "tolerance": 5, "min_value": 80, "max_value": 90}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "patanjali_dahi": {
            "name": "Patanjali Dahi",
            "category": "food",
            "subcategory": "dairy",
            "description": "Traditional Indian yogurt",
            "quality_parameters": [
                {"parameter": "Fat Content", "expected": "3.5", "unit": "%", "tolerance": 0.5, "min_value": 3.0, "max_value": 4.0},
                {"parameter": "Moisture Content", "expected": "85", "unit": "%", "tolerance": 5, "min_value": 80, "max_value": 90}
            ],
            "storage_conditions": {"temperature": "4°C", "humidity": "NA"},
            "shelf_life_days": 15,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "dabur_honey": {
            "name": "Dabur Honey",
            "category": "food",
            "subcategory": "sweeteners",
            "description": "Pure natural honey",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Fructose Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "patanjali_honey": {
            "name": "Patanjali Honey",
            "category": "food",
            "subcategory": "sweeteners",
            "description": "Pure organic honey",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Fructose Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "saffola_honey": {
            "name": "Saffola Honey",
            "category": "food",
            "subcategory": "sweeteners",
            "description": "Pure honey for health",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Fructose Content", "expected": "40", "unit": "%", "tolerance": 5, "min_value": 35, "max_value": 45}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "jaggery": {
            "name": "Jaggery",
            "category": "food",
            "subcategory": "sweeteners",
            "description": "Unrefined cane sugar",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 12},
                {"parameter": "Sucrose Content", "expected": "70", "unit": "%", "tolerance": 5, "min_value": 65, "max_value": 75}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "palm_jaggery": {
            "name": "Palm Jaggery",
            "category": "food",
            "subcategory": "sweeteners",
            "description": "Sweetener from palm sap",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 12},
                {"parameter": "Sucrose Content", "expected": "70", "unit": "%", "tolerance": 5, "min_value": 65, "max_value": 75}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mtr_idli_dosa_mix": {
            "name": "MTR Idli Dosa Mix",
            "category": "food",
            "subcategory": "instant mixes",
            "description": "Instant mix for idli and dosa",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mtr_vada_mix": {
            "name": "MTR Vada Mix",
            "category": "food",
            "subcategory": "instant mixes",
            "description": "Instant mix for crispy vadas",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mtr_upma_mix": {
            "name": "MTR Upma Mix",
            "category": "food",
            "subcategory": "instant mixes",
            "description": "Instant mix for semolina upma",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "5", "unit": "%", "tolerance": 1, "min_value": 4, "max_value": 6}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mtr_khaman_dhokla_mix": {
            "name": "MTR Khaman Dhokla Mix",
            "category": "food",
            "subcategory": "instant mixes",
            "description": "Instant mix for Gujarati dhokla",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 180,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "bambino_vermicelli": {
            "name": "Bambino Vermicelli",
            "category": "food",
            "subcategory": "pasta",
            "description": "Semolina-based vermicelli",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "maggi_masala_noodles": {
            "name": "Maggi Masala Noodles",
            "category": "food",
            "subcategory": "noodles",
            "description": "Instant noodles with masala flavor",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 270,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "yippie_noodles": {
            "name": "Yippie Noodles",
            "category": "food",
            "subcategory": "noodles",
            "description": "Instant noodles with spicy seasoning",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fat Content", "expected": "15", "unit": "%", "tolerance": 2, "min_value": 13, "max_value": 17}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 270,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "sunfeast_pasta": {
            "name": "Sunfeast Pasta",
            "category": "food",
            "subcategory": "pasta",
            "description": "Durum wheat pasta with masala",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Protein Content", "expected": "12", "unit": "%", "tolerance": 1, "min_value": 11, "max_value": 13}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "patanjali_noodles": {
            "name": "Patanjali Atta Noodles",
            "category": "food",
            "subcategory": "noodles",
            "description": "Whole wheat instant noodles",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 1, "min_value": 9, "max_value": 11},
                {"parameter": "Fiber Content", "expected": "2.0", "unit": "%", "tolerance": 0.5, "min_value": 1.5, "max_value": 2.5}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 270,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "knorr_soup": {
            "name": "Knorr Soup",
            "category": "food",
            "subcategory": "instant mixes",
            "description": "Instant soup mix",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "5", "unit": "%", "tolerance": 1, "min_value": 4, "max_value": 6},
                {"parameter": "Sodium Content", "expected": "1.0", "unit": "%", "tolerance": 0.2, "min_value": 0.8, "max_value": 1.2}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "mtr_badam_drink_mix": {
            "name": "MTR Badam Drink Mix",
            "category": "food",
            "subcategory": "beverage mixes",
            "description": "Almond-flavored drink mix",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "5", "unit": "%", "tolerance": 1, "min_value": 4, "max_value": 6},
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "40%"},
            "shelf_life_days": 365,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian"]
        },
        "dabur_chyawanprash": {
            "name": "Dabur Chyawanprash",
            "category": "food",
            "subcategory": "health supplements",
            "description": "Ayurvedic herbal jam",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian", "Ayurvedic"]
        },
        "patanjali_chyawanprash": {
            "name": "Patanjali Chyawanprash",
            "category": "food",
            "subcategory": "health supplements",
            "description": "Ayurvedic immunity booster",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian", "Ayurvedic"]
        },
        "zandu_kesari_jeevan": {
            "name": "Zandu Kesari Jeevan",
            "category": "food",
            "subcategory": "health supplements",
            "description": "Saffron-based health supplement",
            "quality_parameters": [
                {"parameter": "Moisture Content", "expected": "20", "unit": "%", "tolerance": 2, "min_value": 18, "max_value": 22},
                {"parameter": "Sugar Content", "expected": "50", "unit": "%", "tolerance": 5, "min_value": 45, "max_value": 55}
            ],
            "storage_conditions": {"temperature": "Room Temperature", "humidity": "NA"},
            "shelf_life_days": 730,
            "regulatory_standards": ["FSSAI"],
            "certifications": ["FSSAI License", "Vegetarian", "Ayurvedic"]
        }
    }
}

# Add category defaults for fallback
CATEGORY_DEFAULTS = {
    "food": [
        {"parameter": "Moisture Content", "expected": "10", "unit": "%", "tolerance": 2, "min_value": 8, "max_value": 12}
    ],
    "personal_care": [
        {"parameter": "pH", "expected": "7.0", "unit": "", "tolerance": 1, "min_value": 6, "max_value": 8}
    ]
}

def standardize_key(name):
    return name.strip().lower().replace(" ", "_")

def get_product_by_key(product_key):
    # Try direct key
    prod = INDIAN_PRODUCTS_DATABASE["products"].get(product_key)
    if prod:
        return prod
    # Try standardized key
    std_key = standardize_key(product_key)
    return INDIAN_PRODUCTS_DATABASE["products"].get(std_key)

def get_product_quality_parameters(product_key):
    product = get_product_by_key(product_key)
    if product and product.get("quality_parameters"):
        return product["quality_parameters"]
    # Fallback to category defaults
    if product and product.get("category"):
        return CATEGORY_DEFAULTS.get(product["category"], [])
    return []

# Helper functions to work with the database
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

def is_product_good(product_key):
    product = get_product_by_key(product_key)
    if not product:
        return False, "Product not found."
    # Parse manufacturing and expiry dates
    try:
        mfg = product.get("manufacturing_date")
        exp = product.get("expiry_date")
        if not mfg or not exp:
            return False, "Manufacturing or expiry date missing."
        mfg_date = datetime.datetime.fromisoformat(str(mfg))
        exp_date = datetime.datetime.fromisoformat(str(exp))
        now = datetime.datetime.now()
        if now < mfg_date:
            return False, "Product manufacturing date is in the future."
        if now > exp_date:
            return False, "Product is expired."
        return True, "Product is within shelf life and not expired."
    except Exception as e:
        return False, f"Date parsing error: {e}"

def is_product_good_from_obj(product):
    if not product:
        return False, "Product not found."
    try:
        # Support both dict and ORM object
        mfg = product.get("manufacturing_date") if isinstance(product, dict) else getattr(product, "manufacturing_date", None)
        exp = product.get("expiry_date") if isinstance(product, dict) else getattr(product, "expiry_date", None)
        if not mfg or not exp:
            return False, "Manufacturing or expiry date missing."
        # If these are datetime objects, use them directly; else parse
        if isinstance(mfg, str):
            mfg_date = datetime.datetime.fromisoformat(str(mfg))
        else:
            mfg_date = mfg
        if isinstance(exp, str):
            exp_date = datetime.datetime.fromisoformat(str(exp))
        else:
            exp_date = exp
        now = datetime.datetime.now()
        if now < mfg_date:
            return False, "Product manufacturing date is in the future."
        if now > exp_date:
            return False, "Product is expired."
        return True, "Product is within shelf life and not expired."
    except Exception as e:
        return False, f"Date parsing error: {e}"