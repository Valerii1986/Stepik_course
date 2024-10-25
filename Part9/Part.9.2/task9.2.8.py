# На вход программе подается строка текста. Напишите программу, которая разрежет ее на две равные части,
# переставит их местами и выведет на экран.

text = input()
first_part = text[0:len(text) - len(text) // 2]
second_part = text[len(text) - len(text) // 2: len(text)]

print(second_part, first_part, sep='')
