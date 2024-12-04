# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем
# k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки,
# в которых встречаются одновременно все поисковые запросы.

data = [input() for _ in range(int(input()))]
search_list = [input() for _ in range(int(input()))]
for counter_1 in range(len(data)):
    summ = 0
    for counter_2 in range(len(search_list)):
        if search_list[counter_2].lower() in data[counter_1].lower():
            summ += 1
        if summ == len(search_list):
            print(data[counter_1])
