import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from src.solver import *

class Visualize:
    def __init__(self) -> None:
        pass

    def save_gif_1d(self, eq: WaveEq1D, ratio=10):
        fig, ax = plt.subplots()
        x = eq.my_mesh.x_vec
        line, = ax.plot(x, eq.U[0,:])
        def animate(i, ratio):
            line.set_ydata(eq.U[int(i / ratio),:])  # update the data.
            return line,
        ani = animation.FuncAnimation(
            fig, animate, interval=40, blit=True)

    def save_gif_2d(self, eq: WaveEq2D):
        print("2d")