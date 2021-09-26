# --coding: utf -8 --
n = int(input('Ведите первое число'))
m = int(input('Ведите второе число'))
k = int(input('Ведите третье число'))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('ДА')
else:
    print('НЕТ')