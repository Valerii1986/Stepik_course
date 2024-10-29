# На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.

text = input()
updated_text = ''
index_1 = text.find("h")
index_2 = text.rfind("h")
for i in range(len(text)):
    if i < index_1 or i > index_2:
        updated_text += text[i]
print(updated_text)
