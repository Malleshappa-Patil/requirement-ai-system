import csv
import os

def classify_requirement(text: str) -> str:
    if any(word in text for word in ["safe", "safety", "emergency", "hazard"]):
        return "Safety"
    elif any(word in text for word in ["speed", "time", "seconds", "ms", "performance"]):
        return "Performance"
    elif any(word in text for word in ["shall", "control", "activate", "support"]):
        return "Functional"
    else:
        return "Non-Functional"


def classify_requirements(input_csv: str, output_csv: str):
    classified_data = []

    with open(input_csv, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = classify_requirement(row["requirement_text"])
            row["category"] = category
            classified_data.append(row)

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["requirement_id", "requirement_text", "category"]
        )
        writer.writeheader()
        writer.writerows(classified_data)
