import tkinter
from turtle import title

window = tkinter.Tk()
window.title("My first GUI programme")
window.minsize(width=500, height=300)

#lable
my_lable = tkinter.Label(text="My Lable", font=("Areal", 12, "bold"))
my_lable.pack()

def click():
    my_lable.config(text="My Button Got Clicked")
    print("I Got Clicked")
    window.title(my_entry.get())

#button
my_button = tkinter.Button(text="Click Me", command=click)
my_button.pack()


#entry
my_entry = tkinter.Entry(width=10)
my_entry.pack()





window.mainloop()