from src import *

def main():

    Nx = 201
    h = 1 / (Nx-1)
    Fs = 1000
    tau = 1 / Fs
    Nt = 1001

    mid = 0.3 # s
    sigma = 0.02

    my_mesh = Mesh1D(h, Nx)
    my_time = MyTime(tau, Nt)
    f = Source(my_time)
    f.set_position(int(Nx / 2))
    f.set_ricker_wavelet(mid, sigma)
    c = Field1D(h, Nx)
    c.set_val(np.ones(Nx))

    diffOp = DiffOp1D()

    eq = WaveEq1D(my_mesh, my_time, c, f, diffOp)
    eq.solve()

    Visualize.plot_source(f)
    Visualize.save_gif_1d(eq)
    # print(eq.U.shape)

if __name__ == "__main__":

    main()