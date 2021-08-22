import numpy as np
import matplotlib.pyplot as plt

x = []
num_sum = []
for i in range(0, 10):
    num_sum.append(0)
    x.append(np.random.rand(32))
print(x)
num_sum = x[0] + x[1] + x[2] + x[3] + x[4] + x[5] + x[6] + x[7] + x[8] + x[9]
print(num_sum)

num_bins = 7
n, bins, patches = plt.hist(num_sum, num_bins)
plt.xlabel('сумма')
plt.ylabel('вероятность')
plt.title('Гистограмма распределения')
plt.show()
