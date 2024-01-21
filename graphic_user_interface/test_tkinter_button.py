import tkinter as tk
from tkinter import Button

HEIGHT = 400
WIDTH = 640


def func_counter() -> None:
    func_counter.cnt += 1
    print(f"cnt: {func_counter.cnt}")


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.title("Test Mainloop")

    canvas = tk.Canvas(window, bg='white',
                       height=HEIGHT,
                       width=WIDTH)

    # (0, 0)
    label = tk.Label(window, text="(0, 0)", width=50, height=5, fg="black", bg="white")
    canvas.create_window(0 + 50, 0 + 50, window=label)

    # (0, HEIGHT)    
    label = tk.Label(window, text="(0, HEIGHT)", width=50, height=5, fg="black", bg="white")
    canvas.create_window(0 + 50, HEIGHT - 50, window=label)
    
    # (WIDTH, 0)
    label = tk.Label(window, text="(WIDTH, 0)", width=50, height=5, fg="black", bg="white")
    canvas.create_window(WIDTH - 50, 0 + 50, window=label)
    
    # (WIDTH, HEIGHT)
    label = tk.Label(window, text="(WIDTH, HEIGHT)", width=50, height=5, fg="black", bg="white")
    canvas.create_window(WIDTH - 50, HEIGHT - 50, window=label)
    
    label = tk.Label(window, text="Click Button", width=10, height=5, fg="black", bg="white")
    canvas.create_window(WIDTH - 200, HEIGHT - 300, window=label)

    canvas.create_line(WIDTH - 200, HEIGHT - 200, WIDTH - 200, HEIGHT - 300)

    func_counter.cnt: int = 0
    test_button = Button(window, text="Button", command=func_counter)
    test_button.configure(width=10, activebackground="#33B5E5")
    canvas.create_window(WIDTH - 200, HEIGHT - 150, window=test_button)

    canvas.pack()

    window.mainloop()
