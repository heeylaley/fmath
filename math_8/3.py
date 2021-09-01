import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
             )
B = np.array([[12, 2, 1]])
C = np.concatenate((A, B.T), axis=1)

print(C)
print(np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001))
