
from tkinter import*
from tkinter import Listbox

window=Tk()
window.geometry("250x350")
window.config(bg="Lavender")
l1=Label(window,text="ACT APP")
l1.pack()
scroll_bar=Scrollbar(window)
scroll_bar.pack(side=RIGHT,fill=Y)
my_list=Listbox(window,yscrollcommand=scroll_bar.set)
for line in range(1,50):
    my_list.insert(END,"Alladi Cloud"+str(line))
my_list.pack(side=LEFT,fill=BOTH)
scroll_bar.config(command=my_list.yview)

window.mainloop()

