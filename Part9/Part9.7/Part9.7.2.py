# На вход программе подаются два числа a и b. Напишите программу, которая для каждого кодового значения в диапазоне от
# a до b(включительно), выводит соответствующий ему символ из таблицы символов Unicode.

letter_a = int(input())
letter_b = int(input())
for i in range(letter_a, letter_b + 1):
    print(chr(i), end=' ')