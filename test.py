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



if __name__ == "__main__":
    unittest.main()