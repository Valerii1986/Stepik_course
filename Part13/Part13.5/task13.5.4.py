# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является надёжным, или False в противном случае.
#
# Пароль является надёжным, если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.



def is_password_good(password):
    upper_case = False
    lower_case = False
    number = False
    if len(password)<8:
        return False
    for char in password:
        if char.isupper():
            upper_case = True
        if char.islower():
            lower_case = True
        if char.isdigit():
            number = True
    return upper_case and lower_case and number


print(is_password_good(input()))
