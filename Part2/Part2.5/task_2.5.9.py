num = int(input())

fourth_digit = num % 10
third_digit = num // 10 % 10
second_digit = num // 100 % 10
first_digit = num // 1000
print("Цифра в позиции тысяч равна", first_digit)
print("Цифра в позиции сотен равна", second_digit)
print("Цифра в позиции десятков равна", third_digit)
print("Цифра в позиции единиц равна", fourth_digit)
