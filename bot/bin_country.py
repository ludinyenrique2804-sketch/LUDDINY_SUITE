BIN_DB = {
    "466474": {"country": "USA", "brand": "VISA"},
    "425907": {"country": "USA", "brand": "VISA"},
    "533265": {"country": "USA", "brand": "MASTERCARD"},
    "542687": {"country": "USA", "brand": "MASTERCARD"},
    "373831": {"country": "USA", "brand": "AMEX"},
    "362079": {"country": "USA", "brand": "DISCOVER"},
    "347356": {"country": "USA", "brand": "AMEX"},
    "389690": {"country": "USA", "brand": "Diners Club"},
    "466474": {"country": "USA", "brand": "JCB"},
    "498522": {"country": "USA", "brand": "JCB"},
    "656622": {"country": "USA", "brand": "DISCOVER"},
    "542687": {"country": "USA", "brand": "MASTERCARD"},
    "373831": {"country": "USA", "brand": "AMEX"},
    "645731": {"country": "USA", "brand": "DISCOVER"},
    "362020": {"country": "USA", "brand": "Diners  Club"},

}


def get_bin_info(card_number: str) -> dict:
    if not card_number or not card_number.isdigit():
        return {"country": "UNKNOWN", "brand": "UNKNOWN"}

    bin_code = card_number[:6]

    if bin_code in BIN_DB:
        return BIN_DB[bin_code]

    # Detección por prefijo
    if card_number.startswith("4"):
        return {"country": "USA", "brand": "VISA"}
    if card_number.startswith(("51", "52", "53", "54", "55")):
        return {"country": "USA", "brand": "MASTERCARD"}
    if card_number.startswith(("34", "37")):
        return {"country": "USA", "brand": "AMEX"}
    if card_number.startswith("6"):
        return {"country": "USA", "brand": "DISCOVER"}
    if card_number.startswith(("35","49","46")):
        return {"country": "USA", "brand": "JCB"}
    if card_number.startswith("36"):
        return {"country": "USA", "brand": "Diners Club"}

    return {"country": "UNKNOWN", "brand": "UNKNOWN"}

