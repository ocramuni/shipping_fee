import csv
from allpairspy import AllPairs

parameters = {
    "total_band": ["low", "medium", "high"],
    "premium": [True, False],
    "international": [True, False],
}


def main() -> None:
    keys = list(parameters.keys())
    values = [parameters[k] for k in keys]

    with open("test_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["total_band", "premium", "international", "expected"],
        )
        writer.writeheader()

        for combo in AllPairs(values):
            row = dict(zip(keys, combo))
            row["expected"] = ""  # to be filled manually
            writer.writerow(row)

    print("Generated pairwise combinations in test_data.csv")
    print("Now fill the expected column manually from the specification.")


if __name__ == "__main__":
    main()