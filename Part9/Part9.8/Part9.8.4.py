# На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно,
# не учитывая регистр и игнорируя все небуквенные символы.
# Программа должна вывести «YES», если строки окажутся равны в результате такой проверки, или «NO» в противном случае.

text_1 = input()
text_2 = input()
alpha_row_1 = ''
alpha_row_2 = ''
text_1 = text_1.lower()
text_2 = text_2.lower()
for counter_1 in range(len(text_1)):
    if text_1[counter_1].isalpha():
        alpha_row_1 += text_1[counter_1]
for counter_2 in range(len(text_2)):
    if text_2[counter_2].isalpha():
        alpha_row_2 += text_2[counter_2]

if alpha_row_1 == alpha_row_2:
    print("YES")
else:
    print("NO")
