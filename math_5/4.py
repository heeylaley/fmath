import itertools

print('1. Вариации 0123')
count = 0
for p in itertools.product("0123", repeat=4):
    print(''.join(p))
    count = count + 1
print(f'всего = {count}')

print('2. Перестановка 0123')
count = 0
for p in itertools.permutations("0123", 4):
    print(''.join(str(x) for x in p))
    count = count + 1
print(f'всего = {count}')

print('3. Комбинации 0123 в 3 символах')
count = 0
for p in itertools.combinations("0123", 3):
    print(''.join(str(x) for x in p))
    count = count + 1
print(f'всего = {count}')
