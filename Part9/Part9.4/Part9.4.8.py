# На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.

text = input()
print(text[:text.find("h")] + text[text.rfind("h") + 1:])


