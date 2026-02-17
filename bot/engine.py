# bot/engine.py
import random
from bot.core.generator import generate_cards
from bot.bin_country import get_bin_info

def run_gen(qty=10):
    validas, invalidas = generate_cards(qty)
    return {
        "action": "gen",
        "status": "LIVE",
        "validas": validas,
        "invalidas": invalidas
    }

def run_mass(items):
    resultados = []

    for card in items:
        info = get_bin_info(card)
        resultados.append({
            "card": card,
            "status": "LIVE" if info else "DIE",
            "bank": info.get("bank", "UNKNOWN") if info else "UNKNOWN",
            "country": info.get("country", "UNKNOWN") if info else "UNKNOWN",
            "bin": card[:6]
        })

    return {
        "action": "mass",
        "results": resultados
    }

def run_estrass(pattern, qty=10):
    validas = []

    for _ in range(qty):
        card = fill_x(pattern)
        info = get_bin_info(card)
        validas.append({
            "card": card,
            "bank": info.get("bank", "UNKNOWN"),
            "country": info.get("country", "UNKNOWN"),
            "bin": card[:6]
        })

    return {
        "action": "estrass",
        "results": validas
    }

def fill_x(pattern):
    return "".join(str(random.randint(0,9)) if c.lower()=="x" else c for c in pattern)

