# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.
row_1, row_2, row_3 = len(input()), len(input()), len(input())
if (row_1 + row_3) / 2 == row_2 or (row_1 + row_2) / 2 == row_3 or (row_2 + row_3) / 2 == row_1:
    print("YES")
else:
    print("NO")
