"""Strict integer-answer scoring utility; not a training implementation."""
import argparse
import json
import re
from pathlib import Path


def parse_answer(text):
    if not isinstance(text, str):
        return None
    match = re.fullmatch(r"\s*<answer>([+-]?[0-9]+)</answer>\s*", text)
    return int(match.group(1)) if match else None


def score(rows):
    total = correct = formatted = 0
    seen = set()
    for row in rows:
        identity = row["id"]
        if not isinstance(identity, str) or not identity or identity in seen:
            raise ValueError("IDs must be unique non-empty strings")
        seen.add(identity)
        expected = row["expected"]
        if not isinstance(expected, str) or not re.fullmatch(r"[+-]?[0-9]+", expected):
            raise ValueError("expected must be an integer string")
        value = parse_answer(row["prediction"])
        total += 1
        formatted += value is not None
        correct += value is not None and value == int(expected)
    if not total:
        raise ValueError("Cannot evaluate an empty dataset")
    return {"total": total, "correct": correct, "formatted": formatted,
            "accuracy": correct / total, "format_rate": formatted / total}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", type=Path)
    args = parser.parse_args()
    with args.predictions.open(encoding="utf-8") as handle:
        rows = [json.loads(line) for line in handle if line.strip()]
    print(json.dumps(score(rows), indent=2))


if __name__ == "__main__":
    main()
