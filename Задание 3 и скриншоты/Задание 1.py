# -- coding: utf-8 --
A = int(input('Введите натуральное число А:'))
B = int(input('Введите натуральное число B:'))
print('Порядок натуральных чисел от A до B:')
if A<=B:
  for C in range(A, B + 1):
    print(C)
