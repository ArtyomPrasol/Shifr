import Rabin as rab
import random


# def find_primitive_root(p):
#     if p == 2:
#         return 1
#     phi = p - 1
#     for g in range(int(p/10), p):
#         if is_primitive_root(g, p, phi):
#             return g
#     return None


# def is_primitive_root(g, p, phi):
#     for i in range(1, phi):
#         if pow(g, i, p) == 1:
#             return False
#     return True


def find_primitive_root(p):
  """Находит примитивный корень простого числа p."""

  if p == 2:
    return 1  # специальный случай для p = 2

  phi = p - 1
  factors = []
  # находим все простые делители phi (p - 1)
  n = 2
  while n * n <= phi:
    if phi % n == 0:
      factors.append(n)
      while phi % n == 0:
        phi //= n
    n += 1
  if phi > 1:
    factors.append(phi)
  # проверяем числа от некоторого до p-1
  for g in range(int(p/10), p-1):
    is_primitive_root = True
    for factor in factors:
      if pow(g, phi // factor, p) == 1:
        is_primitive_root = False
        break
    if is_primitive_root:
      return g
  return None  # если не найден примитивный корень, возвращаем None


def daffi(p):
    with open("exit_daffi.txt", "a", encoding="utf-8") as f:
        g = find_primitive_root(p)
        f.write(f"Примитивный элемент: {g}\n")

        a = random.randint(1, p-1)
        A = pow(g, a, p)

        b = random.randint(1, p-1)
        B = pow(g, b, p)

        K_A = pow(B, a, p) 
        K_B = pow(A, b, p)

        f.write(f"Публиный ключ A: {A}; Публиный ключ B: {B}\n")
        f.write(f"Секретный ключ A: {K_A}; Секретный ключ B: {K_B}\n")
        if K_A != K_B:
            f.write(f"Секретные ключи не совпадают!\n")
        else: 
            f.write(f"Общий секретный ключ успешно вычислен и совпадает.\n")    


if __name__ == "__main__":
    n = 20
    k = 5

    valid = 0
    while valid != 1:
        p = rab.gen_p(n)
        b = int(rab.max_pow(p))
        m = int(rab.get_m(p,b))
        for _ in range(k):
            a = int(rab.take_a(p))
            z = pow(a, m, p)
            valid = rab.rabin_test(p, z, b)
            with open("exit_daffi.txt", "a", encoding="utf-8") as f:
                f.write(f"Число: {p} ; значение a: {a}\n")
                f.write(f"Тест {_+1}: {valid}\n")
                if _ == k - 1 and valid == 1:
                    f.write(f"Число является простым!\n")

            if valid == 0:
                break

    daffi(p)