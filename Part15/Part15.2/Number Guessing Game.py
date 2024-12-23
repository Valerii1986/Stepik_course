import random


def is_valid(inputed_number):
    if inputed_number.isdigit():
        return True
    else:
        return False


def game():
    print("Welcome to the number guessing game")
    print("Input right border for number guessing game ")
    right_border = input()
    while True:
        if is_valid(right_border):
            break
        else:
            print("Input right border for number guessing game")
            right_border = input()

    right_border = int(right_border)
    random_number = random.randint(1, right_border)
    print(random_number)
    counter = 0

    while True:
        print("Please input number from 1 to", right_border)
        number = input()
        if not is_valid(number):
            print("Enter please correct data>number from 1 to", right_border)
            continue
        else:
            number = int(number)
        if number < random_number:
            print("Your number is less than the guessed number, try again")
            counter += 1
            continue
        elif number > random_number:
            print("Your number is greater than the guessed number, try again")
            counter += 1
            continue
        else:
            print("You guessed it, congratulations!")
            print("You try to guess", counter, "times")
            break


while True:
    game()
    print("Do you want play one more time? Write ---> Yes or No")
    answer = input()
    if answer.lower() == "yes":
        continue
    else:
        print('Thank you for playing the number guessing game. See you later...')
        break
