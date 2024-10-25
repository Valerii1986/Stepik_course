# На вход программе подается одно слово, записанное в нижнем регистре.
# Напишите программу, которая определяет, является ли оно палиндромом.
counter = -1
word = input()
flag = True
for i in range(len(word) - 1):
    if word[i] != word[counter]:
        flag = False
        break
    counter += -1
if flag:
    print("YES")
else:
    print("NO")
