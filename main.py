from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
FONT="Arial"

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
    print(website, username, password)

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This are the details entered: \n"
                                                      f"Email: {username}\n"
                                                      f"Password: {password}\n"
                                                      f"Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as write_file:
                write_file.write(f"{website} | {username} | {password} \n")
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
web_input = Entry(width=50)
web_input.focus()
web_input.grid(column=1, row=1, columnspan=2)

email_username_input = Entry(width=50)
email_username_input.insert(0, "charms.salcedo@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_pw = Button(text="Generate Password", command=generate_pw)
generate_pw.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)






window.mainloop()