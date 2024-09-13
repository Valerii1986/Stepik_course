number = int(input())

if 1 <= number <= 10 and number % 2 == 0:
    print('black')
elif 11 <= number <= 18 and number % 2 == 0:
    print('red')
elif 19 <= number <= 28 and number % 2 == 0:
    print('black')
elif 29 <= number <= 36 and number % 2 == 0:
    print('red')
elif 1 <= number <= 10 and number % 2 != 0:
    print('red')
elif 11 <= number <= 18 and number % 2 != 0:
    print('black')
elif 19 <= number <= 28 and number % 2 != 0:
    print('red')
elif 29 <= number <= 36 and number % 2 != 0:
    print('black')
elif number == 0:
    print('green')
else:
    print('input error')
