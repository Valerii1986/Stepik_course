# На вход программе подается строка текста. Напишите программу, использующую списочное выражение,
# которая выводит все цифровые символы данной строки.

print(*[char for char in input() if char.isdigit()], sep='')
