digit = int(input())
if (1000 <= digit <= 9999) and (digit % 7 == 0 or digit % 17 == 0):
    print('YES')
else:
    print('NO')
