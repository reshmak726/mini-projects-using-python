# from cProfile import label
# from cgitb import text
from tkinter import *
# from tkinter import font
# from turtle import speed
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    labdown.config(text=down)
    labup.config(text=up)




sp=Tk()
sp.title("internet speed meter")
sp.geometry("500x650")
sp.config(bg="blue")
lab=Label(sp,text="internet speed meter",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="download speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

labdown=Label(sp,text="00",font=("Time New Roman",30,"bold"))
labdown.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="upload speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

labup=Label(sp,text="00",font=("Time New Roman",30,"bold"))
labup.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="check speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()
