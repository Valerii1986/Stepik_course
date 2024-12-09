# На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем
# k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки,
# в которых встречаются одновременно все поисковые запросы.

lst = [input() for _ in range(int(input()))]
searches = [input() for _ in range(int(input()))]

for text in lst:
    if all(search.lower() in text.lower() for search in searches):
        print(text)
