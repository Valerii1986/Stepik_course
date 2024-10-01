# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# (1+1/2+1/3+....+1/n) - ln(n)
import math

num_n = int(input())
summ = 0
for i in range(1, num_n + 1):
    summ = summ + 1 / i
print(summ - math.log(num_n))
