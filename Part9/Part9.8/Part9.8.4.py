# На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно,
# не учитывая регистр и игнорируя все небуквенные символы.
# Программа должна вывести «YES», если строки окажутся равны в результате такой проверки, или «NO» в противном случае.

row_1 = [counter_1.lower() for counter_1 in input() if counter_1.isalpha()]
row_2 = [counter_2.lower() for counter_2 in input() if counter_2.isalpha()]

print("YES" if row_1 == row_2 else "NO")


