from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd 
import Caesar as ceas
import Kamasutra as kam
import Atbash as at
import GOST as gt

flag = 0


def change_cip(choise):
    global flag
    global textCaesar
    global textKam1
    global textKam2

    choise = combobox.get()

    dropall()

    match choise:
        case "Caesar":
            flag = 1
            textCaesar = ttk.Spinbox(from_=1, to=100)
            textCaesar.pack(anchor=CENTER, padx=6, pady=6)
        case "Kamasutra":
            flag = 2
            textKam1 = ttk.Label(text=kam.TABLE_CH_KAM[0])
            textKam2 = ttk.Label(text=kam.TABLE_CH_KAM[1])
            textKam1.pack(anchor=CENTER, padx=6, pady=6)
            textKam2.pack(anchor=CENTER, padx=6, pady=6)


def dropall():
    match flag:
        case 1:
            textCaesar.destroy()
        case 2:
            textKam1.destroy()
            textKam2.destroy()


def exit_in_file(text1,text2, tcase, metod):
    with open("exit_main.txt", "a", encoding="utf-8") as f:
        f.write(f"{metod}. {tcase}: {text1} ----> {text2}\n")

def encrypt():
    new_text = ''
    old_text = textVarMax.get("1.0",END)
    choise = combobox.get()
    match choise:
        case "Caesar":
            new_text = ceas.caesar(textVarMax.get("1.0",END), int(textCaesar.get()))
        case "Kamasutra":
            new_text = kam.encrypt(kam.TABLE_CH_KAM, textVarMax.get("1.0",END))
        case "Atbash":
            new_text = at.encrypt(textVarMax.get("1.0",END))
        case "GOST":
            if len(textVarMax.get("1.0",END)) <= 12:
                new_text = "Ошибка! Добавьте больше символов!"
            else: 
                print(textVarMax.get("1.0",END))
                print(len(textVarMax.get("1.0",END)))
                new_text = gt.encrypt(textVarMax.get("1.0",END))
    exit_in_file(old_text, new_text, "Зашифровать: ", choise)

    textVarMax.replace("1.0", END, new_text)


def decrypt():
    new_text = ''
    old_text = textVarMax.get("1.0",END)
    choise = combobox.get()
    match choise:
        case "Caesar":
            new_text = ceas.caesar(textVarMax.get("1.0",END), -int(textCaesar.get()))
        case "Kamasutra":
            new_text = kam.decrypt(kam.TABLE_CH_KAM, textVarMax.get("1.0",END))
        case "Atbash":
            new_text = at.decrypt(textVarMax.get("1.0",END))
        case "GOST": 
            new_text = "Нет расшифровки"

    exit_in_file(old_text, new_text, "Расшифровать: ", choise)

    textVarMax.replace("1.0", END, new_text)


cipher = ["Caesar", "Kamasutra", "Atbash", "GOST"]

root = Tk()
root.title("Шифрование")
root.geometry('300x500')
root.resizable(False, True)

combobox = ttk.Combobox(values=cipher)
combobox.pack(anchor=CENTER, padx=6, pady=6)
combobox.bind("<<ComboboxSelected>>", change_cip)

textVarMax = Text(width = 30, height = 10, wrap=WORD)
textVarMax.pack(anchor=CENTER, padx=6, pady=6)

btn1 = ttk.Button(text="Зашифровать", command = encrypt)
btn1.pack(side=TOP, padx=25, pady=6)

btn2 = ttk.Button(text="Расшифровать", command = decrypt)
btn2.pack(side=TOP, padx=25, pady=6)

root.mainloop()