# Даны три вещественных числа a, b, c Напишите программу, которая находит вещественные корни квадратного уравнения:
#  возвращает его корни в порядке возрастания. Гарантируется, что квадратное уравнение имеет хотя бы один корень.
# . Если уравнение имеет только один корень, нужно вернуть два числа, равных этому корню.

import math


def solve(num_a, num_b, num_c):
    discriminant = num_b ** 2 - 4 * num_a * num_c
    if discriminant > 0:
        x_1 = (-num_b - math.sqrt(discriminant)) / (2 * num_a)
        x_2 = (-num_b + math.sqrt(discriminant)) / (2 * num_a)
        return sorted([x_1, x_2])
    elif discriminant == 0:
        return -num_b / (2 * num_a),  -num_b / (2 * num_a)


print(*solve(float(input()), float(input()), float(input())))
