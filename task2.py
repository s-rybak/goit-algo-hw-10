import random
import scipy.integrate as spi

a = 0
b = 2


def f(x):
    """f(x) = x^2"""
    return x**2


def monte_carlo_method(f, a, b):
    max_y = f(b)
    points = [(random.uniform(a, b), random.uniform(0, max_y)) for _ in range(150000)]
    inside_points = [point for point in points if 0 <= point[1] <= f(point[0])]
    N = len(points)
    M = len(inside_points)
    rect_area = (b - a) * max_y
    return (M / N) * rect_area


result, error = spi.quad(f, a, b)

monte_carlo_results = [monte_carlo_method(f, a, b) for _ in range(10)]
delta = [abs(result - monte_carlo_result) for monte_carlo_result in monte_carlo_results]
average_delta = sum(delta) / len(delta)

print("Інтеграл spi: ", result, error)
print("Площа за методом Монте-Карло: ", monte_carlo_results)
print("Різниця: ", delta)
print("Середня різниця: ", average_delta)
