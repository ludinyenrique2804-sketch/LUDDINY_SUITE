from utils.luhn import luhn_check
from bin_country import get_bin_info

def check_card(card: str) -> str:
    info = get_bin_info(card)
    brand = info["brand"]
    country = info["country"]

    if not card.isdigit():
        return f"{card} | {brand} | {country} | ❌ NO NUMÉRICA"

    if not luhn_check(card):
        return f"{card} | {brand} | {country} | ❌ Luhn"

    return f"{card} | {brand} | {country} | ✅ SANDBOX"

