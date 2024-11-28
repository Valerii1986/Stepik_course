# На вход программе подается строка текста, содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.

new_list = [int(i) for i in input().split()]
index_min = new_list.index(min(new_list))
index_max = new_list.index(max(new_list))
new_list[index_min], new_list[index_max] = max(new_list), min(new_list)
print(*new_list)
