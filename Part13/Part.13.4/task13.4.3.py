# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую
# список всех делителей данного числа.
#
# Примечание. Следующий программный код:
#
# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))
# должен выводить:
#
# [1]
# [1, 5]
# [1, 2, 5, 10]

def get_factors(num):
    return [counter for counter in range(1, num//2 + 1) if num % counter == 0] + [num]


print(get_factors(int(input())))
