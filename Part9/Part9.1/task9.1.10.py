# На вход программе подаётся одна строка с буквами русского языка. Напишите программу, которая определяет
# количество гласных и согласных букв и выводит текст в следующем формате:
# Количество гласных букв равно <кол-во гласных букв>
# Количество согласных букв равно <кол-во согласных букв>

text = input()
counter_glasn = 0
counter_soglasn = 0
for i in range(len(text)):
        if text[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
            counter_glasn += 1
        elif text[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
            counter_soglasn += 1
print(counter_glasn)
print(counter_soglasn)
