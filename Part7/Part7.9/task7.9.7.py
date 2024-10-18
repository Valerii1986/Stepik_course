# На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит все
# простые числа от a до b включительно.

num_a = int(input())
num_b = int(input())
counter = 0
for i in range(num_a, num_b + 1):
    for j in range(2, i):
        counter = 0
        if i % j == 0:
            counter = 1
            break
    if counter == 0 and i != 1:
        print(i)
