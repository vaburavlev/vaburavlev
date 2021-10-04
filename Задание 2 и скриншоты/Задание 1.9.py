# -*- coding: utf-8 -*-
def N():
    print('Введите входные данные (3 числа)')
    n = int(input('Введите количество долек по шир:'))
    m = int(input('Введите количество долек по длине:'))
    k = int(input('Введите количество долек:'))
    if(n * m > k and (k % m == 0 or k % n == 0)):
        return "Да"
    else:
        return "Нет"
print(N())
