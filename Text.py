from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text="This is a line of text on a canvas")

canvas.create_text(130, 120, text="This is a line of text in red", fill="red")

canvas.create_text(150, 150, text="This is a line of text in Courier,", font=("Courier", 15))
