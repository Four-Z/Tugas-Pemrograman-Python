import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import ImageTk, Image


win = tk.Tk()
namefile_temp = tk.StringVar()
code_temp = tk.StringVar()


def display():
    global checkDigit, img_lbl
    win.geometry("400x500")
    win.resizable(False, False)
    win.title("TP04 - Barcode")

    ttk.Label(win, text="Save barcode as:", font=(
        "Times", 16, "bold")).place(x=115, y=20)
    ttk.Entry(win, width=30, textvariable=namefile_temp).place(
        x=100, y=50, height=25,)
    ttk.Label(win, text="Enter code (first 12 decimal digits):",
              font=("Times", 16, "bold")).place(x=30, y=80)
    ttk.Entry(win, width=30, textvariable=code_temp).place(
        x=100, y=110, height=25,)
    Button(win, text="Add!", width=5, background="light green",
           command=lambda: validateCode()).place(x=165, y=140)

    win.mainloop()


def validateCode():
    code = code_temp.get()
    listcode = list(code)

    check = False

    if len(listcode) != 12:
        check = True
    else:
        for i in listcode:
            if i.isdigit() == False:
                check = True
                break

    if check:
        messagebox.showwarning("error", "please enter correct input code")
    else:
        generateBarcode(code)


def getNameFile():
    nameFile = namefile_temp.get()
    return nameFile


def displayBarcode(code, nameFile):
    img = Image.open(nameFile+".png")
    resized_img = img.resize((250, 200), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_img)

    canvas = Canvas(win, width=300, height=300)
    canvas.place(x=30, y=170)
    canvas.create_image(40, 40, anchor=NW, image=new_image)

    checkDigit = Label(win, text="",)
    checkDigit.place(x=80, y=420)

    checkDigit.config(text="Check Digit: " + (str(code))[-1])
    mainloop()


def generateBarcode(number):
    nameFile = getNameFile()

    barcode = EAN13(number, writer=ImageWriter())
    barcode.save(nameFile)

    displayBarcode(barcode, nameFile)


def main():
    display()


if __name__ == "__main__":
    main()
