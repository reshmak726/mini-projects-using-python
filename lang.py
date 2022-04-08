from cgitb import text
from tkinter import *
from tkinter import ttk

from googletrans import Translator,LANGUAGES

















root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source text",font=("Time New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=100,height=20,width=300)


sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")

button_chnge = Button(frame,text="Translate",relief=RAISED)
button_chnge.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")


lab_txt = Label(root,text="Dest text",font=("Time New Roman",20,"bold"),fg="black",bg="red")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)









root.mainloop()