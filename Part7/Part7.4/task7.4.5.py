# На вход программе подается последовательность целых чисел,
# каждое число на отдельной строке. Признаком окончания последовательности является любое отрицательное число,
# при этом в саму последовательность оно не входит. Напишите программу,
# которая выводит сумму всех членов данной последовательности.

num = int(input())
count = 0
while num >= 0:
    count += num
    num = int(input())
print(count)
