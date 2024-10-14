# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.
row_1 = input()
row_2 = input()
row_3 = input()
minimum = min(len(row_1), len(row_2), len(row_3))
maximum = max(len(row_1), len(row_2), len(row_3))
middle = (len(row_1) + len(row_2) + len(row_3) - maximum - minimum)

if (maximum - middle) == (middle - minimum):
    print("YES")
else:
    print("NO")


