from src import *

if __name__ == "__main__":

    eq = make_equation()
    eq.solve()
    Visualize.save_gif_1d(eq)
