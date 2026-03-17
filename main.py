import tkinter

window = tkinter.Tk()
window.geometry("300x200")
window.title("Unit Converter")
window.config(padx=100, pady=50)

# Entry
input_miles = tkinter.Entry(window, width=10)
input_miles.grid(column=1, row=0)

# Label
my_label = tkinter.Label(window, text="miles")
my_label.grid(column=2, row=0)

def button_clicked():
    miles = float(input_miles.get())
    km = miles * 1.609
    answer.config(text=f"{km}")

ans = tkinter.Label(window, text="~")
ans.grid(column=0, row=1)

answer = tkinter.Label(window, text="0")
answer.grid(column=1, row=1)

a_label = tkinter.Label(window, text="kms")
a_label.grid(column=2, row=1)

# Button
button = tkinter.Button(window, text="Convert", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()