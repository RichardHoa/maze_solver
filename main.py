from Canvas import Window, Line, Point, Cell, Maze
import time


def main():
    # # l = Line(Point(50, 50), Point(400, 400))
    # # win.draw_line(l, "black")
    # cell = Cell(win, 50, 50, 100, 100)
    # cell.draw()

    # cell_2 = Cell(win, 300, 300, 350, 350)
    # cell_2.draw()
    # print(maze.cells)
    # cell.draw_move(cell_2,False)
    screen_width = 1500
    screen_height = 700
    win = Window(screen_width, screen_height)
    
    cell_size_x = 30
    cell_size_y = 30
    x = 10
    y = 10
    maze_rows = (screen_height - y - 50) // cell_size_y
    maze_cols = (screen_width - x - 100) // cell_size_x
    

    # cell_size_x = (screen_width - x - 100) / (maze_cols + 1)
    # cell_size_y = (screen_height - y - 100) / (maze_rows + 1)

    # print(
    #     f"formula width x: {x} + {cell_size_x} * {maze_cols} = {cell_size_x * maze_cols}"
    # )
    # print(
    #     f"formula height y: {y} + {cell_size_y} * {maze_rows} = {cell_size_y * maze_rows}"
    # )
    maze = Maze(x, y, maze_cols, maze_rows, cell_size_x, cell_size_y, win)

    maze.create_cells()
    maze.draw_cells()
    maze.break_entrance_and_exit()

    maze.break_walls_r(0, 0)

    maze.reset_cell_visited()

    maze.solve()

    win.wait_for_close()


main()
