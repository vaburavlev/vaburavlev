# --coding: utf -8 --
def w():
    print("Введите входные данные (3 числа)")
    x = int(input())
    y = int(input())
    z = int(input())
    print("Ответ:")
    return min(x,y,z)
print(w())
