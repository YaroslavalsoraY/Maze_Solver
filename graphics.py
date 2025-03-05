from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
            )


class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_working = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.is_working = True
        while self.is_working:
            self.redraw()
        print("...closed...")
    
    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)

    def close(self):
        self.is_working = False
