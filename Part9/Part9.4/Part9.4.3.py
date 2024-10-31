number_times = int(input())
counter = 0
for i in range(number_times):
    text = input()
    if text.count("11") >= 3:
        counter += 1
print(counter)
