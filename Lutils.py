from tkinter import *
from tkinter import ttk
import hashlib

def encode ():
    encodeWay = codeChosen.get();
    expressKey = expressKeyEntry.get()
    secretKey = secretKeyEntry.get()
    if secretKey:
        expressKey = expressKey + secretKey
    encodeRes = expressKey
    if encodeWay == "MD5" :
        md5 = hashlib.md5()
        md5.update(expressKey.encode("utf-8"))
        encodeRes = md5.hexdigest()
    elif encodeWay == "AES" :
        print()
    elif encodeWay == "DES" :
        print()
    elif encodeWay == "3DES":
        print()

    ciphertextKeyEntry.delete(0, END)
    ciphertextKeyEntry.insert(0, encodeRes)

master = Tk()

# 左侧button
code = Button(master, text="加解密").grid(sticky=E)
find = Button(master, text="查询").grid(sticky=E)

# 右侧加密解密方式
codeWay = StringVar()
codeChosen = ttk.Combobox(master, width=6, textvariable=codeWay)
codeChosen['values'] = ("AES", "DES", "3DES", "MD5")
codeChosen.grid(column=1, row=0)
codeChosen.current(0)

# 秘钥以及输入框
secretKeyLabel = Label(master, text="秘钥")
secretKeyEntry = Entry(master)
secretKeyLabel.grid(column=2, row=0)
secretKeyEntry.grid(column=3, row=0)

encodeBtn = Button(master, text="加密", command=encode).grid(column=5, row=0)
decodeBtn = Button(master, text="解密").grid(column=6, row=0)

# 明文以及输入框
expressKeyLabel = Label(master, text="明文")
expressKeyEntry = Entry(master)
expressKeyLabel.grid(column=2, row=1)
expressKeyEntry.grid(column=3, row=1)

# 密文以及输入框
ciphertextKeyLabel = Label(master, text="密文")
ciphertextKeyEntry = Entry(master)
ciphertextKeyLabel.grid(column=5, row=1)
ciphertextKeyEntry.grid(column=6, row=1)



# e1 = Entry(master)
# e2 = Entry(master)
#
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# var = IntVar()
# checkbutton = Checkbutton(master, text='Preserve aspect', variable=var)
# checkbutton.grid(columnspan=2, sticky=W)

# button1 = Button(master, text='Zoom in')
# button1.grid(row=2, column=2)
#
# button2 = Button(master, text='Zoom out')
# button2.grid(row=2, column=3)

mainloop()
