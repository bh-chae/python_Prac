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

def btncmd():
    pass
btn = Button(root, text="click", command=btncmd)

root.mainloop()