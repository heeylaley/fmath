import numpy as np

A = np.array([1, 5, 0])
B = np.array([2, 8, 7])
C = np.array([7, 1.5, 3])
D = np.array([A, B, C])
m1 = np.cross(A, B)

print(f'Векторное произведение A и B = {m1}')
print(f'Векторное произведение A и B, умноженное скалярно на C = {np.dot(m1, C)}')
