first_color = input()
second_color = input()
if (first_color == 'red' and second_color == 'blue') or (first_color == 'blue' and second_color == 'red'):
    print('purple')
elif (first_color == 'red' and second_color == 'yellow') or (first_color == 'yellow' and second_color == 'red'):
    print('orange')
elif (first_color == 'blue' and second_color == 'yellow') or (first_color == 'yellow' and second_color == 'blue'):
    print('green')
elif first_color == 'red' and second_color == 'red':
    print('red')
elif first_color == 'blue' and second_color == 'blue':
    print('blue')
elif first_color == 'yellow' and second_color == 'yellow':
    print('yellow')
else:
    print('Color Error')
