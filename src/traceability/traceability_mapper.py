import csv
import os
from src.utils.similarity import similarity_score

SIMILARITY_THRESHOLD = 0.5

def load_requirements(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def map_traceability(customer_csv, system_txt, output_csv):
    customer_reqs = load_requirements(customer_csv)

    with open(system_txt, "r") as file:
        system_reqs = [line.strip() for line in file.readlines()]

    traceability = []

    for cr in customer_reqs:
        best_match = None
        best_score = 0

        for sr in system_reqs:
            score = similarity_score(cr["requirement_text"], sr)
            if score > best_score:
                best_score = score
                best_match = sr

        status = "Mapped" if best_score >= SIMILARITY_THRESHOLD else "Unmapped"

        traceability.append({
            "customer_requirement_id": cr["requirement_id"],
            "customer_requirement": cr["requirement_text"],
            "system_requirement": best_match if status == "Mapped" else "",
            "similarity_score": round(best_score, 2),
            "status": status
        })

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "customer_requirement_id",
                "customer_requirement",
                "system_requirement",
                "similarity_score",
                "status"
            ]
        )
        writer.writeheader()
        writer.writerows(traceability)
