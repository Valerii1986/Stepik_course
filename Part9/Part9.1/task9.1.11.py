# На вход программе подается натуральное число, записанное в десятичной системе счисления.
# Напишите программу, которая переводит данное число в двоичную систему счисления.
num = int(input())
binarn = ''
while num > 0:
    binarn = str(num % 2) + binarn
    num = num // 2
print(binarn)
