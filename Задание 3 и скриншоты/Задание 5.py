# -- coding: utf-8 --
n = int(input('Ввести натуральное число:'))
sum = 0
for i in range(1, n + 1):
    sum += i*i*i**3
print(sum)