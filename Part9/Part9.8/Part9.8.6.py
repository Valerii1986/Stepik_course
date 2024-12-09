# Все книги в домашней библиотеке Душнилы, друга Сэма, должны быть обязательно отсортированы по возрастанию:
# сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям. Напишите программу, которая проверяет,
# верно ли отсортированы книги. На вход вашей программе поступает число n, а затем – n строк, каждая строка
# представляет собой книгу в следующем формате:
# <фамилия автора> <инициалы автора>, «<название книги>»
# Программа должна вывести «YES» (без кавычек), если книги отсортированы в соответствии с пожеланиями Душнилы,
# или «NO» (без кавычек) в противном случае.

previous_book = ''
is_ordered = 'YES'

for counter in range(int(input())):
    new_book = input()
    current_surname = new_book[: new_book.find(' ')]
    current_title = new_book[new_book.find('«') + 1: new_book.rfind('»')]
    current_book = current_surname + current_title

    if current_book < previous_book:
        is_ordered = 'NO'
    previous_book = current_book

print(is_ordered)





