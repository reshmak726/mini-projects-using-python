from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")


    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)


clock = Tk()
clock.title('  ******Digital clock******')
clock.geometry('1000x500')
clock.config(bg='black')

lab_hr = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_hr.place(x=120,y=50,height=110,width=100)

lab_hr_text = Label(clock,text="Hour",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_hr_text.place(x=120,y=190,height=40,width=100)

lab_min = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_min.place(x=340,y=50,height=110,width=100)

lab_min_text = Label(clock,text="min.",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_min_text.place(x=340,y=190,height=40,width=100)


lab_sec = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_text = Label(clock,text="sec.",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_sec_text.place(x=560,y=190,height=40,width=100)      


lab_am = Label(clock,text="00",font=('TimesNewRoman',50,"bold"),bg="white",fg="black")
lab_am.place(x=780,y=45,height=110,width=100)

lab_am_text = Label(clock,text="am/pm",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_am_text.place(x=780,y=190,height=40,width=100)  

#     ********************date************

lab_date = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_date.place(x=120,y=270,height=110,width=100)

lab_date_text = Label(clock,text="Date",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_date_text.place(x=120,y=410,height=40,width=100)

lab_mo= Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_mo.place(x=340,y=270,height=110,width=100)

lab_mo_text = Label(clock,text="Month",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_mo_text.place(x=340,y=410,height=40,width=100)

lab_year = Label(clock,text="00",font=('TimesNewRoman',60,"bold"),bg="white",fg="black")
lab_year.place(x=560,y=270,height=110,width=100)

lab_year_text = Label(clock,text="Year",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_year_text.place(x=560,y=410,height=40,width=100) 


lab_day = Label(clock,text="00",font=('TimesNewRoman',30,"bold"),bg="white",fg="black")
lab_day.place(x=780,y=270,height=110,width=100)

lab_day_text = Label(clock,text="day",font=('TimesNewRoman',20,"bold"),bg="white",fg="black")
lab_day_text.place(x=780,y=410,height=40,width=100) 


date_time()
clock.mainloop()