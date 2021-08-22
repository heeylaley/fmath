import numpy as np

A = np.matrix([[1, 2, 3, 4, 5],
              [5, 4, 3, 2, 1],
              [10, 10, 10, 13, 11],
              [1, 44, 31, 41, 51],
              [13, 1, 133, 1, 31]]
              )

A = 5 * A
A_inv = np.linalg.inv(A)
print(A_inv)
