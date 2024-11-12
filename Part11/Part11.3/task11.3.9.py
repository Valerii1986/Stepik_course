# На вход программе подается натуральное число n, а затем  n строк. Напишите программу, которая создает
# список из символов всех строк, а затем выводит его.

number = int(input())
old_list = [input() for counter in range(number)]
new_list = []
for counter in range(number):
    new_list.extend(old_list[counter])
print(new_list)