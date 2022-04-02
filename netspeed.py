from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import font
import speedtest

sp=Tk()
sp.title("internet speed meter")
sp.geometry("500x650")
sp.config(bg="blue")
lab=Label(sp,text="internet speed meter",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="download speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="upload speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="check speed",font=("Time New Roman",30,"bold"),relief=RAISED)
button.place(x=60,y=360,height=50,width=380)

sp.mainloop()
