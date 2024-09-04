from Canvas import Window, Maze


def main():
    # Rest time is the time between the maze appears and the solver starts
    rest_time = 5000

    # Adjust the screen_width and screen_height to your screen size
    screen_width = 1400
    screen_height = 700
    win = Window(screen_width, screen_height)

    # Decrese the cell size will increase the complexity of the maze
    cell_size_x = 30
    cell_size_y = 30

    # x and y is starting point of the map
    # x = 10 means that the map is 10 pixel from the top
    # y = 10 means that the map is 10 pixel from the left
    x = 10
    y = 10


    # Only touch below this line if you understand the code fully
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

    win.root.after(rest_time, continue_after_delay)

    win.wait_for_close()


main()
