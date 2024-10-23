# На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
text = input()
counter = 0
for i in range(len(text)):
    counter += int(text[i])
print(counter)
