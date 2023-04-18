import tkinter
from tkinter import *

window=tkinter.Tk()
window.title("My GUI Interface")
window.minsize(width=500,height=500)

#Label
my_label=tkinter.Label(text="I am a Label",font=("Arial",18,"bold"))
my_label.pack()

my_label["text"]="New Text"
my_label.config(text="New Text")

#Button


def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me",command=button_clicked)
button.pack()

#Entry
input=Entry(width=10)
input.pack()
print(input.get())
















# import turtle
#
# tim=turtle.Turtle()
# tim.write("Welcome")








window.mainloop()

