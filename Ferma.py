import math
import itertools


def correct_root(x): #правильный корень
    s = int(math.sqrt(x))
    if pow(s,2) == x:
        return True
    return False


def ferma_func(n): #функция Ферма
    qn = abs(math.isqrt(n))
    x = None
    y = None
    k = None
    find = []

    for i in itertools.count():
        k = i + 1
        nn = pow(qn + k, 2) - n
        if correct_root(nn):
            x = qn + k
            y = int(math.isqrt(nn))
            break
    
    find.append(x - y)
    find.append(x + y)
    return find


if __name__ == "__main__":

    n = 964758387457354683609980045464712160753368874876361319018239
    a = ferma_func(n)

    print(f"Делители для {n} :\n{a[0]} ;\n{a[1]}\n")