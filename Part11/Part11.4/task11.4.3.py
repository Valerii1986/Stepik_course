# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое
# значение. # На вход программе подается натуральное число n, а затем n различных натуральных чисел.
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

new_list = []
for _ in range(int(input())):
    new_list.append(int(input()))
del new_list[new_list.index(min(new_list))]
del new_list[new_list.index(max(new_list))]
print(*new_list, sep='\n')