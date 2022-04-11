import math


def calculate_h(a: float, b: float) -> float:
    return ((a - b) ** 2) / ((a + b) ** 2)


def eccentricity(a: float, b: float) -> float:
    return math.sqrt(a * a - b * b) / a


# def minor_axis_for_eccentricity(e: float) -> float:
#     return 1 - e ** 2


def approximate_perimeter(a: float, b: float) -> float:
    return 2 * math.pi * math.sqrt(((a ** 2) + (b ** 2)) / 2)


def approximate_perimeter_ramanujan(a: float, b: float) -> float:
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))


def approximate_perimeter_ramanujan_2(a: float, b: float) -> float:
    h = calculate_h(a, b)
    return math.pi * (a + b) * (1 + 3 * h / (10 + math.sqrt(4 - 3 * h)))


# def series_term(i: int, e: float) -> float:
#     v1 = math.factorial(2 * i) ** 2
#     v2 = (2 ** i * math.factorial(i)) ** 4
#     v3 = e ** (2 * i)
#     v4 = 2 * i - 1
#     return v1 / v2 * v3 / v4
#
#
# def series(a: float, b: float) -> Callable[[int], float]:
#     e = eccentricity(a, b)
#     return lambda i: series_term(i, e)
#
#
# def perimeter_by_series(a: float, b: float, terms: int):
#     return 2 * a * math.pi * (1 - math.fsum(map(series(a, b), range(1, terms + 1))))

# def binomial_coefficient(n: float, r: float) -> float:
#     return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
#
#
# def half_binomial_coefficient(r: float) -> float:
#     n_factorial = 0.5 * math.sqrt(math.pi)
#     return n_factorial / (math.factorial(r) * math.factorial(0.5 - 4))


# def series(a: float, b: float) -> Callable[[int], float]:
#     h = calculate_h(a, b)
#     return lambda n: half_binomial_coefficient(n) * h ** n


half_binomial_coefficients = [
    1,
    1/2,
    -1/8,
    1/16,
    -5/128,
    7/256,
    -21/1024,
    33/2048,
    -429/32768,
    715/65536,
    -2431/262144,
    4199/524288,
    -29392/4194304,
]


def perimeter_by_series(a: float, b: float, terms_count: int = len(half_binomial_coefficients)) -> float:
    h = calculate_h(a, b)
    terms = [
        half_binomial_coefficients[n] ** 2 * h ** n
        for n in range(0, min(terms_count, len(half_binomial_coefficients)))
    ]
    return math.pi * (a + b) * math.fsum(terms)
