from tkinter import*

root = Tk()
root.title("Clock")
root.geometry("800x125") # W X H 
root.maxsize("1000","125")

import datetime
now = datetime.datetime.now()
time = now.strftime("%H : %M : %S ") 
Hour= now.strftime("%H") 
Hour = (int(Hour))

if Hour >= 12 :

    Clock = Label(root,font=("ds-digital",80), bg = "black" , fg = "cyan", text = time+"PM")
    Clock.pack(fill = X)
else:
    Clock = Label(root,font=("ds-digital",80), bg = "black" , fg = "cyan", text = time+"AM")
    Clock.pack(fill = X)

root.mainloop()