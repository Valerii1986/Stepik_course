# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого
# введенного числа x выводит значение функции f(x)=x2+2x+1, каждое на отдельной строке.

entered_list = []
resolved_list = []
for _ in range(int(input())):
    digit_x = int(input())
    entered_list.append(digit_x)
    resolved_list.append(digit_x ** 2 + 2 * digit_x + 1)
print(*entered_list, '', *resolved_list, sep='\n')



