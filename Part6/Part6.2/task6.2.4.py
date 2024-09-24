# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city_1 = input()
city_2 = input()
city_3 = input()
minimum = min(len(city_1), len(city_2), len(city_3))
maximum = max(len(city_1), len(city_2), len(city_3))

if minimum == len(city_1):
    print(city_1)
elif minimum == len(city_2):
    print(city_2)
else:
    print(city_3)
if maximum == len(city_1):
    print(city_1)
elif maximum == len(city_2):
    print(city_2)
else:
    print(city_3)
