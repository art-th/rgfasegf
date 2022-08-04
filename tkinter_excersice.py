from tkinter import *
app = Tk()
app.title("hello tkinter")
def hi():
    pass
g1=Label(text="hello")
bt=Button(command=hi)
bt.grid(row=0)
app.mainloop()
