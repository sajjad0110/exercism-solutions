def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    halfn = number // 2 + 1

    for i in range(1, halfn):
        if number % i == 0:
            factors.append(i)

    if sum(factors) == number:
        return "perfect"
    elif sum(factors) < number:
        return "deficient"
    else:
        return "abundant"
