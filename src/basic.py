import numpy as np

class Mesh1D:

    def __init__(self, h, Nx):
        self.h = h
        self.Nx = Nx
        self.x_vec = np.linspace(0, (Nx-1)*h, Nx)

class Mesh2D:

    def __init__(self, h, Nx, Ny):
        self.h = h
        self.Nx = Nx
        self.Ny = Ny
        self.x_vec = np.linspace(0, (Nx-1)*h, Nx)
        self.y_vec = np.linspace(0, (Ny-1)*h, Ny)

class MyTime:

    def __init__(self, tau, Nt):
        self.tau = tau
        self.Nt = Nt
        self.t = np.linspace(0, (Nt-1)*tau, Nt)
