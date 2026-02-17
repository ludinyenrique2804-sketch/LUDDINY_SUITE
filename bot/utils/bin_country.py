BINS = {
    "473724": ("Visa", "USA", "🇺🇸"),
    "490684": ("Visa", "USA", "🇺🇸"),
    "533234": ("MasterCard", "USA", "🇺🇸"),
    "371517": ("American Express", "USA", "🇺🇸"),
}

def get_bin_info(card):
    for bin_code, info in BINS.items():
        if card.startswith(bin_code):
            return info
    return ("Desconocida", "Global", "🌍")

