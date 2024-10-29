# На вход программе подаётся строка текста. Напишите программу,
# которая выводит на экран символ, который появляется наиболее часто.
text = input()
most_common = text[0]
for char in text:
    if text.count(char) >= text.count(most_common):
        most_common = char
print(most_common)






