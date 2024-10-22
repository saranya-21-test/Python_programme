'''write a python program to calculate a discount for a customer  based on  the purchased amount
using tkinter
conditions:
purchase>=$500: 20% discount
purchase>=200 and <$500: 10% discount
purchase<$200: NO Discount
input: text box in tkinter window
purchase=int(e1.get())
if():
  dis=0.2
elif():
    dis=0.1
else:
  "no discount"
amout_to_be_paid=
print("total amout to be paid",)
 '''





from tkinter import*
from tkinter import messagebox



window=Tk()
window.title("Discount app")
window.config(bg="red")
window.geometry("350x400")

def discount():
    purchase=int(e1.get())
    if purchase>=500:
        messagebox.showinfo("RESULT","20 % DISCOUNT U WILL GET")
        Total_amount=purchase*0.2
    elif purchase>=200 and purchase<500:
        messagebox.showinfo("RESULT", "10 % DISCOUNT U WILL GET")
        Total_amount=purchase*0.1

    else:
        messagebox.showinfo("RESULT", "NO DISCOUNT U WILL GET")
        Total_amount=purchase




l1=Label(window,text="ENTER THE AMOUNT:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
'''l2=Label(window,text="Enter the HEIGHT:")
l2.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=1,column=1)'''

b1=Button(window,text="Discount",command=discount)
b1.grid(row=2,column=0)
'''b2=Button(window,text="Perimeter")
b2.grid(row=2,column=1)'''

window.mainloop()