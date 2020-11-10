# Use the Euclidean algorithm since this applies
from .euclidean_algorithm import *


def axEqualsCModM(a, c, m):
    """
    Returns the integer x to solve for ax being equivalent to c(mod m)
    ax ≡ c(mod m)
    :param a:
    :param c:
    :param m:
    :return:
    """
    g, u, v = euclideanAlgorithm1(a, m)
    x = ((u * c) // g) % m
    return x
