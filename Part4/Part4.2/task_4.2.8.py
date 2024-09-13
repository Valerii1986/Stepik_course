column_1 = int(input())
row_1 = int(input())
column_2 = int(input())
row_2 = int(input())
if (column_1 - 1 <= column_2 <= column_1 + 1) and (row_1 - 1 <= row_2 <= row_1 + 1):
    print('YES')
else:
    print('NO')
