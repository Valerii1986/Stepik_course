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


text = input()
new_text = text
for j in text:
    if j in '*,.!@"-=)?':
        new_text = new_text.replace(j, '')

list_len = [len(i) for i in new_text.split()]

count = 0
word_new = ''

for char in text:
    number = ord(char)

    if char == ' ':
        count += 1
        word_new += chr(number)
    elif 65 <= number <= 90:
        number += list_len[count]
        if number > 90:
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    elif 97 <= number <= 122:
        number += list_len[count]
        if number > 122:
            number = number - 26
            word_new += chr(number)
        else:
            word_new += chr(number)
    else:
        word_new += chr(number)

print(word_new)
