import tkinter as tk
from tkinter import Button
import time
import numpy as np
from PIL import ImageTk, Image

PhotoImage = ImageTk.PhotoImage
UNIT = 100  # 픽셀 수
HEIGHT = 5  # 그리드월드 세로
WIDTH = 5  # 그리드월드 가로


class GraphicDisplay(tk.Tk):
    def __init__(self):
        super(GraphicDisplay, self).__init__()
        self.title('Environment')
        self.geometry('{0}x{1}'.format(HEIGHT * UNIT, HEIGHT * UNIT + 100))
        (self.up, self.down, self.left, self.right), self.shapes = self.load_images()
        self.canvas = self._build_canvas()
    
    def _build_canvas(self):
        canvas = tk.Canvas(self, bg='white',
                           height=HEIGHT * UNIT + 100,
                           width=WIDTH * UNIT)
        # 버튼 초기화
        up_button = Button(self, text="up")
        up_button.configure(width=10, activebackground="#33B5E5")
        canvas.create_window(WIDTH * UNIT * 0.49, HEIGHT * UNIT + 20,
                             window=up_button)
        
        left_button = Button(self, text="Left")
        left_button.configure(width=10, activebackground="#33B5E5")
        canvas.create_window(WIDTH * UNIT * 0.37, HEIGHT * UNIT + 50,
                             window=left_button)
        
        right_button = Button(self, text="right")
        right_button.configure(width=10, activebackground="#33B5E5")
        canvas.create_window(WIDTH * UNIT * 0.62, HEIGHT * UNIT + 50,
                             window=right_button)
        
        down_button = Button(self, text="down")
        down_button.configure(width=10, activebackground="#33B5E5")
        canvas.create_window(WIDTH * UNIT * 0.49, HEIGHT * UNIT + 80,
                             window=down_button)

        # 그리드 생성
        for col in range(0, WIDTH * UNIT, UNIT):  # 0~400 by 80
            x0, y0, x1, y1 = col, 0, col, HEIGHT * UNIT
            canvas.create_line(x0, y0, x1, y1, fill='black')
        for row in range(0, HEIGHT * UNIT + 1, UNIT):  # 0~400 by 80
            x0, y0, x1, y1 = 0, row, HEIGHT * UNIT, row
            canvas.create_line(x0, y0, x1, y1, fill='black')

        # 캔버스에 이미지 추가
        # shapes[0]: rectangle
        # shapes[1]: triangle
        # shapes[2]: circle
        # start point
        canvas.create_image(50, 50, image=self.shapes[0])

        canvas.create_image(50, 150, image=self.shapes[1])
        canvas.create_image(150, 150, image=self.shapes[1])
        canvas.create_image(250, 150, image=self.shapes[1])

        canvas.create_image(250, 350, image=self.shapes[1])
        canvas.create_image(350, 350, image=self.shapes[1])
        canvas.create_image(450, 350, image=self.shapes[1])

        # end point
        canvas.create_image(450, 450, image=self.shapes[2])

        canvas.pack()

        return canvas

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
    grid_world = GraphicDisplay()
    grid_world.mainloop()