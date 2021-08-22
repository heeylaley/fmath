import numpy as np

# 2
A = np.matrix([[1, 2, 3],
              [4, 0, 6],
              [7, 8, 9]]
              )
det = np.linalg.det(A)
print(round(det, 3))

# 3.1
A_inv = np.linalg.inv(A)
print(A_inv)

# 4
A = np.array([1, 5])
B = np.array([2, 8])
print(np.dot(A, B))
