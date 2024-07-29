import unittest

from Canvas import Window, Line, Point, Cell, Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.create_cells()

        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_huge(self):
        num_cols = 400
        num_rows = 200

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.create_cells()

        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_odd(self):
        num_cols = 157
        num_rows = 259

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.create_cells()

        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_even(self):
        num_cols = 100
        num_rows = 50

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.create_cells()

        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 3
        num_rows = 3
        win = Window(600, 600)

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,win)
        m1.create_cells()
        m1.draw_cells()
        m1.break_entrance_and_exit()
        self.assertEqual(
            m1.cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_reset_cell_visited(self):
        num_cols = 3
        num_rows = 3
        win = Window(600, 600)

        m1 = Maze(0, 0, num_rows, num_cols, 30, 30,win)
        m1.create_cells()
        m1.draw_cells()
        m1.break_walls_r(0,0)
        m1.reset_cell_visited()
        m1.break_entrance_and_exit()

        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(m1.cells[i][j].visited, False)



if __name__ == "__main__":
    unittest.main()
