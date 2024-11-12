# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

number_n = int(input())
new_list = []
for counter in range(number_n):
    new_list.append(input())
number_k = int(input())
for counter in range(number_n):
    if len(new_list[counter]) < number_k:
        continue
    else:
        print(new_list[number_k - 1], end='')
