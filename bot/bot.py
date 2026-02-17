# -*- coding: utf-8 -*-
# =========================
# IMPORTS CORRECTOS
# =========================
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bot.core.logo import show_logo
from bot.core.generator import generate_cards
from bot.utils.colors import CYAN, RESET
from bot.utils.luhn import luhn_check
from bot.bin_country import get_bin_info
from bot.engine import run_gen, run_mass, run_estrass
import random


# =========================
# COLORES APK PRO
# =========================
MAGENTA = '\033[95m'   # VÁLIDAS
BLUE = '\033[94m'      # INVÁLIDAS
RESET = '\033[0m'

# =========================
# SONIDOS (TERMUX)
# =========================
def play_sound(command):
    if command == "gen":
        for _ in range(2):
            print("\a🪙", end="", flush=True)

    elif command == "mass":
        for _ in range(3):
            print("\a🪙🪙", end="", flush=True)

    elif command == "estrass":
        for _ in range(4):
            print("\a🪙🪙🪙", end="", flush=True)

    elif command == "exit":
        for _ in range(5):
            print("\a🪙🪙🪙🪙", end="", flush=True)

    print()  # salto de línea


# =========================
# BOT PRINCIPAL
# =========================
def start_bot(action=None):

    if action is not None:

        if action == "gen":
            return "GEN ejecutado"

        elif action == "mass":
            return "MASS ejecutado"

        elif action == "estrass":
            return "ESTRASS ejecutado"

        return "Acción no válida"


    # =========================
    # MODO WEB / FLASK
    # =========================
    if action is not None:

        if action == "gen":
            validas, invalidas = generate_cards(20)(50)
            status = "LIVE"
            card_type = "UNKNOWN""MASTERCARD""VISA""Diner""DISCO""AMEX""JCB"
            bank = "Chase Bank"
            country = "United States"

        elif action == "mass":
            validas, invalidas = generate_cards(10)
            status = "LIVE"
            card_type = "UNKNOWN""MASTERCARD""VISA""Diner""DISCO""AMEX""JCB"
            bank = "Bank of America"
            country = "United States"

        elif action == "estrass":
            validas, invalidas = generate_cards(25)
            status = "LIVE"
            card_type = "UNKNOWN""MASTERCARD""VISA""Diner""DISCO""AMEX""JCB"
            bank = "UNKNOWN""Bank of America""Chase Bank"
            country = "United States"

        else:
            return {
                "action": "ERROR",
                "status": "ERROR",
                "validas": [],
                "invalidas": [],
                "card": "UNKNOWN",
                "bank": "UNKNOWN",
                "country": "UNKNOWN"
            }

        # RESPUESTA PARA FLASK
        return {
            "action": action,
            "status": status,
            "validas": validas,
            "invalidas": invalidas,
            "card": card_type,
            "bank": bank,
            "country": country
        }

# =========================
# MODO CONSOLA
# =========================

    show_logo()
    print(CYAN + "╔══════════════════════════════════╗" + RESET)
    print(CYAN + "║        LUDDINY CHK BOT 💻📱🥷        ║" + RESET)
    print(CYAN + "╚══════════════════════════════════╝" + RESET)
    print("🗃️ help | 🌟 gen | 🪙 mass | 🤐 estrass | 🧠 manual | 🥷exit")


    while True:
        cmd = input("LUDDINY-BOT > ").strip().lower()

        # =========================
        # HELP
        # =========================
        if cmd == "help":
            print("""
🗃️ help       -> mostrar comandos
🌟 gen        -> generar tarjetas
🫥 mass       -> completar X (10)
🤐 estrass    -> completar X (25)
🥷 exit       -> salir del bot
""")
        # =========================
        # GEN
        # =========================
        elif cmd == "gen":
            play_sound("gen")
            qty = input("🔢 ¿Cuántas quieres generar?(20 / 50): ").strip()
            if qty not in ("20","50"):
               print("❌ Solo se permite 20 o 50")
               continue

            validas, invalidas = generate_cards(int(qty))

            print(f"\n{MAGENTA}╔═══ VÁLIDAS ✅💳🤑😈(20)o(50) ═══╗{RESET}\n")
            for c in validas:
                print(f"{MAGENTA}✅💳 {c['number']}|{c['exp']}|{c['cvv']}{RESET}")

            print(f"\n{BLUE}╔═══ INVÁLIDAS 💳❌😅☠️ (20)o(50) ═══╗{RESET}\n")
            for c in invalidas:
                print(f"{BLUE}❌💳 {c['number']}|{c['exp']}|{c['cvv']}{RESET}")

        # =========================
        # MASS
        # =========================
        elif cmd == "mass":
            play_sound("mass")
            print("🫥 MASS")
            print("Ejemplo: 4539XXXXXXXX563412|12|26|000")

            pattern = input("📥 Ingresa patrón: ").strip()

            if "x" not in pattern.lower():
                print("⚠️ El número no contiene 'x'")
                continue

            validas, invalidas = [], []

            # 10 válidas
            for _ in range(10):
                number = fill_x_numbers(pattern)
                mm = f"{random.randint(1,12):02d}"
                yy = str(random.randint(26, 36))
                cvv = f"{random.randint(000,999):03d}"
                validas.append((number, mm, yy, cvv))

            # 10 inválidas
            for _ in range(10):
                base = fill_x_numbers(pattern)
                bad = make_invalid(base)
                mm = f"{random.randint(1,12):02d}"
                yy = str(random.randint(26, 36))
                cvv = f"{random.randint(000,999):03d}"
                invalidas.append((bad, mm, yy, cvv))

            print(f"\n{MAGENTA}╔═══ VÁLIDAS✅😈✅(10) ═══╗{RESET}\n")
            for n, mm, yy, cvv in validas:
                print(f"{MAGENTA}💳🤑 {n}|{mm}|{yy}|{cvv}{RESET}")

            print(f"\n{BLUE}╔═══ INVÁLIDAS❌💳☠ (10) ═══╗{RESET}\n")
            for n, mm, yy, cvv in invalidas:
                print(f"{BLUE}💳☠ {n}|{mm}|{yy}|{cvv}{RESET}")

        # =========================
        # ESTRASS
        # =========================
        elif cmd == "estrass":
            play_sound("estrass")
            print("🤐 ESTRASS")
            print("Ejemplo: 463157xxxxxxxxxx|xx|xx|xxx")

            pattern = input("📥 Ingresa patrón: ").strip()

            if "x" not in pattern.lower():
                print("⚠️ El número no contiene 'x'")
                continue

            validas, invalidas = [], []

            # 25 válidas
            for _ in range(25):
                number = fill_x_numbers(pattern)
                mm = f"{random.randint(1,12):02d}"
                yy = str(random.randint(26, 36))
                cvv = f"{random.randint(000,999):03d}"
                validas.append((number, mm, yy, cvv))

            # 25 inválidas
            for _ in range(25):
                base = fill_x_numbers(pattern)
                bad = make_invalid(base)
                mm = f"{random.randint(1,12):02d}"
                yy = str(random.randint(26, 36))
                cvv = f"{random.randint(000,999):03d}"
                invalidas.append((bad, mm, yy, cvv))

            print(f"\n{MAGENTA}╔═══ VÁLIDAS✅😈✅ (25) ═══╗{RESET}\n")
            for n, mm, yy, cvv in validas:
                print(f"{MAGENTA}💳🤑 {n}|{mm}|{yy}|{cvv}{RESET}")

            print(f"\n{BLUE}╔═══ INVÁLIDAS❌☠❌ (25) ═══╗{RESET}\n")
            for n, mm, yy, cvv in invalidas:
                print(f"{BLUE}❌☠ {n}|{mm}|{yy}|{cvv}{RESET}")

        # =========================
        # MANUAL
        # =========================
        elif cmd == "manual":
            manual_input()

        # =========================
        # EXIT
        # =========================
        elif cmd == "exit":
            play_sound("exit")
            print("🥷 Bot detenido.")
            break

        else:
            print("⚠️ Comando no válido. Usa: help")


def make_invalid(card: str) -> str:
    last = card[-1]
    new_last = "0" if last != "0" else "1"
    return card[:-1] + new_last

def detect_card_type(card):
    if card.startswith("4"):
        return "VISA"
    elif card.startswith(("51", "52", "53", "54", "55")):
        return "MASTERCARD"
    elif card.startswith(("34", "37")):
        return "AMEX"
    elif card.startswith("6"):
        return "DISCO"
    elif card.startswith(("35","49","46")):
        return "JCB"
    elif card.startswith("36"):
        return "Diner"
    else:
        return "UNKNOWN"

def get_bin(card):
        return "bin card"

def manual_input():
    print("\n📥 MODO MANUAL")
    print("\n📥 Pega BIN (6) o TARJETA (13-16)")
    print("↩️ Enter vacío para procesar\n")

    items = []

    while True:
        line = input().strip()

        if line == "":
            break

        if not line.isdigit():
            print("❌ Entrada inválida")
            continue

        if len(line) == 6:
            items.append(("BIN", line))
        elif 13 <= len(line) <= 16:
            items.append(("CC", line))
        else:
            print("⚠️ Longitud inválida")

    validas, invalidas = [], []

    for tipo, value in items:
        for _ in range(25):
            number = generate_from_bin(value, 16) if tipo == "BIN" else value
            mm = f"{random.randint(1,12):02d}"
            yy = str(random.randint(26, 36))
            cvv = str(random.randint(000, 999))
            info = get_bin_info(number)
            validas.append((number, mm, yy, cvv, info))

        for _ in range(25):
            bad = make_invalid(generate_from_bin(value, 16))
            mm = f"{random.randint(1,12):02d}"
            yy = str(random.randint(26, 36))
            cvv = str(random.randint(000, 999))
            info = get_bin_info(bad)
            invalidas.append((bad, mm, yy, cvv, info))

    print(f"\n{MAGENTA}╔═══ VÁLIDAS ✅💳🤑😈 ═══╗{RESET}\n")
    for n, mm, yy, cvv, info in validas:
        print(f"{MAGENTA}✅💳 {n}|{mm}|{yy}|{cvv} | {info.get('brand','?')}{RESET}")

    print(f"\n{BLUE}╔═══ INVÁLIDAS 💳❌😅☠️ ═══╗{RESET}\n")
    for n, mm, yy, cvv, info in invalidas:
        print(f"{BLUE}❌💳 {n}|{mm}|{yy}|{cvv} | {info.get('brand','?')}{RESET}")

def fill_x_numbers(pattern: str) -> str:
    result = ""
    for ch in pattern:
        if ch.lower() == "x":
            result += str(random.randint(0, 9))
        else:
            result += ch
    return result

