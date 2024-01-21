import tkinter as tk

HEIGHT = 400
WIDTH = 640


class GraphicDisplay(tk.Tk):
    def __init__(self):
        super(GraphicDisplay, self).__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")


if __name__ == "__main__":
    grid_world = GraphicDisplay()
    grid_world.mainloop()
    