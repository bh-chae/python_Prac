from msilib.schema import CheckBox
import os
from tabnanny import check
from tkinter import *
import tkinter.ttk as ttk
from tkinter.tix import ButtonBox

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


values=[str(i) + "일" for i in range(1,32)]

combobox = ttk.Combobox(root, height=5, values = values)
combobox.pack()
combobox.set("Day of Credit Card Paying")

read_combobox = ttk.Combobox(root, height=10, values = values, state="readonly") # 읽기 전용
read_combobox.current(0) # 0번째 인덱스 값 선택
read_combobox.pack()



def btncmd():
    print(combobox.get())
    print(read_combobox.get())
    
btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()