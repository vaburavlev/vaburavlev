# -- coding: utf-8 --
N = int(input('Количество чисел из ряда Фибоначчи:'))
sum = 0
(a, b) = (0, 1)
while a <= N:
    (a, b) = (b, a + b)
    if a <= N:
        sum += a
print(sum)