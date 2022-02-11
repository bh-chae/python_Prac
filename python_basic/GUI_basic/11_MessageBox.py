import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


def info():
    msgbox.showinfo("Alarm", "Activate Gass")
    
def warn():
    msgbox.showwarning("경고", "좌석 매진ㄴㄴㄴ")
    
def err():
    msgbox.showerror("err", "errrrrrr")
    
    
def okcancel():
    msgbox.askokcancel("확인 / 취소", "유아 동반석 예매 하십니까?")
    
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적 오류 재시도??")
    
def yesno():
    response= msgbox.askyesno("Y/N", "일단 냅다 Y")
    if response == 1 :
        print("Oh yes1111111")
    else : print("Gpd damn it!2222222222")

    
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="저장하고 종료 진행하시겠습니까??")
    # Y : 저장 후 종료, N : 저장 않고 종료, C : 종료 취소
    print("Response : ", response) # True : 1, False : 0 , None : 그 외
    if response == 1 :
        print("Oh yes")
    elif response == 0 :
        print("OMG NO!")
    else : print("Gpd damn it!")


Button(root, command=info, text="Alarm").pack()
Button(root, command=warn, text="Warning").pack()
Button(root, command=err, text="ERrrrrrr").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예/아니오").pack()
Button(root, command=yesnocancel, text="예/아니오/취소").pack()

root.mainloop()