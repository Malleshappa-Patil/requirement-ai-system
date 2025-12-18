# requirement-ai-system

## 📌 Project Overview

In system engineering projects, customer requirements are often provided as large unstructured documents written in natural language.  
Manually reading, classifying, and mapping these requirements to system design and test cases is time-consuming and error-prone.

This project demonstrates a **proof of concept (PoC)** that uses **Python and basic NLP techniques** to automate key activities of **requirements engineering**, including:

- Requirement extraction  
- Requirement classification  
- Traceability mapping  
- Validation insights  

The goal is to support system engineers by reducing manual effort and improving consistency.

---

## 🎯 Problem Statement

Manual analysis of large customer requirement documents is slow, difficult to scale, and prone to human error.  
There is a need for an automated approach that can extract important requirements, organize them, and ensure traceability across the system development lifecycle.

This project addresses that need by building an **AI-assisted requirements engineering pipeline**.

---

## 🧠 Key Concepts Covered

- Requirements Engineering  
- Functional vs Non-Functional Requirements  
- Traceability Matrix  
- Validation and Coverage Checks  
- V-Model Alignment  
- NLP-based Text Processing  

---

## 🏗️ System Architecture (High Level)

Raw Requirement Documents
        ↓
Requirement Extraction
        ↓
Requirement Classification
        ↓
Traceability Mapping
        ↓
Validation & Reports


## 📂 Project Structure

requirements-ai-system/
│
├── data/
│ ├── raw/
│ │ ├── customer_requirements.txt
│ │ └── system_requirements.txt
│ │
│ └── processed/
│ ├── extracted_requirements.csv
│ └── classified_requirements.csv
│
├── outputs/
│ └── traceability_matrix.csv
│
├── src/
│ ├── extraction/
│ │ └── requirement_extractor.py
│ │
│ ├── classification/
│ │ └── requirement_classifier.py
│ │
│ ├── traceability/
│ │ └── traceability_mapper.py
│ │
│ ├── validation/
│ │ └── validation_checks.py
│ │
│ └── utils/
│ ├── text_preprocessing.py
│ └── similarity.py
│
├── main.py
├── pyproject.toml
└── README.md


---

## ⚙️ How the Pipeline Works

### 1. Requirement Extraction
- Reads customer requirement documents
- Identifies requirement sentences using keywords like `shall`, `must`, and `should`
- Outputs structured CSV data

### 2. Requirement Classification
- Classifies each requirement into:
  - Functional
  - Safety
  - Performance
  - Non-Functional
- Uses rule-based logic for explainability

### 3. Traceability Mapping
- Maps customer requirements to system requirements
- Uses text similarity to find the best matches
- Generates a traceability matrix

### 4. Validation
- Identifies unmapped or weakly mapped requirements
- Provides early validation insights

---

## 🚀 How to Run the Project (Using `uv`)

### 1️⃣ Create Virtual Environment
```bash
uv venv
```

### 2️⃣ Activate Environment
```
source .venv/bin/activate
```

### 3️⃣ Run the Pipeline
```
uv run python main.py
```

## Generated Outputs

After successful execution, the following files are auto-generated:

data/processed/extracted_requirements.csv
data/processed/classified_requirements.csv
outputs/traceability_matrix.csv

