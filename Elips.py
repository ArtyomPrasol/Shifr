import Rabin as r


def sum_point(P, Q, a = 1):
    if P is None:  # Если P — бесконечно удалённая точка
        return Q
    if Q is None:  # Если Q — бесконечно удалённая точка
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:  # Сложение противоположных точек
        return None  # Бесконечно удалённая точка

    if x1 != x2:  # Сложение точек с разными абсциссами
        k = (y2 - y1) * pow(x2 - x1, -1)
    else:  # x1 == x2 и y1 == y2 — удвоение точки
        if y1 == 0:  # Если точка лежит на оси x, результат — бесконечно удалённая точка
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
    while True:
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
    print(P151[0], P151[1])
    
