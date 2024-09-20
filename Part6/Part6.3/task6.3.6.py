# Даны три вещественных числа a, b, c Напишите программу, которая находит вещественные корни квадратного уравнения:

from math import *

num_a = float(input())
num_b = float(input())
num_c = float(input())

discriminant = num_b ** 2 - 4 * num_a * num_c
if discriminant > 0:
    x_1 = (-num_b - sqrt(discriminant)) / (2 * num_a)
    x_2 = (-num_b + sqrt(discriminant)) / (2 * num_a)
    if x_1 < x_2:
        print(x_1)
        print(x_2)
    else:
        print(x_2)
        print(x_1)
elif discriminant == 0:
    print(-num_b / (2 * num_a))
else:
    print('no roots')
