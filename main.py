import collections
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

label = Label(text="New text", font=("Arial", 16, "bold"))
label.grid(column=1, row=0)

def click():
    label["text"] = f"{input.get()}"
    label.grid(column=3, row=0)

button = Button(text="click me", command=click)
button.grid(column=2, row=2)


input = Entry(width=10)
input.grid(column=4, row=4)


print(input)

window.mainloop()
