# На вход программе подаётся строка текста, содержащая целые числа. Напишите программу,
# использующую списочное выражение, которая выведет квадраты чётных чисел, кроме тех квадратов,
# которые оканчиваются на цифру 4.

print(*[int(number) ** 2 for number in input().split() if int(number) % 2 == 0 and (int(number) ** 2) % 10 != 4 and (int(number) ** 2) // 10 != 0])
