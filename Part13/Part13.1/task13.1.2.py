# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными 10 в
# соответствии с образцом:
#
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********

def draw_triangle():
    for _ in range(1, 11):
        print(_ * "*")


print(draw_triangle())
