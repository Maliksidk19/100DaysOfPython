from tkinter.ttk import *
from tkinter import Tk, Canvas, PhotoImage, messagebox
import base64
from random import choice, shuffle, randint


# Random Password Generate
def gen_rand_pass():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    nr_letters = randint(8, 12)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

window.tk.call("source", "Files/azure.tcl")
window.tk.call("set_theme", "light")

# Canvas

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="Files/logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=2)

# Labels

web_label = Label(text="Website:", font=("Poppins", 10, "bold"), padding=10)
web_label.grid(row=2, column=1)
email_label = Label(text="Email/Username:", font=("Poppins", 10, "bold"), padding=10)
email_label.grid(row=3, column=1)
pass_label = Label(text="Password:", font=("Poppins", 10, "bold"), padding=10)
pass_label.grid(row=4, column=1)

# Entry

web_entry = Entry(width=40, font=("Poppins", 8))
web_entry.grid(row=2, column=2, columnspan=2)
web_entry.focus()
email_entry = Entry(width=40, font=("Poppins", 8))
email_entry.grid(row=3, column=2, columnspan=2)
email_entry.insert(0, "malik@hotmail.com")
pass_entry = Entry(width=40, font=("Poppins", 8))
pass_entry.grid(row=4, column=2, columnspan=2)


def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Error!!", message="Please make sure you haven't left any fields empty.")

    else:
        ans = messagebox.askyesno(title=f"{website}", message=f"These are the details Entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if ans:
            messagebox.showinfo(title=f"{website}", message="Data saved successfully!!!")
            with open("data.txt", "a") as f:
                encoded_pass = base64.b64encode(password.encode('utf-8')).decode('utf-8')
                f.write(f"{website} | {email} | {encoded_pass}\n")
                f.close()
        else:
            messagebox.showerror(title="Error Message", message="Error saving your data.")


# Buttons

pass_gen_btn = Button(width=20, text="Generate Password", cursor="hand2", command=gen_rand_pass)
pass_gen_btn.grid(row=5, column=3)
add_btn = Button(text="Add", width=20, command=save_data, cursor="hand2")
add_btn.grid(row=5, column=2)

window.mainloop()
