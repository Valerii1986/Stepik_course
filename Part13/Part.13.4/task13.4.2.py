# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и возвращает количество дней в данном месяце.
#
# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12.
#
# Примечание 2. Считайте, что год является невисокосным.
#
# Примечание 3. Следующий программный код:
#
# print(get_days(1))
# print(get_days(2))
# print(get_days(9))
# должен выводить:
#
# 31
# 28
# 30





def get_days(month):
    year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return year[month-1]


print(get_days(int(input())))
