import numpy as np

def normal_pdf(x, mu=0, sigma=1):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def trap_rule(n, a, b, f, mu, sigma):
    deltax = (b - a) / n
    area = ( f(a, mu, sigma) + f(b, mu, sigma) ) / 2

    for i in range(n):
        area += f(a + i * deltax , mu, sigma)

    area *= deltax
    return area

def trapezoidal_rule(f, a, b, n, mu=0, sigma=1):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x, mu, sigma)
    integral = (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    return integral

def find_quantile(f, P, a, b, tol, max_iter, mu=0, sigma=1):
    n = 1000
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        midpoint = (a + b) / 2
        integral = trapezoidal_rule(f, mu - 10 * sigma, midpoint, n, mu, sigma)
        if integral < P:
            a = midpoint
        else:
            b = midpoint
        iter_count += 1
    return (a + b) / 2


def evaluate_varfloat(min, max, msg, msg_warn):
    while True:
        val = float(input(msg))
        if val >= min and val <= max:
            return val
        else:
            print(msg_warn)


def evaluate_varint(min, msg, msg_warn):
    while True:
        val = int(input(msg))
        if val >= min:
            return val
        else:
            print(msg_warn)


def evaluate_varint2(min, max, msg, msg_warn):
    while True:
        val = int(input(msg))
        if val >= min and val<=max:
            return val
        else:
            print(msg_warn)
