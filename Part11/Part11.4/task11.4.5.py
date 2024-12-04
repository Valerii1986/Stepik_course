data = [input() for _ in range(int(input()))]
row = input()
for _ in range(len(data)):
    if row.lower() in data[_].lower():
        print(data[_])
