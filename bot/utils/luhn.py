def luhn_check(number):
    digits = [int(d) for d in number[::-1]]
    total = 0

    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0

