# Дано натуральное число n(n≤9).Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n
# (включительно) в соответствии с примером.

num = int(input())
for i in range(1, num + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print('')
