# Напишите программу, выводящую следующий список:
# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]

# Примечание. Последний элемент списка должен состоять из  26 символов z.
new_list = []
for counter in range(0, 26):
    new_list.append(chr(ord('a') + counter) * (counter + 1))
print(new_list)
