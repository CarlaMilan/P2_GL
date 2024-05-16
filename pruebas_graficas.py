import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np
import matplotlib.figure

def plot():
    ax.clear()

    y = [1, 4 , 0, 5, 0, 3, 2, 1 , 2, 5, 1, 2]
    x = ['E', 'F', 'M', 'A', 'Y', 'J', 'X', 'A', 'S', 'O', 'N', 'D']

    ax.bar(x,y)
    plt.tight_layout()
    canvas.draw()



# Inicializar Tkinter
root = tk.Tk()
fig = matplotlib.figure.Figure()
ax = fig.add_subplot()

# Tkinter
frame = tk.Frame(root)
label = tk.Label(text = 'Libros leídos por mes')
label.config(font=('Courier', 32))
label.pack()

canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().pack()

frame.pack()

tk.Button(frame, text = 'Plot Graph', command = plot).pack(pady = 10)

root.mainloop()

