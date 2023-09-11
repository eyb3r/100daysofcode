from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_field.delete(0, END)
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    specials = "[];'./<>?|:}{!@#$%^&*()_+="
    num_threshold = 0.2
    spec_threshold = 0.2

    length = random.randint(12, 14)
    password = ""

    while len(password) < length:
        if len(password) in [3, 8]:
            password += '-'

        kind = random.random()
        if kind < num_threshold:
            # add a number to a password and make numbers a little bit less probable
            password += str(random.randint(0, 9))
            num_threshold *= 0.85
        elif kind > 1 - spec_threshold:
            # add a special character to a password and make them little bit less probable
            password += random.choice(specials)
            spec_threshold *= 0.85
        else:
            # add a letter
            password += random.choice(alphabet)

    password_field.insert(0, password)
    pyperclip.copy(password)


def validate_password(password):
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():
    # save password to a file
    entry = [website_field.get(), email_field.get(), password_field.get()]
    website, email, password = entry  # allow easier handling
    json_data = None
    entry_validation = [len(x) > 0 for x in entry]
    if False in entry_validation:
        messagebox.showerror(title='Error', message='Fill all the fields.')
    else:
        new_record = {
            website: {
                "email": email,
                "password": password
            }
        }
        try:
            with open('database.json', 'r') as db:
                json_data = json.load(db)
                json_data.update(new_record)
        except (FileNotFoundError, json.JSONDecodeError):
            json_data = new_record

        finally:
            with open('database.json', 'w') as db:
                json.dump(json_data, db, indent=4)
            # clear the form
            website_field.delete(0, END)
            password_field.delete(0, END)


def find_password():
    website = website_field.get()
    try:
        if website == "":
            raise ValueError("Empty value is not allowed")

        with open('database.json', 'r') as db:
            json_data = json.load(db)

        messagebox.showinfo(title=f'{website} entry', message=f'email:{json_data[website]["email"]}\n'
                                                              f'password:{json_data[website]["password"]}')

    except FileNotFoundError:
        messagebox.showinfo(title=f'missing database', message=f'No database found.')
    except KeyError:
        messagebox.showinfo(title=f'missing key for {website}', message=f'No entry for {website} has been found.')
    except ValueError:
        messagebox.showinfo(title=f'missing website', message=f'Enter a website to search for!')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager I'll never use")
window.config(padx=50, pady=50)

logo = PhotoImage(file='logo.png')
canvas = Canvas(highlightthickness=0, width=200, height=200)
logo_widget = canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1, sticky='e')

website_field = Entry(width=25)
website_field.grid(column=1, row=1)

search_button = Button(text='Search', command=find_password, width=6)
search_button.grid(column=2, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2, sticky='e')

email_field = Entry(width=35)
email_field.insert(0, 'testmail@gmail.com')
email_field.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3, sticky='e')

password_field = Entry(width=25)
password_field.grid(column=1, row=3)

generate_button = Button(text='Generate', command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=33, command=store_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
