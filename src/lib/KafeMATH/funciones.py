
# ===== Constantes =====


def pi():
    return 3.141592653589793

def e():
    return 2.718281828459045

# Constantes fundamentales
tau = 2 * pi()
inf = float('inf')
nan = float('nan')

# ===== Exponenciales y logaritmos =====

def exp(x):
    term = 1.0
    sum_ = 1.0
    for n in range(1, 50):
        term *= x / n
        sum_ += term
    return sum_

def log(x, base=None):
    if base is None and x == e():
        return 1.0
    if x <= 0:
        raise ValueError("math domain error")
    y = (x - 1) / (x + 1)
    y2 = y * y
    term = y
    ln = 0.0
    for n in range(1, 200, 2):
        ln += term / n
        term *= y2
    ln *= 2
    if base is None:
        return ln
    return ln / log(base)

# ===== Potencia y raíz cuadrada =====

def pow_(x, y):
    return exp(y * log(x))

def sqrt(x):
    if x < 0:
        raise ValueError("math domain error")
    guess = x if x != 0 else 1.0
    for _ in range(30):
        guess = (guess + x / guess) / 2
    return guess

# ===== Conversión de ángulos =====

def degrees(x):
    return x * 180.0 / pi()

def radians(x):
    return x * pi() / 180.0

# ===== Funciones trigonométricas =====

def sin(x):
    x = x % (2 * pi())
    term = x
    sum_ = term
    sign = -1
    for n in range(3, 50, 2):
        term *= x * x / ((n - 1) * n)
        sum_ += sign * term
        sign *= -1
    return sum_

def cos(x):
    x = x % (2 * pi())
    term = 1.0
    sum_ = term
    sign = -1
    for n in range(2, 50, 2):
        term *= x * x / ((n - 1) * n)
        sum_ += sign * term
        sign *= -1
    return sum_

def tan(x):
    c = cos(x)
    if c == 0:
        raise ValueError("math domain error")
    return sin(x) / c

# ===== Funciones inversas =====

def asin(x):
    if x == 1:
        return pi() / 2
    if x == -1:
        return -pi() / 2
    if x < -1 or x > 1:
        raise ValueError("math domain error")
    term = x
    sum_ = term
    for n in range(1, 200):
        term *= (2 * n - 1)**2 * x * x / (2 * n * (2 * n + 1))
        sum_ += term
    return sum_

def acos(x):
    if x == 1:
        return 0.0
    if x == -1:
        return pi()
    return pi() / 2 - asin(x)

def atan(x):
    if x == 0:
        return 0.0
    if abs(x) > 1:
        return pi() / 2 * (1 if x > 0 else -1) - atan(1 / x)
    term = x
    sum_ = term
    sign = -1
    for n in range(3, 1000, 2):
        term *= x * x
        sum_ += sign * term / n
        sign *= -1
    return sum_

# ===== Funciones hiperbólicas =====

def sinh(x):
    return (exp(x) - exp(-x)) / 2

def cosh(x):
    return (exp(x) + exp(-x)) / 2

def tanh(x):
    ex = exp(x)
    enx = exp(-x)
    return (ex - enx) / (ex + enx)

# ===== Funciones de teoría de números =====

def factorial(n):
    n = int(n)
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def comb(n, k):
    n, k = int(n), int(k)
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def perm(n, k):
    n, k = int(n), int(k)
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(n - k + 1, n + 1):
        result *= i
    return result

def gcd(*ints):
    result = abs(int(ints[0]))
    for x in ints[1:]:
        a, b = result, int(x)
        while b:
            a, b = b, a % b
        result = abs(a)
    return result

def lcm(*ints):
    def _lcm(a, b):
        return abs(a * b) // gcd(a, b)
    result = int(ints[0])
    for x in ints[1:]:
        result = _lcm(result, int(x))
    return result

# ===== Aritmética flotante =====

def trunc(x):
    return int(x)

def fmod(x, y):
    if y == 0:
        raise ValueError("math domain error")
    return x - y * trunc(x / y)

def remainder(x, y):
    if y == 0:
        raise ValueError("math domain error")
    res = x - y * round(x / y)
    return round(res, 10)

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

def copysign(x, y):
    x, y = float(x), float(y)
    if y == 0.0 and y.hex().startswith('-'):
        return -abs(x)
    return abs(x) if y >= 0 else -abs(x)

def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
 
    if a == b:
        return True
    diff = abs(a - b)
    tol = max(rel_tol * max(abs(a), abs(b)), abs_tol)
    if diff >= tol:
        return True
    if b != 0:
        return abs(a/b - 1) <= rel_tol
    return False

def isfinite(x):
    return not isinf(x) and not isnan(x)

def isinf(x):
    return x == inf or x == -inf

def isnan(x):
    return x != x

def ulp(x):
    if x == 0:
        return 2 ** -1074
    exp_val = floor(log(abs(x), 2))
    return 2 ** (exp_val - 52)

# ===== Potencia, exponencial y logarítmico =====

def exp2(x):
    return float(2 ** x)

def cbrt(x):
    return x ** (1/3)

def expm1(x):
    return exp(x) - 1

def log2(x):
    xi = float(x)
    if xi > 0 and int(xi) == xi:
        v = int(xi)
        n = 0
        while v % 2 == 0 and v > 0:
            v //= 2
            n += 1
        if v == 1:
            return float(n)
    return log(x, 2)

def log10(x):
    xi = float(x)
    if xi > 0 and int(xi) == xi:
        v = int(xi)
        n = 0
        while v % 10 == 0 and v > 0:
            v //= 10
            n += 1
        if v == 1:
            return float(n)
    return log(x, 10)

# ===== Sumatorias y productos =====

def sum_range(a, b):
    return sum(range(int(a), int(b) + 1))

def prod_range(a, b):
    res = 1
    for i in range(int(a), int(b) + 1):
        res *= i
    return res

def dist(p, q):
    if len(p) != len(q):
        raise ValueError("dist() requires equal-length sequences")
    s = 0.0
    for a, b in zip(p, q):
        s += (a - b) ** 2
    return sqrt(s)

def fsum(iterable):
    total = 0.0
    c = 0.0
    for x in iterable:
        y = x - c
        t = total + y
        c = (t - total) - y
        total = t
    return total

def hypot(*coords):
    s = 0.0
    for x in coords:
        s += x * x
    return sqrt(s)

def prod(iterable, start=1):
    result = start
    for x in iterable:
        result *= x
    return result

def sumprod(p, q):
    if len(p) != len(q):
        raise ValueError("sumprod() requires equal-length sequences")
    total = 0
    for a, b in zip(p, q):
        total += a * b
    return total

# ===== Funciones especiales =====

def erf(x):
    from lib.KafeMATH.funciones import factorial, pow_
    coef = 2 / pow_(pi(), 0.5)
    term = x
    sum_ = term
    for n in range(1, 50):
        term *= -1 * x * x / n
        sum_ += term / (2 * n + 1)
    return coef * sum_

def erfc(x):
    return 1 - erf(x)

def gamma(x):
    xi = float(x)
    if xi == int(xi) and xi > 0:
        return factorial(int(xi) - 1)
    raise ValueError("gamma(x) only implemented for positive integers")

def lgamma(x):
    return log(gamma(x))
