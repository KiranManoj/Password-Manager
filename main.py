from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ------------------------ SEARCH GENERATOR --------------------- #


def generate_search():
    search_website = website_input.get()
    try:
        with open("saved_password_file.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")
    else:
        if search_website in data:
            mail = data[search_website]["email"]
            pass_word = data[search_website]["password"]
            messagebox.showinfo(title="The details", message=f"The username is {mail}\nThe password is {pass_word}")
            pyperclip.copy(pass_word)

        else:
            messagebox.showinfo(title="Error", message=f"No detils for {search_website} exists.")
# ------------------------ PASSWORD GENERATOR --------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ------------------------ SAVE PASSWORD --------------------- #


def save():
    website_data = website_input.get()
    email_data = user_name_input.get()
    password_data = password_input.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("saved_password_file.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("saved_password_file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("saved_password_file.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------ UI SETUP --------------------- #


window = Tk()
window.title("Password Manager")
window.minsize(height=400, width=400)
window.config(padx=50, pady=50)

# Canvas for image

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website = Label(text="Website:")
website.grid(row=1, column=0)

user_name = Label(text="Email/Username:")
user_name.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries

website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()

user_name_input = Entry(width=35)
user_name_input.insert(0, "kiranmanoj019@gmail.com")
user_name_input.grid(row=2, column=1,)

password_input = Entry(width=17)
password_input.config(width=35)
password_input.grid(row=3, column=1,)

# buttons
search_button = Button(text="Search", width=15, command=generate_search)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

