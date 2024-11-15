# На вход программе подается натуральное число  n, а затем n целых чисел. Напишите программу, которая
# создает из указанных чисел список их кубов.

number_n = int(input())
new_list = []
for counter in range(number_n):
    digit = int(input())
    new_list.append(digit**3)
print(new_list)