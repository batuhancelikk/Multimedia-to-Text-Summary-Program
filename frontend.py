import tkinter as tk
from tkinter import *
import backend1

root = Tk()
root.geometry("640x480")
root.wm_title("Multimedia to Text Program V.0.01")
logo = tk.PhotoImage(file="logo.png")
tk.Label(root, image=logo).pack(side="right")


l1 = tk.Label(root, text='Video URL\n', font="Helvetica 16 bold")
l1.pack()

canvas1 = tk.Canvas(root, width=100, height=10)
canvas1.pack()

video_url = tk.Entry(root, width=50)
canvas1.create_window(50, 0, window=video_url)

l2 = tk.Label(root, text='Text URL\n', font="Helvetica 16 bold")
l2.pack()

canvas2 = tk.Canvas(root, width=100, height=10)
canvas2.pack()

text_url = tk.Entry(root, width=50)
canvas2.create_window(50, 0, window=text_url)

l3 = tk.Label(root, text='Audio URL\n', font="Helvetica 16 bold")
l3.pack()

canvas3 = tk.Canvas(root, width=100, height=30)
canvas3.pack()

sound_url = tk.Entry(root, width=50)
canvas3.create_window(50, 0, window=sound_url)

btn = Button(root, text='Summarize!', command=backend1.summarize())
btn.place(x=145, y=200)

scroll_bar = Scrollbar(root)
scroll_bar.pack( side = RIGHT, fill = Y )
textBox = Text( width=40, height=15, x=150, y=210, yscrollcommand=scroll_bar.set)
textBox.pack(side=BOTTOM)

root.mainloop()
