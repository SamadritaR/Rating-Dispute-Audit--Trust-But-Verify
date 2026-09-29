"""Check a truthfulness delivery before it ships.

Every row labeled "Contains Inaccuracy" must carry evidence a customer can
verify on their own: the flagged claim (quoted verbatim from the response),
a correction, and a linked source. Rows missing any of these fail the check.

Usage: python scripts/audit_report.py data/dataset_i_audited.csv
"""
import csv
import sys

FLAG = "Contains Inaccuracy"


def check_row(row):
    """Return a list of problems with this row. Empty list means it passes."""
    problems = []
    if row["rater_label"] != FLAG:
        return problems
    claim = row["flagged_claim"].strip().strip('"')
    if not claim:
        problems.append("no flagged claim quoted")
    elif claim not in row["response"]:
        problems.append("flagged claim does not appear verbatim in the response")
    if not row["correction"].strip():
        problems.append("no correction given")
    if not row["source"].strip():
        problems.append("no source cited")
    elif "http" not in row["source"]:
        problems.append("source has no link the customer can open")
    return problems


def main(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))

    flagged = [r for r in rows if r["rater_label"] == FLAG]
    failures = {r["row"]: check_row(r) for r in rows if check_row(r)}
    disagreements = [r for r in rows if r["rater_label"] != r["audit_label"]]
    borderline = [r for r in flagged if "strictness" in r["confidence"]]

    print(f"Rows in delivery: {len(rows)}")
    print(f"Flagged as inaccurate: {len(flagged)}")
    print(f"Rater label overturned by independent audit: {len(disagreements)} of {len(rows)}")
    print(f"Borderline flags to review with the customer: {', '.join('row ' + r['row'] for r in borderline) or 'none'}")
    print()
    if failures:
        print("NOT READY TO SHIP. Flags missing evidence:")
        for row_id, problems in failures.items():
            print(f"  Row {row_id}: {'; '.join(problems)}")
        return 1
    print("READY TO SHIP. Every flag carries a verbatim claim, a correction, and a linked source.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data/dataset_i_audited.csv"))
