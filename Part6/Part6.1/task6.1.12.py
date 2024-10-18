# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути.
# Если только вы не умеете проходить сквозь стены, вам обязательно придется идти вдоль его параллельно-перпендикулярных улиц.
# На плоскости манхэттенское расстояние между двумя точками (p1;p2) и (q1;q2) определяется так: ∣p1−q1∣+∣p2−q2∣
# Напишите программу, определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

p_1 = int(input())
p_2 = int(input())
q_1 = int(input())
q_2 = int(input())

print(abs(p_1 - q_1) + abs(p_2 - q_2))