# Use the Euclidean algorithm since this applies
from .euclidean_algorithm import *


def xEqualToKEqb(k, b, p, q):
    """
    Returns x for the equation x^k ≡ b(mod m), Euler's formula
    :param k:
    :param b:
    :param p:
    :param q:
    :return:
    """
    m = p * q
    if euclideanAlgorithm1(b, m)[0] != 1 or euclideanAlgorithm1(k, (p - 1) * (q - 1))[0] != 1:
        return False
    g, u, v = euclideanAlgorithm1(k, (p - 1) * (q - 1))
    return (b ** u) % m
