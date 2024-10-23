# Дано натуральное число (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры и
# выводит текст в следующем формате:
# Максимальная цифра равна <максимальная цифра>
# Минимальная цифра равна <минимальная цифра>

num = int(input())
maximum = 0
minimum = num % 10
while num > 0:
    if (num % 10) > maximum:
        maximum = num % 10
    if (num % 10) < minimum:
        minimum = num % 10
    num = num // 10
print('Maximum digit is', maximum)
print('Minimum digit is', minimum)

