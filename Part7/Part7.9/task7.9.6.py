# Дано натуральное число n. Напишите программу, которая выводит значение суммы:
# 1!+2!+3!+…+n!
num = int(input())
count = 1
summ = 0
for i in range(1, (num + 1)):
    count = i * count
    summ = summ + count

print(summ)
