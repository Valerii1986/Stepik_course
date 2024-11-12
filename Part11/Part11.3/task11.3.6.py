# На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел. Напишите программу,
# которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).


number_n = int(input())
new_list = []

for counter in range(number_n):
    new_list.append(int(input()))
for counter in range(number_n - 1):
    new_list[counter] = new_list[counter] + new_list[counter + 1]

del new_list[-1]
print(new_list)
