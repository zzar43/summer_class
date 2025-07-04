import numpy as np
from abc import ABC, abstractmethod

class Mesh(ABC):

    @abstractmethod
    def initialize(self):
        pass

class Mesh1D(Mesh):

    def __init__(self):
        self.h = 0
        self.Nx = 0
        self.x_vec = None

    def initialize(self):
        self.Nx = 401
        self.h = 1 / (self.Nx-1)
        self.x_vec = np.linspace(0, (self.Nx-1)*self.h, self.Nx)

    def __str__(self) -> str:
        return '1D Mesh object with size: {}.'.format(self.Nx)

class Mesh2D(Mesh):

    def __init__(self):
        self.h = 0
        self.Nx = 0
        self.Ny = 0
        self.x_vec = None
        self.y_vec = None

    def initialize(self):
        self.Nx, self.Ny = 401, 401
        self.h = 1 / (self.Nx-1)
        self.x_vec = np.linspace(0, (self.Nx-1)*self.h, self.Nx)
        self.y_vec = np.linspace(0, (self.Ny-1)*self.h, self.Ny)

class MyTime:

    def __init__(self):
        self.tau = 0
        self.Nt = 0
        self.t = None

    def initialize(self):
        self.tau = 1 / 1000
        self.Nt = 1001
        self.t = np.linspace(0, (self.Nt-1)*self.tau, self.Nt)
