import numpy as np

from src.field import *

class DiffOp1D:

    def __init__(self) -> None:
        pass

    def laplace(self, u: Field1D):
        """return value is a np.ndarray."""
        res = np.zeros(u.Nx)
        res[1:-1] = u.val[2:] - 2*u.val[1:-1] + u.val[:-2]
        return res
        

class DiffOp2D:

    def __init__(self) -> None:
        pass

    def laplace(self, u: Field2D):
        """return value is a np.ndarray."""
        res = np.zeros((u.Nx, u.Ny))
        res[1:-1, 1:-1] = -4 * u.val[1:-1,1:-1] + u.val[2:,1:-1] + u.val[:-2,1:-1] + u.val[1:-1,2:] + u.val[1:-1,:-2]
        return res