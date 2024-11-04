# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова.
# Напишите программу, которая принимает 4 слова и находит среди них самое тяжелое слово.
# Если самых тяжелых слов будет несколько, то программа должна вывести первое из них.

word_1 = input()
word_2 = input()
word_3 = input()
word_4 = input()
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
for char in word_1:
    counter_1 += ord(char)
for char in word_2:
    counter_2 += ord(char)
for char in word_3:
    counter_3 += ord(char)
for char in word_4:
    counter_4 += ord(char)
if max(counter_1, counter_2, counter_3, counter_4) == counter_1:
    print(word_1)
elif max(counter_1, counter_2, counter_3, counter_4) == counter_2:
    print(word_2)
elif max(counter_1, counter_2, counter_3, counter_4) == counter_3:
    print(word_3)
elif max(counter_1, counter_2, counter_3, counter_4) == counter_4:
    print(word_4)


