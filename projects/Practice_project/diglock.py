from tkinter import Tk
from tkinter import Label
import time

root=Tk()
root.title("Clock")
def Present_time():
    display_time=time.strftime("%I:%M:%S %p")
    digi_lock.config(text=display_time)
    digi_lock.after(200,Present_time)

digi_lock=Label(root,font=("arial",150) ,bg="Blue",fg="white")
digi_lock.pack()

Present_time()
root.mainloop()
