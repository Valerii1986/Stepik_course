# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит только
# уникальные строки, в том же порядке, в котором они были введены.

data = []
for counter in range(int(input())):
    row = input()
    if row not in data:
        data.append(row)
print(*data, sep='\n')
