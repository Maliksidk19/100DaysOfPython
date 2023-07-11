from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(width=400, height=150, padx=25, pady=25)

input_field = Entry(width=10)
input_field.grid(row=1, column=2)

label1 = Label(text="Miles")
label1.grid(row=1, column=3)

label2 = Label(text="Km")
label2.grid(row=2, column=3)

label3 = Label(text="is equal to")
label3.grid(row=2, column=1)

result = Label(text=0)
result.config(padx=2)
result.grid(row=2, column=2)


def button_clicked():
    result.config(text=int(int(input_field.get()) * 1.6))


button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

window.mainloop()
