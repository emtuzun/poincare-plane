import matplotlib.pyplot as plt
import numpy as np
# import hyperbolic

class Poincare:

    def __init__(self) -> None:
        global ax
        space_dot = np.linspace(0, 2 * np.pi, 200)
        fig, ax = plt.subplots()
        ax.plot(np.cos(space_dot), np.sin(space_dot))

    def drawLine(points):                       # buradaki noktalar kompleks numpy array nokta olacak
        line_1 = []                             # point_1 gecen teget dogru 
        line_2 = []                             # point_2 gecen teget dogru 
        cross_point = 0                         # iki dogrunun kesistigi merkez nokta
        r = 0                                   # cemberin yari capi
        dots = []                               # point_1'den point_2'ye kadar cember uzerinde bulunan noktalar
        ax.plot(np.cos(dots), np.sin(dots))     # cember yayinin cizilmesi

    def show():
        ax.axis('equal')
        plt.show()
