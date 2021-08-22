import numpy as np
import math


def monte_karlo(k, n):
    a = np.random.randint(0, 2, n)
    b = np.random.randint(0, 2, n)
    c = np.random.randint(0, 2, n)
    d = np.random.randint(0, 2, n)
    x = a + b + c + d

    for i in range(0, n):
        if x[i] == 2:
            k = k + 1

    return round(k / n, 3)


def ber_func(n, k):
    p = math.factorial(n) / (math.factorial(k) * math.factorial(n-k)) * 0.5 ** n
    return p


# 3.1
print(f'Вероятность по Монте-Карло = {monte_karlo(2, 5000)}')
print(f'Вероятность по Бернулли = {ber_func(10, 2)}')

# 3.2
print(f'Вероятность по Бернулли = {ber_func(10, 3)}')
