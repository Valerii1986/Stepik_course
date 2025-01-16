# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
# а также на то, какие символы требуется в него включить, а какие исключить.

# Программа должна запрашивать у пользователя следующую информацию:
#
# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?


import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
EXCEPTION = "il1Lo0O"
CHARS = ""

number_of_passwords = int(input("Введите количество паролей для генерации:"))
length = int(input("Введите длину одного пароля:"))

add_digit = input("Включать ли цифры 0123456789? да/нет: ").strip().lower()
add_lowercase_letters = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? да/нет: ").strip().lower()
add_uppercase_letters = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? да/нет: ").strip().lower()
add_punctuation = input("Включать ли символы !#$%&*+-=?@^_? да/нет: ").strip().lower()
remove_exception = input("Исключать ли неоднозначные символы il1Lo0O? да/нет: ").strip().lower()

if add_digit == "да":
    CHARS += DIGITS
if add_lowercase_letters == "да":
    CHARS += LOWERCASE_LETTERS
if add_uppercase_letters == "да":
    CHARS += UPPERCASE_LETTERS
if add_punctuation == "да":
    CHARS += PUNCTUATION
if remove_exception == "да":
    for x in EXCEPTION:
        CHARS = CHARS.replace(x, "")


def generate_password(length, CHARS):
    password = ""
    for i in range(length):
        password += random.choice(CHARS)
    return password


passwords = []
for _ in range(number_of_passwords):
    passwords.append(generate_password(length, CHARS))

print("Сгенерированные пароли:")
for password in passwords:
    print(password)
