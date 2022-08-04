from tkinter import *
app = Tk()
app.title("hello tkinter")
def hi():
    pass
def h():
    print("hel")
    

l1 = Label(text="hajfoiajgfdsgsdgdfsgsdgfsdgsdgfiofdjaiofjdioafjioadfjiofjaoifjaiosdfjo")
l1.grid(row=1)
bt=Button(command=hi)
bt.grid(row=0,column=1)
app.mainloop()
