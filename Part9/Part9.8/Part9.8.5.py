# На вход программе подаются 3 различных слова. Вам необходимо отсортировать эти слова по возрастанию
# в лексикографическом порядке и вывести их на одной строке, разделяя символом пробела.

word_1 = input()
word_2 = input()
word_3 = input()

print(min(word_1, word_2, word_3), end=' ')
print(min(max(word_1, word_2), max(word_1, word_3), max(word_2, word_3)), end=' ')
print(max(word_1, word_2, word_3), end=' ')
