def factorial(n):
    """
    factorial(n)
    1 if n = 1
    n * factorial(n-1) if n > 1
    :param n:
    :return:
    """
    if n < 0:
        raise ValueError("Factorial doesn't exist for negative numbers")
    elif n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """
    0: return 0
    1: return 1
    n > 1: Fib(n-1) + Fib(n-2)
    :param n:
    :return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    """
    Euclid’s algorithm is one method to find the GCD of two numbers. Mathematically, we know
    that if r is the remainder (%) when a is divided by b, then gcd(a, b) = gcd(b, r)
    :param a:
    :param b:
    :return:
    """
    if a == 0:
        return b
    elif b == 0:
        return a 
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """
    -1 number if s1 < s2,
    0 if s1 == s2, and
    1 number if s1 > s2
    Do the comparison character by character
    :param s1:
    :param s2:
    :return:
    """
    # length = len(s1)
    if len(s1) > len(s2):
        return 1
    if len(s1) < len(s2):
        return - 1
    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    elif s1[0] == s2[0]:
        if len(s1) == 1 and len(s2) == 1:
            return 0
        return compareTo(s1[1::], s2[1::])


if __name__ == "__main__":
    for i in range(10):
        print(f"factorial({i}) = {factorial(i)}")

    # Fibonacci test
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(12) = {fibonacci(12)}")

    # GCD test
    print(f"gcd(24, 56) = {gcd(24, 56)}")
    print(f"gcd(100, 45) = {gcd(100, 45)}")

    # compare strings test
    print(f"compareTo('Alain', 'Alan') = {compareTo('Alain', 'Alan')}")
    print(f"compareTo('Rocker', 'rocker') = {compareTo('Rocker', 'rocker')}")
    print(f"compareTo('rocker', 'rocker') = {compareTo('rocker', 'rocker')}")
    print(f"compareTo('Rocker', Rocker') = {compareTo('Rocker', 'Rocker')}")
    print(f"compareTo('Rocker', Rrocer') = {compareTo('Rocker', 'Rocser')}")
    print(f"compareTo('Rocmer', Rocker') = {compareTo('Rocmer', 'Rocker')}")
    print(f"compareTo('Rocmer', Rocmmmmmer') = {compareTo('Rocmer', 'Rocmmmker')}")