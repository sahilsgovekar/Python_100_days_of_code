from tkinter import *
from tkinter import Message
from tkinter import messagebox
import random
import pyperclip
import json


# .........................Searching to json .............. #
def search():
    user_ent = ent_web.get()

    try:
        with open("passward_list.json") as data_file:
            data = json.load(data_file)
            ent_eu.delete(0, END)
            ent_pass.delete(0, END)
            email = data[user_ent]["email?username"]
            passw = data[user_ent]["passward"]
            ent_eu.insert(END, string=data[user_ent]["email?username"])
            ent_pass.insert(END, string=data[user_ent]["passward"])
            messagebox.showinfo(title=user_ent ,message=f"Email : {email} \nPassward : {passw}")

    except:
        messagebox.showinfo(message="Data Dosent Exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_passward():

    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    ent_pass.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def sav_pass():
    web_val = ent_web.get()
    eu_val = ent_eu.get()
    pas_val = ent_pass.get()

    #checking no entry validation
    if len(web_val) <= 0:
        messagebox.showinfo(message="No website found")
    elif len(eu_val) <= 0:
        messagebox.showinfo(message="No email/username found")
    elif len(pas_val) <= 0:
        messagebox.showinfo(message="No Passward found")
    else:
        new_data = {
            web_val : 
            {
                "email?username" : eu_val,
                "passward" : pas_val
            }
        }

        is_ok = messagebox.askokcancel(title="PasswardGenerated", message="Do you want to add it to the server?") 
        if is_ok:
            try:
                with open("passward_list.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("passward_list.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            
            else:
                data.update(new_data)
                with open("passward_list.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            
            finally:
                #deleting entries
                ent_web.delete(0, END)
                ent_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passward Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#labels
#label_website
lab_web = Label(text="Website")
lab_web.grid(column=0, row=1)

#label email/username
lab_eu = Label(text="Email/Username")
lab_eu.grid(column=0, row=2)

#label pass
lab_pass = Label(text="Passward")
lab_pass.grid(column=0, row=3)


#Entries
#website entry
ent_web = Entry(width=21)
ent_web.grid(column=1, row=1)
ent_web.focus()

#email/username entry
ent_eu = Entry(width=40)
ent_eu.grid(column=1, row=2, columnspan=2)
ent_eu.insert(END, string="youremail@email.com")

#pass
ent_pass = Entry(width=21)
ent_pass.grid(column=1, row=3)


#buttons
#gen pass 
but_genp = Button(text="Generate Passward", command=generate_passward)
but_genp.grid(column=2, row=3)

#add
but_add = Button(text="Add", width=35, command=sav_pass)
but_add.grid(column=1, row=4, columnspan=2)

#search
but_serch = Button(text="Search", command=search, width=10)
but_serch.grid(column=2, row=1)





window.mainloop()