# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.


num = int(input())
flag = True
s = ''
while flag:
    s = s + str(num % 10)
    num = num // 10
    if num == 0:
        flag = False
print(s)