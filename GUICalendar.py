from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calendar")
root.geometry("600x400")

cal = Calendar(root, year = 2021, month = 5, day = 25)
cal.pack(pady=0)

root.mainloop()