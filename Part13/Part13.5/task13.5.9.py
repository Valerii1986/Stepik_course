# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».
#
# Примечание 1. Почитать подробнее о стилях именования можно по ссылке.
#
# Примечание 2. Приведённый ниже код:
#
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
#
# this_is_camel_cased
# is_prime_number

def convert_to_python_case(text):
    new_list = []
    for char in text:
        new_list.append(char)
    new_list[0] = new_list[0].lower()
    for char in new_list:
        if char.isupper():
            new_list[new_list.index(char)] = '_' + new_list[new_list.index(char)].lower()

    return new_list


print(*convert_to_python_case(input()), sep='')
