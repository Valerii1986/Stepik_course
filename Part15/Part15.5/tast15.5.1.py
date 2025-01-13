# На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.
#
# Формат входных данных
# На вход программе подаётся строка текста на английском языке.
#
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
#
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.


alphabet = 'abcdefghijklmnopqrstuvwxyz'

text_old = input()
words = text_old.split()
text_new = ""
for word in words:
    shift = sum([int(letter.lower() in alphabet) for letter in word])

    for letter in word:
        if letter in alphabet:
            old_letter_position = alphabet.index(letter)
            letter = alphabet[(old_letter_position + shift) % 26]

        elif letter.lower() in alphabet:
            old_letter_position = alphabet.index(letter.lower())
            letter = alphabet[(old_letter_position + shift) % 26].upper()

        text_new += letter

    text_new += " "

print(text_new)

