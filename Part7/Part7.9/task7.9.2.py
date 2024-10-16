# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной n,
# в соответствии с примером:
# 1
# 121
# 12321
# 1234321
# 123454321

num = int(input())
count = 1
for i in range(1, (num + 1)):
    for j in range(1, count+1):
        if j <= i:
            print(j, end='')
            counter_negative = j
        else:
            counter_negative -= 1
            print(counter_negative, end='')
    print('')
    count = count + 2
