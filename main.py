from Canvas import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    # l = Line(Point(50, 50), Point(400, 400))
    # win.draw_line(l, "black")
    cell = Cell(win, 50, 50, 200, 200)
    cell.has_bottom_wall = False
    cell.draw()

    cell_2 = Cell(win, 300, 300, 400, 400)
    cell_2.has_top_wall = False
    cell_2.draw()

    win.wait_for_close()


main()
