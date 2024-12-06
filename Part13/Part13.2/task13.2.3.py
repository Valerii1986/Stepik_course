# Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.
def print_digit_sum(num):
    print(sum(int(i) for i in num))


print_digit_sum(input())
