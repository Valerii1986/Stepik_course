# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.

num_n = int(input())
num_a = 1
num_c = 0
for i in range(1, num_n + 1):
    num_b = num_a
    num_a = num_b + num_c
    num_c = num_b
    print(num_b, end=' ')
