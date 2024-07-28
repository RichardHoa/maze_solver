from Canvas import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    # l = Line(Point(50, 50), Point(400, 400))
    # win.draw_line(l, "black")
    cell = Cell(win, 50, 50, 100, 100)
    cell.draw()

    cell_2 = Cell(win, 300, 300, 350, 350)
    cell_2.draw()

    cell.draw_move(cell_2,False)
    win.wait_for_close()


main()
