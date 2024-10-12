from tkinter import *

#create a new window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)


#Input
mile_input = Entry(width=8)
mile_input.grid(column= 1, row = 0)
#Labels
miles_sentence = Label(text="Miles", font=("Arial", 24))
miles_sentence.grid(column =2, row=0)
miles_sentence.config(padx=0, pady=5)

sentence = Label(text="is equal to ", font=("Arial", 24))
sentence.grid(column =0, row=1)
sentence.config(padx=5, pady=5)

km = Label(text= "0", font=("Arial", 24))
km.grid(column =1, row=1)
km.config(padx=0, pady=5)

km_sentence = Label(text="Km", font=("Arial", 24))
km_sentence.grid(column =2, row=1)
km_sentence.config(padx=0, pady=5)

def button_click():
    km.config(text=f"{round(float(mile_input.get()) * 1.609, 2)}")

button = Button(text="Calculate", command=button_click)
button.grid(column = 1, row = 2)

window.mainloop()