# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает два
# значения: длину окружности и площадь круга, ограниченного данной окружностью.

import math


def get_circle(radius):
    return 2 * math.pi * radius, math.pi * radius ** 2


print(*get_circle(float(input())))
