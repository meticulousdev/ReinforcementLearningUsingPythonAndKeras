import tkinter as tk
from tkinter import Button
import time
import numpy as np
from PIL import ImageTk, Image

UNIT = 100
HEIGHT = 5
WIDTH = 5

PhotoImage = ImageTk.PhotoImage


class GraphicDisplay(tk.Tk):
    def __init__(self):
        super(GraphicDisplay, self).__init__()
        (self.up, self.down, self.left, self.right), self.shapes = self.load_images()

    def load_images(self):
        file_path: str = "./chap01/img/"
        up = PhotoImage(Image.open(file_path + "up.png").resize((13, 13)))
        right = PhotoImage(Image.open(file_path + "right.png").resize((13, 13)))
        left = PhotoImage(Image.open(file_path + "left.png").resize((13, 13)))
        down = PhotoImage(Image.open(file_path + "down.png").resize((13, 13)))
        rectangle = PhotoImage(Image.open(file_path + "rectangle.png").resize((65, 65)))
        triangle = PhotoImage(Image.open(file_path + "triangle.png").resize((65, 65)))
        circle = PhotoImage(Image.open(file_path + "circle.png").resize((65, 65)))
        return (up, down, left, right), (rectangle, triangle, circle)


if __name__ == "__main__":
    # window = tk.Tk()
    # file_path: str = "./chap01/img/"
    # up = PhotoImage(Image.open(file_path + "up.png").resize((13, 13)))

    gd = GraphicDisplay()
    print(gd.up)
    # print(type(gd.up))

    window = tk.Tk()
    window.geometry(f"{WIDTH * UNIT}x{HEIGHT * UNIT}")
    window.title("Test Grid")

    canvas = tk.Canvas(window, bg='white',
                       height=HEIGHT * UNIT,
                       width=WIDTH * UNIT)

    canvas.create_image(50, 50, image=gd.shapes[0])
    
    canvas.pack()

    window.mainloop()
