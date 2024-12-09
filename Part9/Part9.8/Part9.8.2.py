# В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму: берет самую "маленькую"
# и самую "большую" строки, перемножает Unicode-коды последних символов этих строк и возводит полученное число в
# квадрат. Результатом и является "волшебное" число.
# На вход программе подаются 4 слова. Найдите "волшебное" число в этом наборе слов.

word_1 = input()
word_2 = input()
word_3 = input()
word_4 = input()
maximum = max(word_1, word_2, word_3, word_4)
minimum = min(word_1, word_2, word_3, word_4)
uni_min = ord(minimum[len(minimum) - 1])
uni_max = ord(maximum[len(maximum) - 1])
print((uni_max * uni_min) ** 2)
