import tkinter
from tkinter import ttk

screen=tkinter.Tk()
screen.title("FirstApp")
screen.geometry("400x500")
screen.config(background="lightblue")

#lbl1=tkinter.Label(text="Firstname").pack()
#lbl2=tkinter.Label(text="Lastname").pack()

#lbl1=tkinter.Label(text="Firstname").place(x=0,y=0)
#lbl1=tkinter.Label(text="Lastname").place(x=0,y=30)

lbl1=tkinter.Label(text="Firstname:",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=0,column=0,sticky='W')
lbl1=tkinter.Label(text="Lastname:",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=1,column=0,sticky='W')

txt1=tkinter.Entry()
txt1.grid(row=0,column=1,sticky='W')
txt2=tkinter.Entry()
txt2.grid(row=1,column=1,sticky='W')

ch1=tkinter.Radiobutton(value=0,text="Male",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=2,column=0,sticky='W')
ch2=tkinter.Radiobutton(value=1,text="Female",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=2,column=1,sticky='W')

op1=tkinter.Checkbutton(text="Python",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=3,column=0,sticky='W')
op2=tkinter.Checkbutton(text="Java",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=4,column=0,sticky='W')
op3=tkinter.Checkbutton(text="PHP",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=5,column=0,sticky='W')
op4=tkinter.Checkbutton(text="Androis/iOS",bg="lightblue",fg="red",font="Ebrima 15 bold").grid(row=6,column=0,sticky='W')

city=["Rajkot","Ahmedabad","Baroda","Surat","Jamnagar"]
ttk.Combobox(values=city).grid(row=7,column=0)

def btnclick():
    print("Button clicked!")
    print("Firstname:",txt1.get())
    print("Lastname:",txt2.get())


tkinter.Button(command=btnclick, text="Submit",fg="red",font="Ebrima 15 bold").place(x=170,y=300)

screen.mainloop()