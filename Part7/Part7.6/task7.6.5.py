# Дано натуральное число n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

num = int(input())
while num > 0:
    if num // 10 == 0:
        print(digit)
    digit = num % 10
    num = num // 10
