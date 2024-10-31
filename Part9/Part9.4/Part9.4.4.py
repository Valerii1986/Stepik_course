# На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
text = input()
counter = 0
for char in text:
    if char.isdigit():
        counter += 1
print(counter)