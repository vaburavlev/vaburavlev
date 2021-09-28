# --coding: utf -8 --
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))
d = int(input('Введите четвертое число'))
x = a % 2
y = b % 2
z = c % 2
f = d % 2
if x==1 and y==1 and z==1 and f==1:
    print('ДА')
elif x==1 and y==1 and z==0 and f==0:
    print('ДА')
elif x==0 and y==0 and z==1 and f==1:
    print('ДА')
elif x==1 and y==0 and z==1 and f==0:
    print('ДА')
elif x==0 and y==1 and z==0 and f==1:
    print('ДА')
elif x==1 and y==1 and z==0 and f==1:
    print('НЕТ')
elif x==1 and y==1 and z==1 and f==0:
    print('НЕТ')
elif x==0 and y==0 and z==1 and f==0:
    print('НЕТ')
elif x==0 and y==0 and z==0 and f==1:
    print('НЕТ')
elif x==1 and y==0 and z==1 and f==1:
    print('НЕТ')
elif x==1 and y==0 and z==0 and f==1:
    print('НЕТ')
elif x==0 and y==1 and z==0 and f==0:
    print('НЕТ')
elif x==1 and y==0 and z==0 and f==1:
    print('ДА')
else: 
    print('ДА')