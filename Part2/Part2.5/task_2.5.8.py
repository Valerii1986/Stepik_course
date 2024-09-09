num = int(input())

third_digit = num % 10
second_digit = (num // 10) % 10
first_digit = num // 100
print(first_digit, second_digit, third_digit, sep="")
print(first_digit, third_digit, second_digit, sep="")
print(second_digit, first_digit, third_digit, sep="")
print(second_digit, third_digit, first_digit, sep="")
print(third_digit, first_digit, second_digit, sep="")
print(third_digit, second_digit, first_digit, sep="")
