# На вход программе подаются три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов с 1-го по
# n-й день (включительно). Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.

start_num = int(input())
increase_percent = int(input())
num_days = int(input())
population = start_num
for i in range(num_days):
    print(i + 1, population)
    population = population * increase_percent / 100 + population
