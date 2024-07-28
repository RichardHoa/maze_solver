from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")  # Hardcoded title
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.root.destroy()

    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class Line:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, canvas, fill_color="black"):
        # print(self.x.p1, self.y.p1, self.x.p2, self.y.p2,fill_color)
        canvas.create_line(
            self.x.p1, self.y.p1, self.x.p2, self.y.p2, fill=fill_color, width=2
        )
