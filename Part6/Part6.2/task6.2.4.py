# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
city_1 = input()
city_2 = input()
city_3 = input()

print(min(city_1, city_2, city_3, key=len ))
print(max(city_1, city_2, city_3, key=len ))
