import math

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def gauss_method(matrix, results):
    n = len(matrix)

    # Прямой ход (приведение к треугольному виду)
    for i in range(n):
        # Поиск ведущего элемента
        max_row = i + max(range(n - i), key=lambda k: abs(matrix[i + k][i]))
        if i != max_row:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            results[i], results[max_row] = results[max_row], results[i]

        # Нормализация текущей строки
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Система не имеет единственного решения.")

        for j in range(i, n):
            matrix[i][j] /= pivot
        results[i] /= pivot

        # Обнуление нижних элементов столбца
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            results[k] -= factor * results[i]

    # Обратный ход (поиск решений)
    solutions = [0] * n
    for i in range(n - 1, -1, -1):
        solutions[i] = results[i] - sum(matrix[i][j] * solutions[j] for j in range(i + 1, n))

    return solutions


def bas_opt(b, p, a, g): #поиск пересекающихся итераций с помощью сетов
    i = 1
    u = {}
    v = {}
    while True:
        u_val = pow(b, i, p)
        v_val = (a * pow(g, i, p)) % p

        if v_val in u:
            return u[v_val], i
        if u_val in v:
            return i, v[u_val]

        u[u_val] = i
        v[v_val] = i

        i += 1


def big_and_small_step(g, a, p): #Шаг младенца - шаг великана
    m = k = int(math.sqrt(p)) + 1 
    b = pow(g, k, p)
    
    i, j = bas_opt(b,p,a,g)
    x = pow(m * i - j, 1, p)
    return x
    
##Все для исчисления порядка
def find_base(k, g, p, t, a = 1):
    num = pow(a * pow(g, k), 1, p)
    line = []
    primes_t = PRIMES[:t]
    for prime in primes_t:
        count = 0
        while num % prime == 0:
            num //= prime
            count += 1
        line.append(count)
    if num == 1:
        return line
    return None


def extended_gcd(a, b): #расширенный алгоритм Евклида для нод
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
    return gcd, x, y


def obr(a, b): #обратный элемент по модулю
    g = extended_gcd(a, b)
    if g[0] == 1:
        return g[1] % b
    else:
        return 0
    

def gauss_method(matrix, p):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        max_row = i
        for k in range(i + 1, n): #поиск макс элемент
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        if matrix[i][i] == 0: #матрица не подходит
            return None

        pivot_inverse = obr(matrix[i][i], p - 1) #
        if pivot_inverse == 0:
            return None

        for k in range(i, m):
            matrix[i][k] = (matrix[i][k] * pivot_inverse)

        for j in range(i + 1, n):
            factor = matrix[j][i]
            for k in range(i, m):
                matrix[j][k] = (matrix[j][k] - factor * matrix[i][k])

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][m - 1]
        for j in range(i + 1, n):
            x[i] = (x[i] - matrix[i][j] * x[j]) % (p - 1)
    return x


def count_order(g, a, p, t = 4, c = 10): #Метод исчисления порядка
    matrix = []
    b = []

    k = 0
    while len(matrix) < t + c: #ищем все уравнения
        line = find_base(k, g, p, t)
        if line != None:
            matrix.append(line)
            b.append(k)
        k += 1

    print("Матрица : \n", matrix, '\nРешение : \n', b, '\n')
    ml = []
    for j in range(t): #находим подходящие уравнения, чтоб можно было найти все лог
        for i in range(len(matrix)):
            if matrix[i][j] != 0 and i not in ml:
                ml.append(i)
                break

    matrix_find = []
    for i in range(len(ml)): #собираем уравнения нужные
        matrix_find.append(matrix[ml[i]])
        matrix_find[i] = matrix_find[i] + [b[ml[i]]]
    save = matrix_find[0]
    matrix_find[0] = matrix_find[2]
    matrix_find[2] = save #меняем порядок для наших значений 7 и 263
    

    print("Матрица  :\n", matrix_find, "\n")
    res = gauss_method(matrix_find, p) #решаем методом Гаусса составленную систему
    print("Ответ полученный методом Гаусса: \n", res, '\n')

    for i in range(len(res)): res[i] = pow(res[i], 1, p-1)

    answer = None
    k = 0
    while answer == None:
        answer = find_base(k, g, p, t, a) #ищем первую подходящую базу
        k += 1
    print("База найдена : \n", answer, '\n')
    
    final = 0
    for i in range(t):
        final += answer[i] * res[i]
    final -= k-1
    final = pow(final, 1, p-1)
    return final #посчитали и вернули результат


if __name__ == "__main__":
    g = 7
    a = 22
    p = 263

    print("Считаем методом Шаг младенца - Шаг великана: ",big_and_small_step(g, a, p)) 
    print("Исчисление порядка: ",count_order(g,a,p))
