# На вход программе подается одна строка. Напишите программу, которая выводит элементы строки с
# индексами 0, 2, 4, ... в столбик.

text = input()
for i in range(0, len(text), 2):
    print(text[i])
