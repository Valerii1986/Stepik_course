# На вход программе подается два вещественных числа a и b
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import *

num_a = float(input())
num_b = float(input())

print((num_a + num_b) / 2)
print(sqrt(num_a * num_b))
print((2 * num_a * num_b) / (num_a + num_b))
print(sqrt((pow(num_a, 2) + pow(num_b, 2))/2))
