import random

def generate_card():
    bin_code = random.choice(TEST_CARDS)
    body = "".join(str(random.randint(0, 9)) for _ in range(9))
    return bin_code + body + str(random.randint(0, 9))

import random

# NÚMEROS DE cc (SANDBOX)
TEST_CARDS = {
    "Visa":"4239376850324679",
    "Visa":"4357804703186627",
    "Visa":"4398356654496643",
    "Visa":"4797014703186627",
    "Visa":"4282232352991988",
    "Visa":"4790114387146520",
    "Visa":"4112296899418884",
    "Visa":"4114291014598758",
    "Express":"3774976965016984",
    "Express":"3489752965933763",
    "Express":"3444288423610222",
    "Express":"3486358633550157",
    "Express":"3480078879563704",
    "Descubrir":"6023474356245679",
    "Descubrir":"6012546586951597",
    "Descubrir":"6086478964532853",
    "Descubrir":"6034589541275501",
    "Descubrir":"6147358856831248",
    "Descubrir":"6198536432178002",
    "Descubrir":"6078398065421789",
    "MasterCard":"5449683896908613",
    "MasterCard":"5398136353226385",
    "MasterCard":"5219652394808798",
    "MasterCard":"5196381128625545",
    "MasterCard":"5332653456424498",
    "MasterCard":"5380634365249455",
    "JCB":"3571189537831012",
    "JCB":"3588769858583598",
    "JCB":"3572427342637011",
    "JCB":"3571455745858117",
    "JCB":"3535836238703255",
    "Diners Club":"3892384647985634",
    "Diners Club":"3044079146876964",
    "Diners Club":"3041506554269922",
    "Diners Club":"3029931807228159",
    "Diners Club":"3841576411894635"

}

def generate_cards(amount):
    cards = []

    for _ in range(amount):
        brand = random.choice(list(TEST_CARDS.keys()))
        number = TEST_CARDS[brand]

        # DATOS MOCK ( REALES)
        exp = f"{random.randint(1,12):02d}/2{random.randint(6,9)}"
        cvv = str(random.randint(100,999))

        cards.append({
            "brand": brand,
            "number": number,
            "exp": exp,
            "cvv": cvv
        })

    return card
import random


def luhn_checksum(number: str) -> int:
    # Limpia cualquier carácter que no sea dígito
    number = "".join(d for d in number if d.isdigit())

    if not number:
        return 1  # inválido

    digits = [int(d) for d in number[::-1]]
    total = 0

    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d

    return total % 10


def generate_luhn_number(prefixes=("3", "4", "5", "6"), length=16) -> str:
    prefix = random.choice(prefixes)

    # Asegura que el prefijo sea solo números
    prefix = "".join(d for d in prefix if d.isdigit())

    base = prefix
    while len(base) < length - 1:
        base += str(random.randint(0, 9))

    for check_digit in range(10):
        candidate = base + str(check_digit)
        if luhn_checksum(candidate) == 0:
            return candidate

    # Fallback (no debería ocurrir)
    return base + "0"


import random

def make_invalid(card: str) -> str:
    # Rompe Luhn cambiando el último dígito
    last = card[-1]
    new_last = "0" if last != "0" else "1"
    return card[:-1] + new_last

def generate_cards(qty: int):
    """
    Genera qty tarjetas:
    - mitad válidas (Luhn OK)
    - mitad inválidas (Luhn FAIL)
    """
    cards_valid = []
    cards_invalid = []

    half = qty // 2

    # VÁLIDAS
    for _ in range(half):
        number = generate_luhn_number()  # tu generador válido
        mm = f"{random.randint(1,12):02d}"
        yy = str(random.randint(26, 35))
        cvv = str(random.randint(100, 999))

        cards_valid.append({
            "number": number,
            "exp": f"{mm}|{yy}",
            "cvv": cvv,
            "status": "VALID"
        })

    # INVÁLIDAS
    for _ in range(half):
        base = generate_luhn_number()
        bad = make_invalid(base)
        mm = f"{random.randint(1,12):02d}"
        yy = str(random.randint(25, 30))
        cvv = str(random.randint(100, 999))

        cards_invalid.append({
            "number": bad,
            "exp": f"{mm}|{yy}",
            "cvv": cvv,
            "status": "INVALID"
        })

    return cards_valid, cards_invalid


def luhn_checksum(number: str) -> int:
    digits = [int(d) for d in number[::-1]]
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10

import random

def generate_from_bin(bin_code: str, length=16) -> str:
    # Asegurar que el BIN es numérico
    bin_code = "".join(d for d in bin_code if d.isdigit())

    if len(bin_code) != 6:
        raise ValueError("BIN inválido")

    base = bin_code

    while len(base) < length - 1:
        base += str(random.randint(0, 9))

    # Calcular dígito Luhn
    for i in range(10):
        candidate = base + str(i)
        if luhn_checksum(candidate) == 0:
            return candidate

    return base + "0"


