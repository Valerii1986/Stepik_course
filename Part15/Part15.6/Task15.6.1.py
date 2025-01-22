# На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит
# его в двоичную, восьмеричную и шестнадцатеричную системы счисления.
#
# Формат входных данных
# На вход программе подается натуральное число.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
#
# Примечание 1. Используйте встроенные функции bin(), oct(), hex().
#
# Примечание 2. Для шестнадцатеричной системы счисления используйте заглавные буквы A, B, C, D, E, F.
#
# Примечание 3. BOH = Binary, Octal, Hex.

def convert_to_binary_octal_hex(n):
    binary = bin(n)[2:]
    octal = oct(n)[2:]
    hexadecimal = hex(n)[2:].upper()
    return binary, octal, hexadecimal


decimal_number = int(input())

binary, octal, hexadecimal = convert_to_binary_octal_hex(decimal_number)

print(binary)
print(octal)
print(hexadecimal)
