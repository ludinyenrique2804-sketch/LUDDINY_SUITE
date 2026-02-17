def get_country_flag(card):
    if card.startswith("4"):
        return "Visa", "🇺🇸"
    elif card.startswith("5"):
        return "MasterCard", "🇺🇸"
    elif card.startswith("3"):
        return "American Express", "🇺🇸"
    elif card.startswith("6"):
        return "Discover", "🇺🇸"
    elif card.startswith("30","38","39"):
        return "Diners Club","🇺🇸"
    elif card.startswith("35"):
        return "JCB","🇺🇸"
    else:
        return "Desconocida", "🌍"

