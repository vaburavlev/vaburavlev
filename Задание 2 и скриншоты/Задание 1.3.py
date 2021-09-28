# --coding: utf -8 --
n = int(input())
hourse = n % (60*24) // 60
minutes = n % 60
print(hourse,'Часа:',minutes,'Минут:')