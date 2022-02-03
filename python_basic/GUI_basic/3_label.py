import os
from tkinter import *

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1= Label(root, text="ㅎㅇ")
label1.pack()

photo = PhotoImage(file=os.path.join(current_path, "img.png"))
label2 = Label(root, image=photo)
label2.pack()

def change() :
    label1.config(text="Seeya")
    global photo2
    photo2= PhotoImage(file=os.path.join(current_path, "img2.png"))
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()