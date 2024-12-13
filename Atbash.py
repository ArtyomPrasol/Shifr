def encrypt(initial): #шифрование Атбашем

    output = ""
    alphabet = {}
    a = ord('а')
    y = ord('я')
    A = ord('А')
    Y = ord('Я')

    for i in range(32): #Проходим по алфавиту
        alphabet[chr(a+i)] = chr(y - i)
        alphabet[chr(A+i)] = chr(Y - i)
    

    for char in initial:
        if char in alphabet:
            output += alphabet[char]
        else:
            output += char

    return output

def decrypt(initial):
    return encrypt(initial)