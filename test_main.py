import csv
import pytest

from app import shipping_fee

CSV_PATH = "acc_test_data.csv"

def parse_bool(value: str) -> bool:
    if value == "True":
        return True
    if value == "False":
        return False
    raise ValueError(f"Cannot parse boolean value: {value}")


def load_test_data():
    rows = []
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["expected"] == "":
                raise ValueError(
                    "Missing expected value in CSV. "
                    "Please complete the expected column before running pytest."
                )

            rows.append(
                pytest.param(
                    row["total_band"],
                    parse_bool(row["premium"]),
                    parse_bool(row["international"]),
                    int(row["expected"]),
                    id=(
                        f"total={row['total_band']},"
                        f"premium={row['premium']},"
                        f"international={row['international']}"
                    ),
                )
            )
    return rows


@pytest.mark.parametrize(
    "total_band, premium, international, expected",
    load_test_data(),
)
def test_shipping_fee(total_band, premium, international, expected):
    assert shipping_fee(total_band, premium, international) == expected