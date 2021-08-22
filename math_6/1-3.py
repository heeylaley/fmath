import itertools


# 1
def sum_prob(n, k):
    return len(n) / k


print('1.')
print(round((sum_prob([2, 5], 6)), 3))


# 2
def mult_prob(n, k, m):
    return (n / k) ** m


print('2.')
print(round((mult_prob(1, 6, 2)), 3))


# 3
def combi_prob(n, k, m):
    # n = благоприятные исходы
    # k = вариантов от одной игральной кости
    # m = сколько бросаем костей
    return n / k ** m


count = 0
for p in itertools.product("25", repeat=2):
    print(''.join(p))
    count = count + 1
print(f'всего = {count}')

print('3.')
print(round(combi_prob(count, 6, 2), 3))
