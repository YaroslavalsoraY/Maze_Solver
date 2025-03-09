from graphics import Cell
import time
import random

class Maze():    
    def __init__(self, x1, y1, num_rows,
                 num_cols, cell_size_x, cell_size_y,
                 win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        if seed != None:
            self.seed = seed
        else:
            self.seed = random.seed()
        
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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
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
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                visit.append((i, j + 1))
            if len(visit) == 0:
                self._draw_cell(i, j)
                return
            direction_index = random.randrange((len(visit)))
            next_index = visit[direction_index]
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        return False

    def solve(self):
        return self._solve_r(0, 0)
