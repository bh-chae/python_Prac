from operator import length_hint
import os
import time
from tkinter import *
import tkinter.ttk as ttk

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) #10 ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="Stop", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): 
        time.sleep(0.01) #0.01 초 대기
        
        p_var2.set(i) #progressbar 값 설정
        progressbar2.update()  #UI update
        print(p_var2.get())

btn = Button(root, text="Stop", command=btncmd2)
btn.pack()

root.mainloop()