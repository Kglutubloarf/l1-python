from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)
    
    # Fin de votre code

    canvas.pack()
    root.mainloop()
