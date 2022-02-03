import os
from tkinter import *

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5) # 긴 텍스트를 받을 때 (줄바꿈 허용) : 이미 입력 되어있음
txt.pack()
txt.insert(END, "Input !!")

e= Entry(root, width=30) # 한줄로 값을 받을 때 (줄바꿈 안됨) : 이미 입력 되어있음
e.pack()
e.insert(0, "한줄만 입력")

def btncmd() :
    print(txt.get("1.0", END)) # (1 줄, 0번째 컬럼 )처음부터 끝까지
    print(e.get())
    
    txt.delete("1.0", END)
    e.delete(0, END)

btn =Button (root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()