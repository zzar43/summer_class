import numpy as np
from abc import ABC, abstractmethod

from src.basic import *
from src.field import *
from src.source import *
from src.diffop import *

class WaveEq(ABC):

    @abstractmethod
    def initialize(self, my_mesh: Mesh, my_time: MyTime, f: Source, diffOp: DiffOp):
        pass

    @abstractmethod
    def solve(self):
        pass

class WaveEq1D(WaveEq):

    def __init__(self) -> None:
        super().__init__()

    def initialize(self, my_mesh: Mesh, my_time: MyTime, f: Source, diffOp: DiffOp) -> None:

        self.h = my_mesh.get_h()
        self.Nx = my_mesh.get_size()[0]

        self.my_mesh = my_mesh
        self.my_time = my_time
        self.f = f
        self.diffOp = diffOp
        # initialization
        self.u0 = Field1D(self.h, self.Nx)
        self.u1 = Field1D(self.h, self.Nx)
        self.u2 = Field1D(self.h, self.Nx)
        self.U = np.zeros((my_time.Nt, self.Nx))

    def solve(self):
        for idx in range(self.my_time.Nt):
            self.time_update(idx, self.f)
            self.time_copy()
            self.save_snap(idx)

    def time_update(self, idx: int, f: Source):
        lap = self.diffOp.laplace(self.u1)
        self.u2.val = 2*self.u1.val - self.u0.val + self.my_time.tau**2 / self.h**2 * lap
        self.u2.val[self.f.pos] += self.my_time.tau**2 * self.f.val[idx]

    def time_copy(self):
        self.u0.val = np.copy(self.u1.val)
        self.u1.val = np.copy(self.u2.val)

    def save_snap(self, idx: int):
        self.U[idx,:] = self.u1.val

    def __str__(self) -> str:
        return '1D wave equation.'


class WaveEq2D(WaveEq):

    def __init__(self) -> None:
        super().__init__()

    def initialize(self, my_mesh: Mesh, my_time:MyTime, f:Source, diffOp:DiffOp) -> None:
        pass

    def solve(self):
        pass

    def __str__(self) -> str:
        return '2D wave equation.'

