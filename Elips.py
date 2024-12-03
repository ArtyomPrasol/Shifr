import Rabin as r
import math

def sum_point(P, Q, a = 1):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:  
        return None  # бесконечно удалённая точка

    if x1 != x2:
        k = ((y2 - y1) * pow(x2 - x1, -1)) 
    else:  # x1 == x2 и y1 == y2
        if y1 == 0:  
            return None
        k = ((3 * x1**2 + a) * pow(2 * y1, -1)) 

    x3 = (k**2 - x1 - x2) 
    y3 = (k * (x1 - x3) - y1) 

    return x3, y3


def find_x_and_root(y, z, delta = 500000):
    # проверяем входные данные
    if z >= y or z < 0:
        raise ValueError("Остаток z должен быть больше или равен 0 и меньше y")
    
    # начинаем искать число с минимального подходящего квадрата
    n = 0
    for i in range(delta):
        x = n**2  # квадрат числа n
        if x % y == z:  # проверяем условие деления с остатком
            return x, n
        n += 1  # переходим к следующему квадрату
    return -1, -1


def rabin(p, k = 10):
    while True: # считаем пока не найдем простое число
        b = int(r.max_pow(p))
        m = int(r.get_m(p,b))

        for _ in range(k):
            a = int(r.take_a(p))
            z = pow(a, m, p)
            valid = r.rabin_test(p, z, b)
            if valid == 0:
                break
            if _ == k - 1: #прошли k проверок
                return p
        p += 1


def func_y(x,a = 1,b = 0):
    return x**3 + a*x + b


def elliptic_curve_order(p, a = 1, b = 0):
    order = 1  # начинаем с точки на бесконечности
    for x in range(p):
        rhs = (x**3 + a * x + b) % p
        count = 0
        # ищем квадратичные вычеты
        for y in range(p):
            if (y * y) % p == rhs:
                count += 1
        order += count
    return order


def hasse(c, porder):
    l = c + 1 - math.sqrt(c) #нижняя граница
    h = c + 1 + math.sqrt(c) #верхняя граница

    if l <= porder <= h: #проверка теоремы Хассе
        return True
    return False


def point_order(P):
    Q = P
    k = 1 # kP = P
    while Q is not None:
        Q = sum_point(Q, P)  # cложение точки с самой собой вместо умножения
        k += 1
        if Q is None: 
            return k
    return None  


if __name__ == "__main__":
    p = int(input("Введите число: "))
    if (p % 2 == 0): p += 1 #делаем число нечет
    p = rabin(p) #запускаем проверку Рабина-Миллера с циклом k = 10 и получаем простое число

    print("Подходящее значение p: ", p)
    x = 0
    while True:
        x += 1
        z = func_y(x)
        y2, y = find_x_and_root(p, z)
        if y2 == -1:
            continue
        else:
            break

    print("Значение функции и корень: ", y2, y)
    print("X: ", x, "Y: ", y)

    #151P считаем
    P = (x,y)
    P2 = sum_point(P,P)
    P4 = sum_point(P2, P2)
    P8 = sum_point(P4, P4)
    P16 = sum_point(P8, P8)
    P32 = sum_point(P16, P16)
    P64 = sum_point(P32, P32)
    P128 = sum_point(P64, P64)
    P151 = sum_point(sum_point(sum_point(sum_point(P2, P), P4), P16), P128)
    print("Точка 151P: ",P151[0], P151[1])

    porder = elliptic_curve_order(p)
    if hasse(p, porder):
        print("Порядок эллиптической кривой: ", porder)
    else:
        print(porder, " не является порядком эллиптической кривой!")

    print("Порядок точки P: ", point_order(P))