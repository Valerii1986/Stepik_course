# Напишите программу, вычисляющую значение тригонометрического выражения sinx+cosx+tanx * txnx
from math import *

degree = float(input())
print(sin(radians(degree)) + cos(radians(degree)) + pow(tan(radians(degree)), 2))
