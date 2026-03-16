def is_armstrong_number(number):
    digits = []
    total = 0
    while number > 0:
        num, digit = divmod(number, 10)
        digits.append(digit)
    for d in digits:
        total += d ** len(digits)
    return total == number
