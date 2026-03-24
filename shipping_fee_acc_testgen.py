import csv
from itertools import product

totals = ["low", "medium", "high"]
premium = [True, False]
international = [True, False]

all_cases = list(product(totals, premium, international))

with open("acc_test_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["total_band", "premium", "international", "expected"])
    for total, prem, intl in all_cases:
        writer.writerow([total, prem, intl, ""])

print(len(all_cases))  # 12
print("Wrote ACC test cases to acc_test_data.csv")