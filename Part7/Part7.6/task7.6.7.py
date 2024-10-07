# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр
# при просмотре справа налево упорядоченной по неубыванию.

num = int(input())
flag = True
while num > 0:
    last_digit = num % 10
    num = num // 10
    if last_digit > num % 10 and num > 0:
        flag = False
if flag:
    print("YES")
else:
    print("NO")
