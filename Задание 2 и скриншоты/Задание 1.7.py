# --coding: utf -8 --
year = int(input('Введите год'))
if (year % 4 == 0):
	print("Высокосный")
elif (year%100 != 0):
	print("Высокосный")
elif (year%400 == 0): 
    print("Высокосный")
else:
    print("Обычный")
