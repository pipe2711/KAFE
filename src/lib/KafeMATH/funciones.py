from .errores import raiseDomainError, raiseNonEqualLength
from TypeUtils import vector_numeros_t, numeros_t, entero_t
from global_utils import check_sig


pi = 3.141592653589793
e = 2.718281828459045


tau = 2 * pi
inf = float('inf')
nan = float('nan')


@check_sig([1], numeros_t)
def exp(x):
    term = 1.0
    sum_ = 1.0
    for n in range(1, 50):
        term *= x / n
        sum_ += term
    return sum_

@check_sig([1, 2], numeros_t, numeros_t)
def log(*args):
    x = args[0]

    base = None
    if len(args) == 2:
        base = args[1]

    if base is None and x == e:
        return 1.0
    if x <= 0:
        raiseDomainError('log')
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


@check_sig([2], numeros_t, numeros_t)
def pow_(x, y):
    if x < 0:
        if float(y).is_integer():
            n = int(y)
            abs_x = -x
            result = exp(y * log(abs_x))
            return -result if (n % 2 != 0) else result
        else:
            raiseDomainError('pow')
    return exp(y * log(x))


@check_sig([1], numeros_t)
def sqrt(x):
    if x < 0:
        raiseDomainError('sqrt')
    guess = x if x != 0 else 1.0
    for _ in range(30):
        guess = (guess + x / guess) / 2
    return guess


@check_sig([1], numeros_t)
def degrees(x):
    return x * 180.0 / pi

@check_sig([1], numeros_t)
def radians(x):
    return x * pi / 180.0


@check_sig([1], numeros_t)
def sin(x):
    x = x % (2 * pi)
    term = x
    sum_ = term
    sign = -1
    for n in range(3, 50, 2):
        term *= x * x / ((n - 1) * n)
        sum_ += sign * term
        sign *= -1
    return sum_

@check_sig([1], numeros_t)
def cos(x):
    x = x % (2 * pi)
    term = 1.0
    sum_ = term
    sign = -1
    for n in range(2, 50, 2):
        term *= x * x / ((n - 1) * n)
        sum_ += sign * term
        sign *= -1
    return sum_

@check_sig([1], numeros_t)
def tan(x):
    c = cos(x)
    if c == 0:
        raiseDomainError('tan')
    return sin(x) / c


@check_sig([1], numeros_t)
def asin(x):
    if x == 1:
        return pi / 2
    if x == -1:
        return -pi / 2
    if x < -1 or x > 1:
        raiseDomainError('asin')
    term = x
    sum_ = term
    for n in range(1, 200):
        term *= (2 * n - 1)**2 * x * x / (2 * n * (2 * n + 1))
        sum_ += term
    return sum_

@check_sig([1], numeros_t)
def acos(x):
    if x == 1:
        return 0.0
    if x == -1:
        return pi
    return pi / 2 - asin(x)

@check_sig([1], numeros_t)
def atan(x):
    if x == 0:
        return 0.0
    if abs(x) > 1:
        return pi / 2 * (1 if x > 0 else -1) - atan(1 / x)
    term = x
    sum_ = term
    sign = -1
    for n in range(3, 1000, 2):
        term *= x * x
        sum_ += sign * term / n
        sign *= -1
    return sum_


@check_sig([1], numeros_t)
def sinh(x):
    return (exp(x) - exp(-x)) / 2

@check_sig([1], numeros_t)
def cosh(x):
    return (exp(x) + exp(-x)) / 2

@check_sig([1], numeros_t)
def tanh(x):
    ex = exp(x)
    enx = exp(-x)
    return (ex - enx) / (ex + enx)


@check_sig([1], [entero_t])
def factorial(n):
    n = int(n)
    if n < 0:
        raise ValueError("factorial: Function not defined for negative values")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@check_sig([2], [entero_t], [entero_t])
def comb(n, k):
    n, k = int(n), int(k)
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

@check_sig([2], [entero_t], [entero_t])
def perm(n, k):
    n, k = int(n), int(k)
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(n - k + 1, n + 1):
        result *= i
    return result

@check_sig([i for i in range(100)], *[[entero_t] for _ in range(100)])
def gcd(*ints):
    result = abs(int(ints[0]))
    for x in ints[1:]:
        a, b = result, int(x)
        while b:
            a, b = b, a % b
        result = abs(a)
    return result

@check_sig([i for i in range(100)], *[[entero_t] for _ in range(100)])
def lcm(*ints):
    def _lcm(a, b):
        return abs(a * b) // gcd(a, b)
    result = int(ints[0])
    for x in ints[1:]:
        result = _lcm(result, int(x))
    return result



@check_sig([1], numeros_t)
def trunc(x):
    return int(x)

@check_sig([2], numeros_t, numeros_t)
def fmod(x, y):
    if y == 0:
        raiseDomainError('fmod')
    return x - y * trunc(x / y)

@check_sig([2], numeros_t, numeros_t)
def remainder(x, y):
    if y == 0:
        raiseDomainError('remainder')
    res = x - y * round(x / y)
    return round(res, 10)

@check_sig([1], numeros_t)
def math_abs(x):
    return x if x >= 0 else -x

@check_sig([1], numeros_t)
def floor(x):
    i = int(x)
    return i if x >= i else i - 1

@check_sig([1], numeros_t)
def ceil(x):
    i = int(x)
    return i if x <= i else i + 1

@check_sig([1, 2], numeros_t, [entero_t])
def math_round(*args):
    x = args[0]

    n = 0
    if len(args) == 2:
        n = args[1]

    factor = 10 ** n
    t = x * factor
    f = floor(t)
    if t - f >= 0.5:
        f += 1
    return f / factor

@check_sig([2], numeros_t, numeros_t)
def copysign(x, y):
    x, y = float(x), float(y)
    if y == 0.0 and y.hex().startswith('-'):
        return -abs(x)
    return abs(x) if y >= 0 else -abs(x)

@check_sig([2, 3, 4], *[numeros_t for _ in range(4)])
def isclose(*args):
    a = args[0]
    b = args[1]

    if len(args) >= 3:
        rel_tol = args[2]
    else:
        rel_tol = 1e-9

    if len(args) == 4:
        abs_tol = args[3]
    else:
        abs_tol = 0.0

    if a == b:
        return True
    diff = abs(a - b)
    tol  = max(rel_tol * max(abs(a), abs(b)), abs_tol)
    return diff <= tol

@check_sig([1], numeros_t)
def isinf(x):
    return x == inf or x == -inf

@check_sig([1], numeros_t)
def isnan(x):
    return x != x

@check_sig([1], numeros_t)
def isfinite(x):
    return not isinf(x) and not isnan(x)

@check_sig([1], numeros_t)
def ulp(x):
    if x == 0:
        return 2 ** -1074
    exp_val = floor(log(abs(x), 2))
    return 2 ** (exp_val - 52)


@check_sig([1], numeros_t)
def exp2(x):
    return float(2 ** x)

@check_sig([1], numeros_t)
def cbrt(x):
    return x ** (1/3)

@check_sig([1], numeros_t)
def expm1(x):
    return exp(x) - 1

@check_sig([1], numeros_t)
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

@check_sig([1], numeros_t)
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



@check_sig([1, 2], [entero_t] + vector_numeros_t, [entero_t])
def sum_range(*args):
    a = args[0]

    if len(args) == 2:
        b = args[1]
    else:
        b = None

    if b is None:
        total = 0
        for x in a:
            total += x
        return total
    total = 0
    for i in range(int(a), int(b) + 1):
        total += i
    return total

@check_sig([1, 2], [entero_t] + vector_numeros_t, [entero_t])
def prod_range(*args):
    a = args[0]

    if len(args) == 2:
        b = args[1]
    else:
        b = None

    if b is None:
        result = 1
        for x in a:
            result *= x
        return result
    result = 1
    for i in range(int(a), int(b) + 1):
        result *= i
    return result

@check_sig([2], vector_numeros_t, vector_numeros_t)
def dist(p, q):
    if len(p) != len(q):
        raiseNonEqualLength('dist')
    s = 0.0
    for a, b in zip(p, q):
        s += (a - b) ** 2
    return sqrt(s)

@check_sig([1], vector_numeros_t)
def fsum(iterable):
    total = 0.0
    c = 0.0
    for x in iterable:
        y = x - c
        t = total + y
        c = (t - total) - y
        total = t
    return total

@check_sig([i for i in range(100)], *[numeros_t for _ in range(100)])
def hypot(*coords):
    s = 0.0
    for x in coords:
        s += x * x
    return sqrt(s)

@check_sig([1, 2], vector_numeros_t, entero_t)
def prod(*args):
    iterable = args[0]

    if len(args) == 2:
        start = args[1]
    else:
        start = 1

    result = start
    for x in iterable:
        result *= x
    return result

@check_sig([2], vector_numeros_t, vector_numeros_t)
def sumprod(p, q):
    if len(p) != len(q):
        raiseNonEqualLength('sumprod')
    total = 0
    for a, b in zip(p, q):
        total += a * b
    return total



@check_sig([1], numeros_t)
def erf(x):
    coef = 2 / pow_(pi, 0.5)
    term = x
    sum_ = term
    for n in range(1, 50):
        term *= -1 * x * x / n
        sum_ += term / (2 * n + 1)
    return coef * sum_

@check_sig([1], numeros_t)
def erfc(x):
    return 1 - erf(x)

@check_sig([1], numeros_t)
def gamma(x):
    xi = float(x)
    if xi == int(xi) and xi > 0:
        return factorial(int(xi) - 1)
    raise ValueError("gamma(x) only implemented for positive integers")

@check_sig([1], numeros_t)
def lgamma(x):
    return log(gamma(x))


pow   = pow_
abs   = math_abs
round = math_round
sum   = sum_range
prod  = prod_range
