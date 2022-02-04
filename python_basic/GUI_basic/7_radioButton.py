from msilib.schema import CheckBox
import os
from tabnanny import check
from tkinter import *
from tkinter.tix import ButtonBox

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="Select Menu").pack()

burger_var=IntVar()
btn_burger1=Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2=Radiobutton(root, text="Cheese burger", value=2, variable=burger_var)
btn_burger3=Radiobutton(root, text="Chicken burger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Select Drink").pack()

drink_var = StringVar()
btn_drink1=Radiobutton(root, text="Cock", value="Cock", variable=drink_var)
btn_drink1.select()
btn_drink2=Radiobutton(root, text="Cider", value="Cider", variable=drink_var)


btn_drink1.pack()
btn_drink2.pack()

def btncmd() :
    print(burger_var.get()) #선택된 값 출력
    print(drink_var.get()) #선택된 값 출력

    

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()