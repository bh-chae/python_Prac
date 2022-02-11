from tkinter import *
from tkinter.tix import ButtonBox


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side ="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="CheeseBurger").pack()
Button(frame_burger, text="Chicken Burger").pack()


frame_drink = LabelFrame(root, text="Drink!!!", relief="solid", bd =3)
frame_drink.pack(side ="right", fill="both", expand=True)

drink_var = StringVar()
btn_drink1=Radiobutton(frame_drink, text="Cock", value= "코카콜라", variable=drink_var).pack()
btn_drink2=Radiobutton(frame_drink, text="Cider", value= "사이다", variable=drink_var).pack()


def btn_cmd():
    print("음료 : ", drink_var.get())

Button(root, text="Print", command=btn_cmd).pack(side="bottom")


root.mainloop()