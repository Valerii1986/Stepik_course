# На вход программе подается строка текста. Напишите программу, которая проверяет,
# что строка заканчивается подстрокой .com или .ru.

text = input()

if text.endswith(".ru") or text.endswith(".com"):
    print("YES")
else:
    print("NO")
