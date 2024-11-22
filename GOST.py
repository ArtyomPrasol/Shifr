sbox = (
        (4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3),
        (14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9),
        (5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11),
        (7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3),
        (6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2),
        (4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14),
        (13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12),
        (1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12),
        )


nums = {0: '0000', 1: '0001', 2: '0010', 3: '0011', 
        4: '0100', 5: '0101', 6: '0110', 7: '0111', 
        8: '1000', 9: '1001', 10: '1010', 11: '1011', 
        12: '1100', 13: '1101', 14: '1110', 15: '1111'}


bins = {'0000': 0, '0001': 1, '0010': 2, '0011': 3, 
        '0100': 4, '0101': 5, '0110': 6, '0111': 7, 
        '1000': 8, '1001': 9, '1010': 10, '1011': 11, 
        '1100': 12, '1101': 13, '1110': 14, '1111': 15}


def makeChar32():
    alphabet = {}
    a = ord('а')
    A = ord('А')
    for i in range(32):
        alphabet[chr(a+i)] = bin(224 + i)[2:len(bin(192 + i))]
        alphabet[chr(A+i)] = bin(192 + i)[2:len(bin(224 + i))]
    alphabet[' '] = '00'+bin(32)[2:len(bin(224 + i))]
    return alphabet


def checkText(text, alp):
    l = ''
    r = ''
    key = ''
    for i in range(4): l += alp[text[i]]
    for i in range(4): r += alp[text[i + 4]]
    for i in range(4): key +=  alp[text[i + 8]]
    return l,r,key


def sumBin(m,n):
    O = '1'
    Z = '0'
    f = 0
    r = ''
    for i in range(len(m)-1, -1, -1):
        if (m[i] == Z and n[i] == O) or (m[i] == O and n[i] == Z): 
            if f: 
                r += Z
            else: 
                r += O
        if m[i] == O and n[i] == O:
            if f: 
                r += O
            else: 
                r += Z
                f = 1
        if m[i] == Z and n[i] == Z:
            if f: 
                r += O
                f = 0
            else: r += Z
    return ''.join(reversed(r))


def modBin(m,n):
    O = '1'
    Z = '0'
    r = ''
    for i in range(len(m)-1, -1, -1):
        if (m[i] == Z and n[i] == O) or (m[i] == O and n[i] == Z): r += O
        if m[i] == O and n[i] == O: r += Z
        if m[i] == Z and n[i] == Z: r += Z
    return ''.join(reversed(r))

def changeWithMatrix(m):
    global bins
    global nums
    global sbox
    text = ''
    for i in range(8, 0, -1):
        j = 8 - i
        text += nums[sbox[i-1][bins[m[j*4:4+j*4]]]]
    return text
    
def encrypt(text):
    l,r,k = checkText(text, makeChar32())
    print("l = " + l)
    print("r = " + r)
    print("k = " + k)
    print("r mod32 k = " + sumBin(r,k))
    new_text = changeWithMatrix(sumBin(r,k))
    print("Change : " + new_text)
    crypt = new_text[11:len(new_text)] + new_text[0:11]
    print("11 bites: " + crypt)
    print("F : " + modBin(crypt,l))
    return modBin(crypt,l)
