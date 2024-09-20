# Напишите программу, которая упорядочивает три числа от большего к меньшему.
num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

max_digit = max(num_1, num_2, num_3)
min_digit = min(num_1, num_2, num_3)
middle_digit = num_1 + num_2 + num_3 - min_digit - max_digit
print(max_digit, middle_digit, min_digit)
