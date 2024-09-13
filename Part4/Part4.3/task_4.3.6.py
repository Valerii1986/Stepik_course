first_digit, second_digit, character = int(input()), int(input()), input()

if character == '+':
    print(first_digit + second_digit)
elif character == '-':
    print(first_digit - second_digit)
elif character == '/' and second_digit != 0:
    print(first_digit / second_digit)
elif character == '*':
    print(first_digit * second_digit)
elif character == '/' and second_digit == 0:
    print("You can't divide by zero!")
else:
    print('Invalid operation')
