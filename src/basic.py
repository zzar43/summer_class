import numpy as np
from abc import ABC, abstractmethod

class Mesh(ABC):

    @abstractmethod
    def get_h(self) -> float:
        pass

    @abstractmethod
    def get_size(self) -> list:
        pass

class Mesh1D(Mesh):

    def __init__(self, h, Nx):
        self.h = h
        self.Nx = Nx
        self.x_vec = np.linspace(0, (Nx-1)*h, Nx)

    def get_h(self):
        return self.h
    
    def get_size(self):
        return [self.Nx]
    
    def __str__(self) -> str:
        return '1D Mesh object with size: {}.'.format(self.Nx)

class Mesh2D(Mesh):

    def __init__(self, h, Nx, Ny):
        self.h = h
        self.Nx = Nx
        self.Ny = Ny
        self.x_vec = np.linspace(0, (Nx-1)*h, Nx)
        self.y_vec = np.linspace(0, (Ny-1)*h, Ny)

    def get_h(self):
        return self.h
    
    def get_size(self):
        return [self.Nx, self.Ny]

    def __str__(self) -> str:
        return '2D Mesh object with size: {} times {}.'.format(self.Nx, self.Ny)

class MyTime:

    def __init__(self, tau, Nt):
        self.tau = tau
        self.Nt = Nt
        self.t = np.linspace(0, (Nt-1)*tau, Nt)
