# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.

num = int(input())
count = 1
for i in range(1, num + 1):
    count = count * i
print(count)
