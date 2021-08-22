import numpy as np


def roulette():
    try:
        bet = int(input('Введите вашу ставку (от 0 до 36): '))
        if 36 < bet < 0:
            print('Введите число от 0 до 36')
            return roulette()
        res = int(np.random.uniform(0, 36))
        print(res)
        if res == bet:
            print('Ваша ставка победила!')
        else:
            print('Извините, попробуйте в следующий раз')
    except ValueError:
        print('Введите число от 0 до 36')
        return roulette()


roulette()
