a_1, b_1, a_2, b_2 = int(input()), int(input()), int(input()), int(input()),

if b_1 < a_2 or b_2 < a_1:
    print('empty set')
elif b_1 == a_2:
    print(b_1)
elif b_2 == a_1:
    print(a_1)
elif a_1 <= a_2 < b_1 < b_2:
    print(a_2, b_1)
elif a_2 <= a_1 < b_2 < b_1:
    print(a_1, b_2)
elif a_1 < a_2 < b_2 <= b_1:
    print(a_2, b_2)
elif a_2 < a_1 < b_1 <= b_2:
    print(a_1, b_1)
elif a_1 == a_2 and b_1 == b_2:
    print(a_1, b_1)
