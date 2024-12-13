#!/usr/bin/python3
"""
  Module: Game of choosing Prime numbers
"""


def primeNumbers(n):


    """
      Return list of prime numbers between 1 and n inclusive args
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


if __name__ == "__main__":
    print(primeNumbers(n))
