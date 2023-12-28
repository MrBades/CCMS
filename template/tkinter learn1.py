from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=12, relief="flat",
   background="#cFc")

btn = ttk.Button(text="Sample")
oBTN= ttk.Progressbar(maximum=100.0)
btn.pack()
oBTN.pack()


root.mainloop()