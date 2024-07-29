from tkinter import Tk, BOTH, Canvas

import time
import random


class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze solver by Thái Hoà") 
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
    def __init__(self, x1, y1, x2, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.visited = False

    def draw(self):
        # time.sleep(0.05)
        if self.has_left_wall:
            self.window.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            )
        elif self.has_left_wall == False:
            self.window.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "white"
            )

        if self.has_right_wall:
            self.window.draw_line(
                Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            )
        elif self.has_right_wall == False:
            self.window.draw_line(
                Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "white"
            )

        if self.has_top_wall:
            self.window.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            )
        elif self.has_top_wall == False:
            self.window.draw_line(
                Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "white"
            )

        if self.has_bottom_wall:
            self.window.draw_line(
                Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            )
        elif self.has_bottom_wall == False:
            self.window.draw_line(
                Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "white"
            )

    def draw_move(self, to_cell, undo=False):
        origin_cell_center = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        to_cell_center = Point(
            (to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2
        )
        if undo == False:
            self.window.draw_line(Line(origin_cell_center, to_cell_center), "red")
        else:
            self.window.draw_line(Line(to_cell_center, origin_cell_center), "white")


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_cols,
        num_rows,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.cells = []

        if seed is not None:
            print("using seed: ", seed)
            random.seed(seed)
        else:
            print("seed is none")
            random.seed()

    def create_cells(self):
        for i in range(self.num_cols):
            columns_cell = []
            for j in range(self.num_rows):
                columns_cell.append(
                    Cell(
                        self.x1 + i * self.cell_size_x,
                        self.y1 + j * self.cell_size_y,
                        self.x1 + (i + 1) * self.cell_size_x,
                        self.y1 + (j + 1) * self.cell_size_y,
                        self.window,
                    )
                )
            self.cells.append(columns_cell)

    def draw_cells(self):
        for i in range(self.num_cols):
            for cell in self.cells[i]:
                cell.draw()
                # self.animate()
        


    def animate(self):
        self.window.redraw()
        time.sleep(0.01)

    def break_entrance_and_exit(self):
        first_cell = self.cells[0][0]
        last_cell = self.cells[self.num_cols - 1][self.num_rows - 1]
        first_cell.has_top_wall = False
        last_cell.has_bottom_wall = False
        first_cell.draw()
        last_cell.draw()

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        # self.animate()

        while True:
            list = []
            # left cell
            if i > 0 and self.cells[i - 1][j].visited == False:
                list.append([i - 1, j])
            # right cell
            if i < self.num_cols - 1 and self.cells[i + 1][j].visited == False:
                list.append([i + 1, j])
            # top cell
            if j > 0 and self.cells[i][j - 1].visited == False:
                list.append([i, j - 1])
            # bottom cell
            if j < self.num_rows - 1 and self.cells[i][j + 1].visited == False:
                list.append([i, j + 1])

            if len(list) == 0:
                self.cells[i][j].draw()
                break

            index = random.randint(0, len(list) - 1)
            dest_i = list[index][0]
            dest_j = list[index][1]
            dest_cell = self.cells[dest_i][dest_j]

            # bottom cell
            if self.cells[i][j].y2 == dest_cell.y1:
                self.cells[i][j].has_bottom_wall = False
                dest_cell.has_top_wall = False

            # right cell
            if self.cells[i][j].x2 == dest_cell.x1:
                self.cells[i][j].has_right_wall = False
                dest_cell.has_left_wall = False

            # top cell
            if self.cells[i][j].y1 == dest_cell.y2:
                self.cells[i][j].has_top_wall = False
                dest_cell.has_bottom_wall = False

            # left cell
            if self.cells[i][j].x1 == dest_cell.x2:
                self.cells[i][j].has_left_wall = False
                dest_cell.has_right_wall = False

            self.cells[i][j].draw()
        
            dest_cell.draw()

            self.break_walls_r(dest_i, dest_j)

    def reset_cell_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

        # for i in range(self.num_cols):
        #     for j in range(self.num_rows):
        #         # print(f"cell {i}, {j} visited: {self.cells[i][j].visited}")
    
    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self.animate()
        current_cell = self.cells[i][j]
        # print("___________________")
        

        current_cell.visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            print("Solved!")
            return True

        # Left cell
        if (
            i > 0
            and self.cells[i - 1][j].visited == False
            and current_cell.has_left_wall == False
        ):
            current_cell.draw_move(self.cells[i - 1][j])
            # print(f"current in cell {i}, {j}")
            # print(
            #     f"Goes to the left cell at {i - 1}, {j}"
            # )

            if self.solve_r(i - 1, j):
                return True
            else:
                current_cell.draw_move(self.cells[i - 1][j], undo=True)

        # right cell
        if (
            i < self.num_cols - 1
            and self.cells[i + 1][j].visited == False
            and current_cell.has_right_wall == False
        ):
            current_cell.draw_move(self.cells[i + 1][j])
            # print(f"current in cell {i}, {j}")
            # print(
            #     f"Goes to the right cell at {i + 1}, {j}"
            # )
            if self.solve_r(i + 1, j):
                return True
            else:
                current_cell.draw_move(self.cells[i + 1][j], undo=True)


        # bottom cell
        if (
            j < self.num_rows - 1
            and self.cells[i][j + 1].visited == False
            and current_cell.has_bottom_wall == False
        ):
            current_cell.draw_move(self.cells[i][j + 1])
            # print(f"current in cell {i}, {j}")
            # print(f"Goes down the bottom cell at {i}, {j + 1}")
            if self.solve_r(i, j + 1):
                return True
            else:
                current_cell.draw_move(self.cells[i][j + 1], undo=True)
                

        # top cell
        if (
            j > 0
            and self.cells[i][j - 1].visited == False
            and current_cell.has_top_wall == False
        ):
            current_cell.draw_move(self.cells[i][j - 1])
            # print(f"current in cell {i}, {j}")
            # print(f"Goes up the top cell at {i}, {j - 1}")
            if self.solve_r(i, j - 1):
                return True
            else:
                current_cell.draw_move(self.cells[i][j - 1], undo=True)


        
        print(f"reach dead end at {i}, {j}")
        return False


