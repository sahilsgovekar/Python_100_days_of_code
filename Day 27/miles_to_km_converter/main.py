from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=250)
window.config(padx=10, pady=10)

def calculate():
    res = entry_m.get()
    km = int(res) * 1.60934
    entry_k.insert(END, string=str(km))



#label mile
lab_m = Label(text="Mile")
lab_m.grid(column=2, row=0)

#label km
lab_km = Label(text="KM")
lab_km.grid(column=2, row=1)

# label =
label_is = Label(text="is equals to")
label_is.grid(column=0, row=1)

#entry mile
entry_m = Entry(width=7)
entry_m.insert(END, string="0")
entry_m.grid(column=1, row=0)

#entry km
entry_k = Entry(width=7)
entry_k.insert(END, string="0")
entry_k.grid(column=1, row=1)

#button cal
cal = Button(text="Calculate", command=calculate)
cal.grid(column=1, row=3)


window.mainloop()