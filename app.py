# import all necessary python packages needed.
# tkinter package is used in creating Desktop User Interfaces
# time package is used to derive our displaying time depending on what is to accomplished
from tkinter import Label, Tk
import time

# Create a
clock_window = Tk()
clock_window.title("Simple Digital Clock")
clock_window.geometry("355x135")
clock_window.configure(bg='#0f4d19')
clock_window.resizable(0, 0)

text_font = ("Arial Black", 68, 'bold')
background = "#0f4d19"
foreground = "#6fc27c"
border_width = 20

label = Label(clock_window, font=text_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)


def simple_digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, simple_digital_clock)


simple_digital_clock()
clock_window.mainloop()
