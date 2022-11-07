import tkinter


def click():
    my_lable.config(text="My Button Got Clicked")
    print("I Got Clicked")
    window.title(my_entry.get())

# Window
window = tkinter.Tk()
window.title("My first GUI programme")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#lable
my_lable = tkinter.Label(text="My Lable", font=("Areal", 12, "bold"))
# my_lable.pack()
# my_lable.place(x=0, y=0)
my_lable.grid(column=0, row=0)


#button
my_button = tkinter.Button(text="Click Me", command=click)
my_button.grid(column=1, row=1)

#new button
new_b = tkinter.Button(text="text")
new_b.grid(column=2, row=0)

#entry
my_entry = tkinter.Entry(width=10)
my_entry.grid(column=3, row=2)


#layout and positioning
#placd and grid



window.mainloop()