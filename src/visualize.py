import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from src.solver import *

class Visualize:
    def __init__(self) -> None:
        pass

    @classmethod
    def plot_source(cls, f: Source):
        plt.figure()
        plt.plot(f.t, f.val, '.-')
        plt.savefig('./data/source.jpg')

    @classmethod
    def save_gif_1d(cls, eq, ratio=20):
        fig, ax = plt.subplots()
        x = eq.my_mesh.x_vec
        val = np.max(eq.U)
        line, = ax.plot(x, eq.U[0,:],'.-')
        ax.set_ylim((-1*val,val))
        def animate(i):
            line.set_ydata(eq.U[i*ratio,:])  # update the data.
            return line,
        ani = animation.FuncAnimation(
            fig, animate, interval=40, blit=False, save_count=int(eq.my_time.Nt/ratio))
        ani.save("./data/movie.gif")

    @classmethod
    def save_gif_2d(cls, eq: WaveEq2D):
        print("2d")