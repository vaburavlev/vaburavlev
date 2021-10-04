# -*- coding: utf-8 -*-
def S():
    print('Введите входные данные (1 число)')
    year = int(input('Год  - '))
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return "Да"
    else:
        return "Нет"
print(S())
