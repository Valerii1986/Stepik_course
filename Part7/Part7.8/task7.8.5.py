# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...

num = int(input())
for i in range(1, (num + 1)):
    print(str(i) * i)
