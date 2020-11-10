
def gcd(a, b):
    """
    Returns the greatest common divisor among two integers
    gcd(a, b) = gcd(b, a % b)
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
