import itertools

# 5
# также учитываем, что не начинается с 0
res = 1 / (9 * 10 ** 6)
print(f'Вероятность номера 8882227 = {res}')

# 6
count = 0
for p in itertools.permutations("123456789", 2):
    print(''.join(str(x) for x in p))
    count = count + 1
print(f'всего вариантов {count}')
print(f'Вероятность угадать номер с первого раза = {round(1 / count, 3)}')
