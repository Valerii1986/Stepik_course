# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

num = int(input())
flag = True
while flag:
    print(num % 10)
    num = num // 10
    if num == 0:
        flag = False
