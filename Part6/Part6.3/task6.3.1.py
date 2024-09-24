# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
import math

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
print(distance)

