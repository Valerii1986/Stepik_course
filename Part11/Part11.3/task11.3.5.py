# На вход программе подается натуральное число n. Напишите программу, которая создает список,
# состоящий из делителей введенного числа.

number_n = int(input())
new_list = []
for counter in range(1, number_n + 1):
    if number_n % counter == 0:
        new_list.append(counter)
print(new_list)
