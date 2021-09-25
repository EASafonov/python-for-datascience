from tkinter import *

root = Tk()
root.title("Расчёт витаминов")
root.geometry('640x480')
ent = Entry(root, width=20, bd=3)
ent.pack()

root.bind('<Escape>', lambda x: root.destroy())
root.mainloop()
