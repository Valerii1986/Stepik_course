# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

num = float(input())
print(int(num * 10 % 10))