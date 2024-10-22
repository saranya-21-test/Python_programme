from tkinter import*
from tkinter import messagebox



window=Tk()
window.config(bg="red")
window.geometry("350x400")

def grad():
    score=int(e1.get())
    if score >= 90:
        messagebox.showinfo("RESULT", "YOU WILL GET A GRADE")
        GRADE=A
    elif score >= 80 and score < 90:
        messagebox.showinfo("RESULT", " U WILL GET B GRADE")
        GRADE=B
    elif score >= 70 and score < 80:
        messagebox.showinfo("RESULT", "U WILL GET C GRADE")
        GRADE=C
    elif score >= 60 and score < 70:
        messagebox.showinfo("RESULT", "U WILL GET D GRADE")
        GRADE=D
    else:
        messagebox.showinfo("RESULT", "U WILL GET E GRADE")
        GRADE=E



l1=Label(window,text="ENTER THE SCORE:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
'''l2=Label(window,text="Enter the HEIGHT:")
l2.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=1,column=1)'''

b1=Button(window,text="grad",command=grad)
b1.grid(row=2,column=0)
'''b2=Button(window,text="Perimeter")
b2.grid(row=2,column=1)'''

window.mainloop()