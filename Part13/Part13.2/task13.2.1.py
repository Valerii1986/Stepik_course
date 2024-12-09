# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# - fill – символ заполнитель;
#  - base – величина основания равнобедренного треугольника;
# а затем выводит его.

def draw_triangle(fill, base):
    for _ in range(1, base + 1):
        print(fill * min(_, base - _ + 1))


fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
