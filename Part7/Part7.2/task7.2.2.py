# Даны два целых числа m и n Напишите программу, которая выводит все целые числа от m до n включительно в порядке
# возрастания, если m<n, или в порядке убывания в противном случае.

num_m = int(input())
num_n = int(input())

if num_m < num_n:
    for i in range(num_m, num_n + 1):
        print(i)
else:
    for i in range(num_m, num_n - 1, -1):
        print(i)
