def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if 0 in sides:
        return False
    if a + b >= c and b + c >= a and c + a >= b and a == b == c:
        return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if 0 in sides:
        return False
    if a + b >= c and b + c >= a and c + a >= b:
        if a == b or b == c or c == a:
            return True
        return False
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if 0 in sides:
        return False
    if a + b >= c and b + c >= a and c + a >= b and a != b and b != c and c != a:
        return True
    return False
