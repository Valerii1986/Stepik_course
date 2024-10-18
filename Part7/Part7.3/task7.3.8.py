# На вход программе подаётся натуральное число n. Напишите программу вычисления знакочередующейся суммы:
# 1−2+3−4+5−6+…+pow((−1)(n+1))⋅n

num_n = int(input())
summ = 0
for i in range(1, num_n + 1):
    summ = summ + pow(-1, i + 1) * i
print(summ)