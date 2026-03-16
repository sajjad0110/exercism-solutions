def is_armstrong_number(number):
    power = len(str(number))
    total = 0
    nums = str(number)
    for n in nums:
        total += int(n) ** power
    return total == number
