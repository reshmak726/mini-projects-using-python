from tkinter import *

clock = Tk()
clock.title('  ******Digital clock******')
clock.geometry('1000x500')
clock.config(bg='black')

lab_hr = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_hr.place(x=40,y=40,height=110,width=100)

lab_min = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_min.place(x=40,y=40,height=110,width=100)





clock.mainloop()