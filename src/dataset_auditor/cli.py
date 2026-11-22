import argparse, json
from .auditor import compute_health_score, sanitize_filename

def main():
    p = argparse.ArgumentParser(description="EVREN CV Dataset Quality Auditor CLI")
    p.add_argument("--labeled-ratio", type=float, default=1.0)
    p.add_argument("--unique-ratio", type=float, default=1.0)
    p.add_argument("--valid-box-ratio", type=float, default=1.0)
    args = p.parse_args()
    score, grade = compute_health_score(args.labeled_ratio, args.unique_ratio, args.valid_box_ratio)
    print(json.dumps({"health_score": score, "grade": grade}))

if __name__ == "__main__":
    main()
