# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр
# при просмотре справа налево упорядоченной по неубыванию.

num = int(input())
while num % 10 <= num // 10 % 10:
    num = num // 10
if num < 10:
    print("YES")
else:
    print("NO")
