num = int(input())
fourth = num % 10
third = num // 10 % 10
second = num//100 % 10
first = num // 1000
# print (first,second, third, fourth, sep='')
if first + fourth == second - third:
    print('YES')
else:
    print('NO')
