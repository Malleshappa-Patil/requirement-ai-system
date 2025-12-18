import os
import csv
from src.utils.text_preprocessing import clean_text

REQUIREMENTS_KEYWORDS = ["shall", "should", "must", "required to"]

def extract_requirements(input_file: str, output_file: str):
    requirements = []

    with open(input_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        cleaned_line = clean_text(line)
        if any(keyword in cleaned_line for keyword in REQUIREMENTS_KEYWORDS):
            requirements.append(cleaned_line)    

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["requirement_id", "requirement_text"])

        for idx, req in enumerate(requirements, start=1):
            writer.writerow([f"CR-{idx}", req])

    return requirements
