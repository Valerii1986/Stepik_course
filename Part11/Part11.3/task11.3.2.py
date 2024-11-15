# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает
# из указанных строк список и выводит его.

row_number = int(input())
final_list = []
for counter in range(row_number):
    row = input()
    final_list.append(row)
print(final_list)
