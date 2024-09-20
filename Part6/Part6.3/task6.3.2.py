# Напишите программу, определяющую площадь круга и длину окружности по заданному радиусу R
import math

radius = float(input())

print(math.pi * pow(radius, 2))
print(2 * math.pi * radius)
