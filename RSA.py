from math import sqrt
import random
from random import randint as rand


alphabet_dict = {
    'А': 1,
    'Б': 2,
    'В': 3,
    'Г': 4,
    'Д': 5,
    'Е': 6,
    'Ё': 7,
    'Ж': 8,
    'З': 9,
    'И': 10,
    'Й': 11,
    'К': 12,
    'Л': 13,
    'М': 14,
    'Н': 15,
    'О': 16,
    'П': 17,
    'Р': 18,
    'С': 19,
    'Т': 20,
    'У': 21,
    'Ф': 22,
    'Х': 23,
    'Ц': 24,
    'Ч': 25,
    'Ш': 26,
    'Щ': 27,
    'Ъ': 28,
    'Ы': 29,
    'Ь': 30,
    'Э': 31,
    'Ю': 32,
    'Я': 33
}


def RSAmain(prev, step, main):
    ak = prev
    p = 1
    l = step
    while l > 0: 
        # print(ak, l, p, l%2)
        s = l % 2
        if s == 1:
            p = (p * ak) % main
        ak = (ak * ak) % main
        l = (l-s)/2
    # print(ak, l, p, l%2)
    # print('\n')
    return p


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    d = random.randrange(1, phi)
    g = gcd(d, phi)

    while True:
        d = random.randrange(1, phi)
        g = gcd(d, phi)
        e = mod_inverse(d, phi)
        if g == 1 and e != d:
            break

    return e,d,n

def hash(nums, h0, n):
    h = []
    f = RSAmain((h0 + nums[0]), 2, n)
    h.append(f)
    for i in range(1, len(nums)):
        f = RSAmain((f + nums[i]), 2, n)
        h.append(f)
    return h


def sig(M, e, d , n):
    return RSAmain(RSAmain(M, d, n), e, n)


def verify(H, r):
    return H == r


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def file_print(e,d,n, enc_mes, exit_mes, val, hash_n, sig):
    with open ("RSAhash.txt", "w", encoding="utf-8") as file:
        file.write(f"Закрытый ключ: {e}, {n}; Открытый ключ: {d}, {n}\n")
        file.write(f"Зашифрованное сообщение: {enc_mes}; расшифрованное сообщение: {exit_mes}\n")
        file.write(f"Хэш: {hash_n} ; Подпись: {sig}\n")
        file.write(f"Подпись подлинная: {val}\n")

# if __name__ == "__main__":
#     f = 0
#     p = 0
#     q = 0
#     num = 3

#     while f != 1:
#         print("Введите пару простых чисел: ")
#         p = int(input()) 
#         q = int(input())

#         if isprime(p) and isprime(q) and p != q:
#             f = 1

#     e,d,n = generate_keypair(p,q)
#     print("\nЗакрытый ключ: ",e,", ",n,"; ", "Открытый ключ: ", d,", ",n)

#     mes = []
#     for let in range(0, num):
#         print("Введите букву: ")
#         mes.append(input())

#     enc = []
#     print("\nВывод: ")
#     for let in range(0, num):
#         enc.append(RSAmain(alphabet_dict[mes[let]], e, n))
#         print(" " + str(enc[let]) + " ")

#     dec = []
#     print("\nВозврат обратно: ")
#     for let in range(0, num):
#         dec.append(RSAmain(enc[let], d, n))
#         print(" " + get_key(alphabet_dict,dec[let]) + " ")
    

if __name__ == "__main__":
    f = 0
    p = 0
    q = 0
    h0 = 49
    num = 3

    while f != 1:
        print("Введите пару простых чисел: ")
        p = int(input()) 
        q = int(input())

        if isprime(p) and isprime(q) and p != q:
            f = 1

    e,d,n = generate_keypair(p,q)
    print("\nЗакрытый ключ: ",e,", ",n,"; ", "Открытый ключ: ", d,", ",n)

    mes = []
    mes_num = []
    for let in range(0, num):
        print("Введите букву: ")
        mes.append(input())
        mes_num.append(alphabet_dict[mes[let]])

    enc = []
    print("\nВывод: ")
    for let in range(0, num):
        enc.append(RSAmain(mes_num[let], e, n))
        print(" " + str(enc[let]) + " ")

    hash_n = hash(mes_num, h0, n)

    sig_n = sig(hash_n[len(hash_n) - 1], e, d, n)
    val = verify(sig_n, hash_n[len(hash_n) - 1])

    dec = []
    print("\nВозврат обратно: ")
    for let in range(0, num):
        dec.append(RSAmain(enc[let], d, n))
        print(" " + get_key(alphabet_dict,dec[let]) + " ")
    
    file_print(e,d,n,enc,dec,val,hash_n,sig_n)