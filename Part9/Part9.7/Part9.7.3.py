# На вход программе подается строка текста. Напишите программу, которая переводит каждый ее символ в
# соответствующий ему код из таблицы символов Unicode.

text = input()
for char in text:
    print(ord(char), end=" ")
print("\n")
text = input()
for char in text:
    print(ord(char), end=" ")
