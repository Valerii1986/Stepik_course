# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.

count = 1
for i in range(1, 11):
    num = int(input())
    if num != 0:
        count = count * num
print(count)
