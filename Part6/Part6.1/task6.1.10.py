# Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет,
# интересное число или нет. Если число интересное, следует вывести «Число интересное», иначе – «Число неинтересное».
num = int(input())
max_digit = max(num // 100, num // 10 % 10, num % 10)
min_digit = min(num // 100, num // 10 % 10, num % 10)
middle_digit = (num // 100 + num // 10 % 10 + num % 10) - max_digit - min_digit
print(num // 100, num // 10 % 10, num % 10)
if max_digit - min_digit == middle_digit:
    print('Interesting digit')
else:
    print('Not interesting digit')
