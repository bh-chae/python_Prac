from msilib.schema import CheckBox
import os
from tabnanny import check
from tkinter import *
from tkinter.tix import ButtonBox

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


chkvar = IntVar() #chkvar에 Int형으로 값을 저장
chkbox = Checkbutton(root, text="Not Allowed", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect # 선택 해제
chkbox.pack()

chkvar2 = IntVar()
chkbox2=Checkbutton(root, text="Week work", variable=chkvar2)
chkbox2.pack()

def btncmd() :
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()