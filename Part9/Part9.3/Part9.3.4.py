# На вход программе подается строка. Напишите программу, которая подсчитывает количество
# буквенных символов в нижнем регистре.

text = input()
counter = 0
for char in text:
    if char.islower():
        counter += 1
print(counter)
