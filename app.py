def shipping_fee(total_band: str, premium: bool, international: bool) -> int:
    if premium:
        return 0
    if international:
        return 20 if total_band in {"low", "medium"} else 10
    return 10 if total_band == "low" else 5 if total_band == "medium" else 0