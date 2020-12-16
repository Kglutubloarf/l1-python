import tkinter as tk
import random

couleur="red"
figure = []

def choix_couleur():
    global couleur
    couleur=input()

def dessine_cercle():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    figure.append(canvas.create_oval(x - 50, y - 50, x + 50, y + 50, fill=couleur))

def dessine_carre():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    figure.append(canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50, fill=couleur))

def dessine_croix():
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)
    figure.append(canvas.create_line(x - 50, y - 50, x + 50, y + 50, fill=couleur))
    figure.append(canvas.create_line(x - 50, y + 50, x + 50, y - 50, fill=couleur))

def undo():
    if len(figure) == 0:
        return
    canvas.delete(figure[-1])
    del figure[-1]

    if len(figure) == 0:
        return

    if canvas.type(figure[-1]) == "line":
        canvas.delete(figure[-1])
        del figure[-1]    


# canvas.type(figure[-1]) == "line"

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400
root = tk.Tk()
root.title("DESSIN")
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief=tk.GROOVE, bd=1)

def create_button(text, fonction, i, j):
    bouton = tk.Button(text=text, command = fonction, font = ("Helvetica", "30"), activeforeground="red", activebackground="black", padx=100)
    bouton.grid(column=i, row=j)
    return bouton

# Début de votre code
cercle = create_button("cercle", dessine_cercle, 0, 1)
carre = create_button("carre",   dessine_carre, 0, 2)
croix = create_button("croix",   dessine_croix, 0, 3)
choix = create_button("choisir une couleur",  choix_couleur, 1, 0)
undo = create_button("Undo", undo, 0, 0)
# Fin de votre code

canvas.grid(column=1, row = 1, rowspan=3)
canvas.create_oval(150, 150, 250, 250)
root.mainloop()
