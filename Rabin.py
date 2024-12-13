import random

def max_pow(p):
    i = 0
    while (p - 1) % (2 ** i) == 0:
        i += 1
    return i - 1

def get_m(p,b): return float(p-1)/float(2 ** b)
def take_a(p): return random.randrange(2, int(p*0.5)-1)


def rabin_test(p, z, b, j = 0): #тест Миллера-Рабина
    if z == 1 or z == p - 1:
        return True
    while j != b:
        if j > 0 and z == 1: 
            return False
        j += 1
        if j < b and z != p - 1:
            z = pow(z,2,p)
            if z == p - 1:
                return True
    return False


def gen_pdb(n): #генерируем двухзначный код
    p = ""
    for _ in range(n):
        if _ == 0 or _ == n - 1:
            p += "1"
        else: 
            if random.randrange(0, 2) == 0:
                p += "0"
            else:
                p += "1"
    return p


def is_prime(num):
  #простое число
  if num <= 1:
    return False
  for i in range(2, int(num*0.5) + 1):
    if num % i == 0:
      return False
  return True


def gen_p(n, primes = [i for i in range(2, 12) if is_prime(i)], f = 0): #генерируем число (ищем первые простые числа перед этим)
    while f != 1:
        f = 1
        pt = gen_pdb(n)
        p = int(pt, 2) #сюда пишем двухзначный код, первое и последнее значения = 1
        for num in primes:
            if p < num:
                break
            if p % int(num) == 0:
                f = 0
                break
    return p


if __name__ == "__main__":
    # генерируем n битное число
    n = 12
    p = gen_p(n)

    b = int(max_pow(p))
    m = int(get_m(p,b))
    k = 5
    for _ in range(k):
        a = int(take_a(p))
        z = pow(a, m, p)
        valid = rabin_test(p, z, b)
        with open("exit.txt", "a", encoding="utf-8") as f:
            f.write(f"Число: {p} ; значение a: {a}\n")
            f.write(f"Тест {_+1}: {valid}\n")
            if _ == k - 1 and valid == 1:
                f.write(f"Число является простым!")

        if valid == 0:
            break


