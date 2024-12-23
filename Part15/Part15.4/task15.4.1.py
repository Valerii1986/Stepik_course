import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exception = "il1Lo0O"
chars = ""

number_of_passwords = int(input("Введите количество паролей для генерации:"))
length = int(input("Введите длину одного пароля:"))

add_digit = input("Включать ли цифры 0123456789? да/нет: ").strip().lower()
add_lowercase_letters = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет: ").strip().lower()
add_uppercase_letters = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет: ").strip().lower()
add_punctuation = input("Включать ли символы !#$%&*+-=?@^_? да/нет: ").strip().lower()
remove_exception = input("Исключать ли неоднозначные символы il1Lo0O? да/нет: ").strip().lower()

if add_digit == "да":
    chars += digits
if add_lowercase_letters == "да":
    chars += lowercase_letters
if add_uppercase_letters == "да":
    chars += uppercase_letters
if add_punctuation == "да":
    chars += punctuation
if remove_exception == "да":
    for x in exception:
        chars = chars.replace(x, "")


def generate_password(length, chars):
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password


passwords = []
for _ in range(number_of_passwords):
    passwords.append(generate_password(length, chars))

print("Сгенерированные пароли:")
for password in passwords:
    print(password)
