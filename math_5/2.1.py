# Сложение
def sum_prob(n, k):
    return len(n) / k


# Умножение
def mult_prob(n, k, m):
    return (n / k) ** m


print(round((sum_prob([1, 6], 6)), 3))
print(round((mult_prob(1, 10, 3)), 3))
