# На вход программе подается строка текста, содержащая слова. Напишите программу,
# которая выводит слова введенной строки в столбик.

print(*[_ for _ in input().split()], sep='\n')