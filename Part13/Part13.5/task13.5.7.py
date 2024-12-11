# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель
# BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_valid_password('1221:101:22'))
# print(is_valid_password('565:30:50'))
# print(is_valid_password('112:7:9'))
# print(is_valid_password('1221:101:22:22'))
# должен выводить:
#
# True
# False
# False
# False

def is_prime(num):
    divine = 0
    for counter in range(1, num + 1):
        if num % counter == 0:
            divine += 1
    if divine == 2:
        return True
    else:
        return False


def is_palindrome(text):
    return text == text[::-1]


def s_valid_password(password):
    new_list = password.split(":")
    return is_palindrome(new_list[0]) and is_prime(int(new_list[1])) and int(new_list[2]) % 2 == 0 and len(new_list) == 3


print(s_valid_password(input()))
