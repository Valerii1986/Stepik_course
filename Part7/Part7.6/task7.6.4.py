# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
summ = 0
count = 0
multiplication = 1
mean = 0
first_plus_last_digit = 0
minimum = num % 10
last_digit = num % 10
while num > 0:
    summ = summ + num % 10
    count = count + 1
    mean = mean + num % 10
    multiplication = multiplication * (num % 10)
    first_digit = num % 10
    num = num // 10

print(summ)
print(count)
print(multiplication)
print(mean/count)
print(first_digit)
print(first_digit + last_digit)


