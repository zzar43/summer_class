import numpy as np
from abc import ABC, abstractmethod

from src.field import *

class DiffOp(ABC):

    @abstractmethod
    def laplace(self, u) -> np.ndarray:
        pass

class DiffOp1D(DiffOp):

    def __init__(self) -> None:
        pass

    def laplace(self, u: Field1D) -> np.ndarray:
        """return value is a np.ndarray."""
        res = np.zeros(u.Nx)
        res[1:-1] = u.val[2:] - 2*u.val[1:-1] + u.val[:-2]
        return res
    
    def __str__(self) -> str:
        return '1D differential operator class.'

class DiffOp2D(DiffOp):

    def __init__(self) -> None:
        pass

    def laplace(self, u: Field2D):
        """return value is a np.ndarray."""
        res = np.zeros((u.Nx, u.Ny))
        res[1:-1, 1:-1] = -4 * u.val[1:-1,1:-1] + u.val[2:,1:-1] + u.val[:-2,1:-1] + u.val[1:-1,2:] + u.val[1:-1,:-2]
        return res
    
    def __str__(self) -> str:
        return '2D differential operator class.'