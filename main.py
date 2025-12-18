from src.extraction.requirement_extractor import extract_requirements
from src.classification.requirement_classification import classify_requirements
from src.traceability.traceability_mapper import map_traceability

RAW_CUSTOMER_REQ = "data/raw/customer_requirements.txt"
SYSTEM_REQ = "data/raw/system_requirements.txt"

EXTRACTED_CSV = "data/processed/extracted_requirements.csv"
CLASSIFIED_CSV = "data/processed/classified_requirements.csv"
TRACEABILITY_CSV = "outputs/traceability_matrix.csv"


def main():
    print("Step 1: Extracting requirements...")
    extract_requirements(RAW_CUSTOMER_REQ, EXTRACTED_CSV)

    print("Step 2: Classifying requirements...")
    classify_requirements(EXTRACTED_CSV, CLASSIFIED_CSV)

    print("Step 3: Mapping traceability...")
    map_traceability(CLASSIFIED_CSV, SYSTEM_REQ, TRACEABILITY_CSV)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
