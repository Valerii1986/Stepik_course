digit_a = int(input())
digit_b = int(input())
digit_c = int(input())

if digit_a < digit_b < digit_c or digit_c < digit_b < digit_a:
    print(digit_b)
elif digit_c < digit_a < digit_b or digit_b < digit_a < digit_c:
    print(digit_a)
else:
    print(digit_c)
