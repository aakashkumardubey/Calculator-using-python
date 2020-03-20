#imports
from tkinter import *

#Window
root=Tk()
root.geometry("300x400")
root.title("Calculator")
root.configure(background="skyblue")
root.resizable(0,0)

Welcome=Label(root,text="**Welcome**",bg="skyblue",font=("courier",20))
Welcome.place(x=55,y=10)

name=Label(root,text="Name",bg="skyblue",font=("courier",15))
name.place(x=10,y=50)

namee=Entry(root,bg="skyblue",font=("courier",15,),width=17)
namee.place(x=80,y=50)

email=Label(root,text="Email",bg="skyblue",font=("courier",15))
email.place(x=10,y=100)

emaile=Entry(root,bg="skyblue",font=("courier",15,),width=17)
emaile.place(x=80,y=100)

phone=Label(root,text="Phone",bg="skyblue",font=("courier",15))
phone.place(x=10,y=150)

phonee=Entry(root,bg="skyblue",font=("courier",15),width=17)
phonee.place(x=80,y=150)

signup=Button(root,text="Sign up",height=3,width=25,bd=4,bg="skyblue",fg="#0D0D0D")
signup.place(x=60,y=190)

skipit=Button(root,text="Jump on Calculator",height=3,width=25,bd=4,bg="skyblue",fg="#0D0D0D")
skipit.place(x=60,y=270)

mainloop()
