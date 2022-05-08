import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


root = tk.Tk()
root.geometry("2000x1080")
container = ttk.Frame()
root.title('Covid Analysis Dashboard : ')
canvas = tk.Canvas(container,width=1300, height=700)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

img = Image.open("img1.png")
resized = img.resize((1250, 500), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic)
label.pack(padx=20, pady=20)

img1 = Image.open("img2.png")
resized1 = img1.resize((1250, 500), Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resized1)
canvas.place(anchor='nw')
tk.Label(text="Grid Layout")
label = tk.Label(scrollable_frame, image=new_pic1)
label.pack(padx=20, pady=20)

img2 = Image.open("img3.png")
resized2 = img2.resize((1250, 500), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized2)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic2)
label.pack(padx=20, pady=20)

img3 = Image.open("img4.png")
resized3 = img3.resize((1250, 500), Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resized3)
canvas.place(anchor='nw')
tk.Label(text="Normal Layout")
label = tk.Label(scrollable_frame, image=new_pic3)
label.pack(padx=20, pady=20)

container.pack(padx=20, pady=20)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
