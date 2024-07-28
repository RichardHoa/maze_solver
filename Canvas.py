from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")  # Hardcoded title
        self.canvas = Canvas(
            self.root, width=self.width, height=self.height, bg="white"
        )
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
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(
        self,
        p1,
        p2,
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, window, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        if self.has_left_wall:
            self.window.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            )
        if self.has_right_wall:
            self.window.draw_line(
                Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            )
        if self.has_top_wall:
            self.window.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            )
        if self.has_bottom_wall:
            self.window.draw_line(
                Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            )

    def draw_move(self, to_cell,undo=False):
        origin_cell_center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        to_cell_center = Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)
        if undo == False:
            self.window.draw_line(Line(origin_cell_center,to_cell_center),"red")
        else:
            self.window.draw_line(Line(to_cell_center,origin_cell_center),"black")
            