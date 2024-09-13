side_a, side_b, side_c = int(input()), int(input()), int(input())
if side_a == side_b == side_c:
    print('Equilateral')
elif side_a == side_b or side_b == side_c or side_c == side_a:
    print('Isosceles')
else:
    print('Scalar')
