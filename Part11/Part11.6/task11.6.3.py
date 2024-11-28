# На вход программе подается строка, содержащая английский текст.
# Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.


new_list = input().lower().split()
counter = new_list.count("a") + new_list.count("an") + new_list.count("the")
print("Number", counter)
