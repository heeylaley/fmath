import numpy as np
import scipy.linalg

A = np.array([[1, 2, 3],
              [2, 16, 21],
              [4, 28, 73]]
             )
P, L, U = scipy.linalg.lu(A)

print(f'P: {P}')
print(f'L: {L}')
print(f'U: {U}')

print(np.dot(P, A) - np.dot(L, U))

print(f'A = L * U: {np.dot(L, U)}')

B = np.array([12, 2, 1])
print(np.linalg.solve(A, B))
