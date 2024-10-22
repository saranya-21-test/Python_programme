from tkinter import*
from tkinter import messagebox



window=Tk()
window.title("rect")
window.config(bg="yellow")
window.geometry("350x400")

def area():
    wdth=int(e1.get())
    height=int(e2.get())

    messagebox.showinfo("RESULT",wdth*height)
    area=wdth*height

def perimeter():
    wdth=int(e1.get())
    height=int(e2.get())

    messagebox.showinfo("RESULT",2*(wdth+height))
    perimeter=2*(height+wdth)



l1=Label(window,text="ENTER THE WIDTH:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
l2=Label(window,text="Enter the HEIGHT:")
l2.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=1,column=1)

b1=Button(window,text="Area",command=area)
b1.grid(row=2,column=0)
b2=Button(window,text="Perimeter",command=perimeter)
b2.grid(row=2,column=1)

window.mainloop()