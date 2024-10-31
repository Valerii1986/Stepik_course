# На вход программе подается строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин),
# Т (тимин). # Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит
# в данную строку генетического кода.

text = input()
counter_a = 0
counter_g = 0
counter_c = 0
counter_t = 0

text_low = text.lower()
for char in text_low:
    if char == 'a':
        counter_a += 1
    elif char == 'g':
        counter_g += 1
    elif char == 'c':
        counter_c += 1
    elif char == 't':
        counter_t += 1
print("Adenin:", counter_a)
print("Guanin:", counter_g)
print("Citozin:", counter_c)
print("Timin:", counter_t)
