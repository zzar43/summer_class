import numpy as np

from src.basic import Mesh1D, Mesh2D

class Field1D(Mesh1D):

    def __init__(self):
        super().__init__()
        self.val = np.array(1)

    def initialize(self):
        self.Nx = 401
        self.h = 1 / (self.Nx-1)
        self.x_vec = np.linspace(0, (self.Nx-1)*self.h, self.Nx)
        self.val = np.zeros(self.Nx)

    def set_val(self, val):
        self.val = val

    def set_ones(self):
        self.val = np.ones(self.Nx)

class Field2D(Mesh2D):
    
    def __init__(self):
        super().__init__()
        self.val = np.array(1)

    def set_val(self, val):
        self.val = val

    def initialize(self):
        self.Nx, self.Ny = 401, 401
        self.h = 1 / (self.Nx-1)
        self.x_vec = np.linspace(0, (self.Nx-1)*self.h, self.Nx)
        self.y_vec = np.linspace(0, (self.Ny-1)*self.h, self.Ny)
        self.val = np.zeros((self.Nx, self.Ny))

    def set_ones(self):
        self.val = np.ones((self.Nx, self.Ny))