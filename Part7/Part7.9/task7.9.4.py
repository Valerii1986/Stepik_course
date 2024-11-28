# На вход программе подается натуральное число n. Напишите программу,
# выводящую графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

num_a = int(input())
num_b = int(input())
summ = 0
max_summ = 0
number = 0
for i in range(num_a, num_b + 1):
    summ = 0
    for j in range(1, i + 1):
        if i % j == 0:
            summ = summ + j
    if summ >= max_summ:
        max_summ = summ
        number = i
print(number, max_summ)