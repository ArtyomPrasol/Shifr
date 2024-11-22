a, z = ord('а'), ord('я')
A, Z = ord('А'), ord('Я')

def caesar(words, shift):
    text = ''

    for ch in words:
        if ch.islower():
            text += gChange(ch, a, z, shift)
        elif ch.isupper():
            text += gChange(ch, A, Z, shift)
        else:
            text += ch
    return text


def gChange(ch, A, Z, shift):
    result = dif = ord(ch) + shift
    if dif > Z:
        result = (dif - Z) % 33 - 1 + A
    elif dif < A:
        result = Z - ((A - dif) % 33 - 1)
    return chr(result)
