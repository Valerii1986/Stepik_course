# На вход программе подаются два целых числа a и b (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от
# a до b (включительно), куб которых оканчивается на 4 или 9.

num_a = int(input())
num_b = int(input())
counter = 0
for i in range(num_a, num_b + 1):
    if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
        counter += 1
print(counter)