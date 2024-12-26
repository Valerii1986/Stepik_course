# Напишите функцию is_prime(num),
# которая принимает в качестве аргумента натуральное число и возвращает значение True,
# если число является простым, или False в противном случае.
def is_prime(num):
    divine = 0
    for counter in range(1, num + 1):
        if num % counter == 0:
            divine += 1
    if divine == 2:
        return True
    else:
        return False


print(is_prime(int(input())))
