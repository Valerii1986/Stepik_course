# На вход программе подается одна строка. Напишите программу, которая выводит:
# общее количество символов в строке;
# исходную строку, повторенную 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удаленным первым и последним символами.

text = input()
counter = 0
for i in range(len(text)):
    counter += 1
print(counter, text * 3, text[0], text[:3], text[-3:], text[::-1], text[1:counter - 1], sep='\n')