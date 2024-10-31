# На вход программе подается одна строка. Напишите программу, которая определяет,
# сколько раз в строке встречаются символы + и *.

text = input()
counter_plus = 0
counter_asterisks = 0
for i in range(len(text)):
    if text[i] in '+':
        counter_plus += 1
    elif text[i] in '*':
        counter_asterisks += 1
print('Symbol + is displayed', counter_plus, 'times')
print('Symbol * is displayed', counter_asterisks, 'times')
