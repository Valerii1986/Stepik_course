# Напишите программу, которая считывает последовательность из 10 целых чисел и
# определяет, является ли каждое из них чётным или нет.
flag = True
for i in range(1, 11):
    num = int(input())
    if num % 2 != 0:
        flag = False
if not flag:
    print('NO')
else:
    print('YES')
