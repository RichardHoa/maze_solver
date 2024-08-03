from Canvas import Window, Maze


def main():

    screen_width = 1400
    screen_height = 700
    win = Window(screen_width, screen_height)

    cell_size_x = 40
    cell_size_y = 40
    x = 10
    y = 10
    maze_rows = (screen_height - y - 50) // cell_size_y
    maze_cols = (screen_width - x - 50) // cell_size_x

    maze = Maze(x, y, maze_cols, maze_rows, cell_size_x, cell_size_y, win)

    maze.create_cells()
    maze.draw_cells()
    maze.break_entrance_and_exit()
    maze.break_walls_r(0, 0)

    def continue_after_delay():
        maze.reset_cell_visited()
        maze.solve()

    win.root.after(15000, continue_after_delay)

    win.wait_for_close()


main()
