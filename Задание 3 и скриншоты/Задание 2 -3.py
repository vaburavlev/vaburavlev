# -- coding: utf-8 --
A = int(input('Введите целое число А:'))
B = int(input('Введите целое число B:'))
if A<B:
 for C in range(A, B + 1):
    print(C)
elif A>B:
  for C in range(A, B - 1, -1):
    print(C)