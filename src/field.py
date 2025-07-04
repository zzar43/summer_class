import numpy as np

from src.basic import Mesh1D, Mesh2D

class Field1D(Mesh1D):

    def __init__(self, h, Nx):
        super().__init__(h, Nx)
        self.val = np.zeros(Nx)

class Field2D(Mesh2D):
    
    def __init__(self, h, Nx, Ny):
        super().__init__(h, Nx, Ny)
        self.val = np.zeros((Nx, Ny))


