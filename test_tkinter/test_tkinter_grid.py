import tkinter as tk
from tkinter import Button

UNIT = 100
HEIGHT = 5
WIDTH = 5


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry(f"{WIDTH * UNIT}x{HEIGHT * UNIT}")
    window.title("Test Grid")

    canvas = tk.Canvas(window, bg='white',
                       height=HEIGHT * UNIT,
                       width=WIDTH * UNIT)
    
    for col in range(0, WIDTH * UNIT, UNIT):  # 0~400 by 80
        x0, y0, x1, y1 = col, 0, col, HEIGHT * UNIT
        canvas.create_line(x0, y0, x1, y1, fill='black')
    for row in range(0, HEIGHT * UNIT, UNIT):  # 0~400 by 80
        x0, y0, x1, y1 = 0, row, HEIGHT * UNIT, row
        canvas.create_line(x0, y0, x1, y1, fill='black')

    canvas.pack()

    window.mainloop()
