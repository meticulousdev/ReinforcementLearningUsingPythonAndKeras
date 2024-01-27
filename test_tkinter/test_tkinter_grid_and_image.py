import tkinter as tk
from tkinter import Button
import time
import numpy as np
from PIL import ImageTk, Image

UNIT = 100
HEIGHT = 5
WIDTH = 5

PhotoImage = ImageTk.PhotoImage


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry(f"{WIDTH * UNIT}x{HEIGHT * UNIT}")
    window.title("Test Grid and Imgae")

    file_path: str = "./chap01/img/"
    up = PhotoImage(Image.open(file_path + "up.png").resize((13, 13)))
    right = PhotoImage(Image.open(file_path + "right.png").resize((13, 13)))
    left = PhotoImage(Image.open(file_path + "left.png").resize((13, 13)))
    down = PhotoImage(Image.open(file_path + "down.png").resize((13, 13)))
    rectangle = PhotoImage(Image.open(file_path + "rectangle.png").resize((65, 65)))
    triangle = PhotoImage(Image.open(file_path + "triangle.png").resize((65, 65)))
    circle = PhotoImage(Image.open(file_path + "circle.png").resize((65, 65)))

    canvas = tk.Canvas(window, bg='white',
                       height=HEIGHT * UNIT,
                       width=WIDTH * UNIT)
    
    # Grid
    for col in range(0, WIDTH * UNIT, UNIT):  # 0~400 by 80
        x0, y0, x1, y1 = col, 0, col, HEIGHT * UNIT
        canvas.create_line(x0, y0, x1, y1, fill='black')
    for row in range(0, HEIGHT * UNIT, UNIT):  # 0~400 by 80
        x0, y0, x1, y1 = 0, row, HEIGHT * UNIT, row
        canvas.create_line(x0, y0, x1, y1, fill='black')

    canvas.create_image(50, 50, image=rectangle)
    canvas.create_image(50, 150, image=triangle)
    canvas.create_image(150, 150, image=triangle)
    canvas.create_image(250, 150, image=triangle)
    
    canvas.pack()

    window.mainloop()
