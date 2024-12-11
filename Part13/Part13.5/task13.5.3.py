# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и
# возвращает первое простое число, большее числа num.

def is_prime(num):
    divine = 0
    for counter in range(1, num + 1):
        if num % counter == 0:
            divine += 1
    if divine == 2:
        return True
    else:
        return False


def get_next_prime(num):
    while not is_prime(num + 1):
        num += 1
        continue
    return num + 1


print(get_next_prime(int(input())))
