# Даны два натуральных числа m и n (m≤n). Напишите программу, которая выводит все целые числа от m до n (включительно),
# удовлетворяющие хотя бы одному из условий:
# число кратно 17
# число оканчивается на 9
# число кратно 3 и 5 одновременно

num_m = int(input())
num_n = int(input())

for i in range(num_m, num_n + 1):
    if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
        print(i)