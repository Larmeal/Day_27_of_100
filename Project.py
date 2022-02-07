# ทำโปรแกรมคำนวณ Km

from tkinter import *


window = Tk()
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
window.title("Mail to Km Converter")

label_mails = Label(text="Miles", font=("Arial", 10))
label_mails.grid(column=2, row=0)

label_km = Label(text="Km", font=("Arial", 10))
label_km.grid(column=2, row=1)

label_is = Label(text="is equal to", font=("Arial", 10))
label_is.grid(column=0, row=1)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

label_values_km = Label(text="0", font=("Arial", 10))
label_values_km.grid(column=1, row=1)

def calculator():
    data_mails = float(input_miles.get())
    data_km = round(data_mails * 1.60934)
    label_values_km.config(text=f"{data_km}")

button = Button(text="Calculate", command=calculator)
button.grid(column=1, row=2)

window.mainloop()