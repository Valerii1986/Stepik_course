# На вход программе подаётся натуральное число n. Напишите программу, которая для каждого из чисел от 0 до n
# n (включительно) выводит текст в следующем формате:
# Квадрат числа <текущее число> равен <квадрат текущего числа>

num = int(input())
for i in range(num+1):
    print('The square of', i, 'is equal to', i ** 2)
