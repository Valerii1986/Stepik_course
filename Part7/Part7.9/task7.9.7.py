# На вход программе подается два натуральных числа a и b (a< b). Напишите программу, которая находит все
# простые числа от a до b включительно

num_a, num_b = int(input()), int(input())
for i in range(num_a, num_b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
