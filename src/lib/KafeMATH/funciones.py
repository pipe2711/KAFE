import sys

# Constants

def pi():
    return 3.141592653589793


def e():
    return 2.718281828459045

# Exponential and Logarithmic functions

def exp(x):
    # Taylor series for e^x
    term = 1.0
    sum_ = 1.0
    for n in range(1, 30):
        term *= x / n
        sum_ += term
    return sum_


def log(x, base=None):
    # Natural logarithm using atanh series
    if x <= 0:
        raise ValueError("math domain error")
    y = (x - 1) / (x + 1)
    y2 = y * y
    term = y
    ln = 0.0
    # sum odd terms up to 99
    for n in range(1, 100, 2):
        ln += term / n
        term *= y2
    ln *= 2
    if base is None:
        return ln
    return ln / log(base)

# Power, square root

def pow_(x, y):
    return exp(y * log(x))


def sqrt(x):
    if x < 0:
        raise ValueError("math domain error")
    guess = x if x != 0 else 1.0
    for _ in range(20):
        guess = (guess + x / guess) / 2
    return guess

# Angular conversion

def degrees(x):
    return x * 180.0 / pi()


def radians(x):
    return x * pi() / 180.0

# Trigonometric functions

def sin(x):
    x = x % (2 * pi())
    term = x
    sum_ = term
    sign = -1
    for n in range(3, 30, 2):
        term *= x * x / ((n - 1) * n)
        sum_ += sign * term
        sign *= -1
    return sum_


def cos(x):
    x = x % (2 * pi())
    term = 1.0
    sum_ = term
    sign = -1
    for n in range(2, 30, 2):
        term *= x * x / ((n - 1) * n)
        sum_ += sign * term
        sign *= -1
    return sum_


def tan(x):
    c = cos(x)
    if c == 0:
        raise ValueError("math domain error")
    return sin(x) / c

# Inverse trigonometric functions

def asin(x):
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    term = x
    sum_ = term
    for n in range(1, 20):
        term *= (2 * n - 1)**2 * x * x / (2 * n * (2 * n + 1))
        sum_ += term
    return sum_


def acos(x):
    return pi() / 2 - asin(x)


def atan(x):
    if x == 0:
        return 0.0
    if abs(x) > 1:
        return pi() / 2 * (1 if x > 0 else -1) - atan(1 / x)
    term = x
    sum_ = term
    sign = -1
    for n in range(3, 50, 2):
        term *= x * x
        sum_ += sign * term / n
        sign *= -1
    return sum_

# Hyperbolic functions

def sinh(x):
    return (exp(x) - exp(-x)) / 2


def cosh(x):
    return (exp(x) + exp(-x)) / 2


def tanh(x):
    ex = exp(x)
    enx = exp(-x)
    return (ex - enx) / (ex + enx)

# Number-theoretic functions

def factorial(n):
    n = int(n)
    if n < 0:
        raise ValueError("factorial() no definido para valores negativos")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a, b):
    a, b = int(a), int(b)
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(int(a) * int(b)) // gcd(a, b)

# Floating point manipulation

def math_abs(x):
    return x if x >= 0 else -x


def floor(x):
    i = int(x)
    return i if x >= i else i - 1


def ceil(x):
    i = int(x)
    return i if x <= i else i + 1


def math_round(x, n=0):
    return round(x, n)

# Summation and product functions

def sum_range(a, b):
    return sum(range(int(a), int(b) + 1))


def prod_range(a, b):
    prod = 1
    for i in range(int(a), int(b) + 1):
        prod *= i
    return prod
