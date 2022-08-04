from tkinter import *
app = Tk()
app.title("hello tkinter")
def hi():
    pass
l1 = Label(text="hello")
l1.grid(row=1)
bt=Button(command=hi)
bt.grid(row=0)
app.mainloop()
