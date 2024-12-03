def mod_exp(a, d, p):
    result = 1
    while d > 0:
        if d % 2 == 1:
            result = (result * a) % p
        a = (a * a) % p
        d //= 2
    return result

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def obr(a, b):
    # a^(-1)modb
    g = extended_gcd(a, b)
    if g[0] == 1:
        return g[1] % b
    else:
        return 0

def rabin_miller_test(m, a, p, b):
    for j in range(b + 1):
        if j == 0:
            z = mod_exp(a, m, p)
        else:
            m *= 2
            z = mod_exp(a, m, p)
        if z == 1 or z == p - 1:
            return True
    return False

def find_y_square_root(x, p):
    y_square = (x * x + x) % p
    for y in range(p):
        if (y * y) % p == y_square:
            return y
    return None

def elliptic_curve_add(P, Q, a, p):
    x1, y1 = P
    x2, y2 = Q
    
    if x1 == x2 and y1 == y2:
        k = ((3 * x1 * x1 + a) * obr(2 * y1, p)) % p
    else:
        k = ((y2 - y1) * obr(x2 - x1, p)) % p
    
    x3 = (k * k - x1 - x2) % p
    y3 = (k * (x1 - x3) - y1) % p
    
    return x3, y3

def elliptic_curve_multiply(k, P, a, p):
    result = None
    addend = P
    
    while k > 0:
        if k % 2 == 1:
            if result is None:
                result = addend
            else:
                result = elliptic_curve_add(result, addend, a, p)
        addend = elliptic_curve_add(addend, addend, a, p)
        k //= 2
    
    return result

letters_to_numbers = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7,
    'Ж': 8, 'З': 9, 'И': 10, 'Й': 11, 'К': 12, 'Л': 13, 'М': 14,
    'Н': 15, 'О': 16, 'П': 17, 'Р': 18, 'С': 19, 'Т': 20, 'У': 21,
    'Ф': 22, 'Х': 23, 'Ц': 24, 'Ч': 25, 'Ш': 26, 'Щ': 27, 'Ъ': 28,
    'Ы': 29, 'Ь': 30, 'Э': 31, 'Ю': 32, 'Я': 33
}


message = ['П', 'А', 'С']
message_numbers = [letters_to_numbers[letter] for letter in message]

a = 1
b = 0
p = int(''.join(map(str, message_numbers))) 
m = (p - 1) // (2 ** b)

while not rabin_miller_test(m, a, p, b):
    p += 1

P = (2, 4224)

P_2 = elliptic_curve_add(P, P, a, p)
P_4 = elliptic_curve_add(P_2, P_2, a, p)
P_8 = elliptic_curve_add(P_4, P_4, a, p)
P_16 = elliptic_curve_add(P_8, P_8, a, p)
P_32 = elliptic_curve_add(P_16, P_16, a, p)
P_64 = elliptic_curve_add(P_32, P_32, a, p)
P_128 = elliptic_curve_add(P_64, P_64, a, p)
P_151 = elliptic_curve_add(P_128, P_16, a, p)
P_151 = elliptic_curve_add(P_151, P_4, a, p)
P_151 = elliptic_curve_add(P_151, P_2, a, p)
P_151 = elliptic_curve_add(P_151, P, a, p)

print(f"151P = {P_151}")