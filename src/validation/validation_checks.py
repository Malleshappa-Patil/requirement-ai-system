def validate_traceability(traceability_data):
    issues = []

    for row in traceability_data:
        if row["status"] == "Unmapped":
            issues.append(
                f"Requirement {row['customer_requirement_id']} has no system mapping"
            )

    return issues
