# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

data = [input() for i in range(int(input()))]
number_n = int(input())
for i in data:
    if len(i) >= number_n:
        print(i[number_n - 1], end='')
