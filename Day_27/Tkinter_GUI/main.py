from tkinter import *

def calculate():
    input_text = int(miles_input.get())
    label_4["text"] = str(round(input_text*1.60934))




window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)

#Label
label_1 = Label(text="Miles", font=("Arial",18))
label_1.grid(row=0, column=2)

label_2 = Label(text="Km", font=("Arial",18))
label_2.grid(row=1, column=2)

label_3 = Label(text="is equal to", font=("Arial",18))
label_3.grid(row=1, column=0)

label_4 = Label(text="0", font=("Arial",18))
label_4.grid(row=1, column=1)


#Button
button = Button(text="Calculate", command = calculate)
button.grid(row=2, column=1)


#Entry
miles_input = Entry(width = 15)
miles_input.grid(row=0, column=1)



window.mainloop()