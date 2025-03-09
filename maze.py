from graphics import Cell
import time

class Maze():    
    def __init__(self, x1, y1, num_rows,
                 num_cols, cell_size_x, cell_size_y,
                 win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        
        self._create_cells()
    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        if self.win == None:
            return
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        
    def _draw_cell(self, i, j):
        self._cells[i][j]._x1 = self.x1 + i * self.cell_size_x
        self._cells[i][j]._x2 = self._cells[i][j]._x1 + self.cell_size_x
        self._cells[i][j]._y1 = self.y1 + j * self.cell_size_y
        self._cells[i][j]._y2 = self._cells[i][j]._y1 + self.cell_size_y

        self._cells[i][j].draw("black")
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
