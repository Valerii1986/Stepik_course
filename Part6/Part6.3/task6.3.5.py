# Напишите программу, которая принимает на вход действительное число xx и вычисляет по нему значение:
# ⌊x⌋+⌈x⌉

from math import *

num = float(input())
print(floor(num) + ceil(num))
