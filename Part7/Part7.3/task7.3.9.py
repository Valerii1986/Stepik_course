# На вход программе подается натуральное число n, а затем n различных натуральных чисел последовательности,
# каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

max_num_1 = 0
max_num_2 = 1

num_n = int(input())
for i in range(1, num_n+1):
    num = int(input())
    if num > max_num_1:
        max_num_2 = max_num_1
        max_num_1 = num
    elif num > max_num_2:
        max_num_2 = num

print(max_num_1, max_num_2, sep='\n')
