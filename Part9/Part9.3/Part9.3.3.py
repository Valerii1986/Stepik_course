# На вход программе подается строка текста. Напишите программу, которая определяет является ли
# оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» во всевозможных регистрах.

text = input()
if "good" in text.lower():
    print("YES")
else:
    print("NO")
