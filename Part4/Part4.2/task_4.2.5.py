side_a = int(input())
side_b = int(input())
side_c = int(input())

if (side_a > 0 and side_b > 0 and side_c > 0) and (side_a + side_b > side_c) and (side_a + side_c > side_b) and (
        side_b + side_c > side_a):
    print('YES')
else:
    print('NO')
