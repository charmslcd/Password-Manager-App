from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
FONT="Arial"


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            username = (data[website.lower()]["email"])
            password = (data[website.lower()]["password"])
    except KeyError:
        messagebox.showinfo(title="Not Found", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="No Data File Found")
    else:
        messagebox.showinfo(title="Found", message=f"Email: {username}\n"
                                                   f"Password: {password}")
        password_input.insert(0, f"{password}")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_num + password_symbol

    print(password_list)

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    username = email_username_input.get()
    password = password_input.get()
    new_data = {
        website.lower(): {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", mode="r") as write_file:
                data = json.load(write_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as write_file:
                json.dump(new_data, write_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as write_file:
                json.dump(data, write_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
web_input = Entry(width=32)
web_input.focus()
web_input.grid(column=1, row=1)

email_username_input = Entry(width=50)
email_username_input.insert(0, "charms.salcedo@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

#Buttons

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

generate_pw = Button(text="Generate Password", command=generate_pw)
generate_pw.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()