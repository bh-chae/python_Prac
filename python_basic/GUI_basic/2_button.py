import os
from tkinter import *

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")

btn1= Button(root, text= "버튼1")
btn1.pack() #포함

btn2 = Button(root, padx=5, pady=10, text="버튼22222222") # padx 가로 크기, pady 세로크기 (버튼 내용물에 따라 유동적으로 크기 변경, 남는 공간을 x, y로)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 고정된 크기
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file=os.path.join(current_path, "img.png"))
btn6 = Button(root, image= photo)
btn6.pack()

def btncmd() :
    print("Button Clicked")

btn7 = Button(root, text = "동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()