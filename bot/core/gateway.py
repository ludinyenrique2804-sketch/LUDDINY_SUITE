def process_payment(card, mm, yy, cvv=None):
    # Validación básica SANDBOX ( pagos reales)

    if not mm.isdigit():
        return "MM inválido"

    mm = int(mm)
    if mm < 1 or mm > 12:
        return "MM fuera de rango"

    if not yy.isdigit():
        return "YY inválido"

    yy = int(yy)
    if yy < 24 or yy > 40:
        return "YY fuera de rango"

    return "APROBADO (SANDBOX)"

