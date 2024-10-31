# На вход программе подается одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек),
# если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).

text = input()
counter = 0
flag = False
for i in range(len(text)):
    if text[i] in '0123456789':
        print("Digital")
        flag = True
        break
if not flag:
    print("No digits")
