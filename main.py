from Canvas import Window, Line, Point, Cell, Maze


def main():
    win = Window(600, 600)
    # # l = Line(Point(50, 50), Point(400, 400))
    # # win.draw_line(l, "black")
    # cell = Cell(win, 50, 50, 100, 100)
    # cell.draw()

    # cell_2 = Cell(win, 300, 300, 350, 350)
    # cell_2.draw()
    maze = Maze(50,50,7,10,50,50,win)
    maze.create_cells()
    # print(maze.cells)
    maze.draw_cells()
    # cell.draw_move(cell_2,False)
    maze.break_entrance_and_exit()
    win.wait_for_close()



main()
