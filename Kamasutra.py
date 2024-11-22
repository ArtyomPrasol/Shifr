#TABLE_CH_SIN = [['А','Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П'],
#               ['Я', 'Э', 'Ю', 'Ь', 'Ы', 'Ъ', 'Щ', 'Ш', 'Ч', 'Ц', 'Х', 'Ф', 'У', 'Т', 'С', 'Р']]

TABLE_CH_KAM = [['А', 'Б', 'Г', 'Д', 'Е', 'Ж', 'И', 'Й', 'К', 'Л', 'М', 'У', 'Ъ', 'Ф', 'Х', 'Я'],
                ['В', 'З', 'Ч', 'П', 'С', 'О', 'Н', 'Ц', 'Р', 'Щ', 'Т', 'Ш', 'Ю', 'Э', 'Ы', 'Ь']]

def encrypt(table, words):
    text = ''
    for ch in words:
        if str.isalpha(ch):
            ch = getOpponent(table, ch)
        text += ch
    return text


def decrypt(table, words):
    return encrypt(table, words)


def toLower(ch, flag):
    if flag:
        return ch.lower()
    else:
        return ch


def getPosition(table, ch):
    row = -1
    
    if ch in table[0]:
        row = 0
    elif ch in table[1]:
        row = 1

    if row != -1:
        return (row, table[row].index(ch))
    else:
        return (None, None)


def getOpponent(table, ch):
    flag = False
    
    if ch.islower():
        flag = True

    row, col = getPosition(table, ch.upper())

    if row == 1:
        return toLower(table[0][col], flag)
    elif row == 0:
        return toLower(table[1][col], flag)
    else:
        return ch
