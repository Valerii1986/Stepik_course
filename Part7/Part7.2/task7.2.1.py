# Даны два целых числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n включительно.

num_m = int(input())
num_n = int(input())

for i in range(num_m, num_n + 1):
    print(i)
