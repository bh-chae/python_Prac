import os
from tkinter import *

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "WaterMelon")
listbox.insert(END, "Grape")
listbox.pack()

def btncmd() :
    # listbox.delete(END) # 맨뒤 항목 삭제 
    # listbox.delete(0) # 맨처음 항목 삭제
    
    #갯수 확인
    # print("There are", listbox.size(), "fruits")
    
    #항목 확인(시장 idx, 끝 idx)
    # print("1~3번째 항목 : ", listbox.get(0,2))
    
    # 선택된 항목 확인 (위치로 반환)
    print("Here :", listbox.curselection())

btn =Button (root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()