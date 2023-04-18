from tkinter import *

def calculator():
    print("I got clicked")
    new_miles = float(miles_input.get())
    new_km=new_miles*1.609
    kilometer_results_label.config(text=new_km)
    print(new_km)



window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equals to ")
is_equal_label.grid(column=0,row=1)

kilometer_results_label=Label(text="0")
kilometer_results_label.grid(column=1,row=1)


kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

Calculate_button=Button(text="Calculate",command=calculator)
Calculate_button.grid(column=1,row=2)





window.mainloop()