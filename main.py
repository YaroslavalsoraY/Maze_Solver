from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line_test = Line(Point(10, 20), Point(20, 10))
    win.draw_line(line_test, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()