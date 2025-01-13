# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение
# True если указанный текст является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
#
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы,
# а также символы , . ! ? -.
#
# Примечание 3. Следующий программный код:
#
# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))
# должен выводить:
#
# True
# True
# False

def is_palindrome(text):
    text1 = "".join(i.lower() for i in text if i.isalpha())
    return text1 == text1[::-1]


print(is_palindrome(input()))
