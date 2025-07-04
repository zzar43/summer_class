import numpy as np

from abc import ABC

from src.basic import *
from src.field import *
from src.source import *
from src.diffop import *


class WaveEq(ABC):

    @abstractmethod
    def solver(self):
        pass
class WaveEq1D(WaveEq):

    def __init__(self, my_mesh: Mesh1D, my_time: MyTime, c: Field1D, f: Source, diffOp: DiffOp1D) -> None:
        self.my_mesh = my_mesh
        self.my_time = my_time
        self.c = c
        self.f = f
        self.diffOp = diffOp
        # initialization
        self.u0 = Field1D(my_mesh.h, my_mesh.Nx)
        self.u1 = Field1D(my_mesh.h, my_mesh.Nx)
        self.u2 = Field1D(my_mesh.h, my_mesh.Nx)
        self.U = np.zeros((my_time.Nt, my_mesh.Nx))

    def solve(self):
        for idx in range(self.my_time.Nt):
            self.time_update(idx, self.f)
            self.time_copy()
            self.save_snap(idx)

    def time_update(self, idx: int, f: Source):
        lap = self.diffOp.laplace(self.u1)
        # lap = np.zeros(self.my_mesh.Nx)
        self.u2.val = 2*self.u1.val - self.u0.val + self.my_time.tau**2 / self.my_mesh.h**2 * lap
        # self.u2.val[self.f.pos] += self.my_time.tau**2 * self.f.val[idx]
        self.u2.val[self.f.pos] += self.f.val[idx]

    def time_copy(self):
        # print('maybe an error, need extra copy')
        # self.u0.set_val(np.copy(self.u1.val))
        # self.u1.set_val(np.copy(self.u2.val))
        self.u0.val = np.copy(self.u1.val)
        self.u1.val = np.copy(self.u2.val)

    def save_snap(self, idx: int):
        self.U[idx,:] = self.u1.val


class WaveEq2D(WaveEq):

    def __init__(self, my_mesh: Mesh2D, my_tine:MyTime, c: Field2D, f:Source, diffOp:DiffOp2D) -> None:
        pass

# class Solver(ABC):

#     def build_wave_1d(self) -> WaveEq1D:

#         h = 0.01
#         Nx = 101
#         tau = 1 / 1000
#         Nt = 1001
#         my_mesh = Mesh1D(h, Nx)
#         my_time = MyTime(tau, Nt)
#         f = Source(my_time)
#         c = Field1D(h, Nx)
#         diffOp = DiffOp1D()

#         return WaveEq1D(my_mesh, my_time, c, f, diffOp)

#     def build_wave_2d(self) -> WaveEq2D:
#         h = 0.01
#         Nx, Ny = 101, 101
#         tau = 1 / 1000
#         Nt = 1001
#         my_mesh = Mesh2D(h, Nx, Ny)
#         my_time = MyTime(tau, Nt)
#         f = Source(my_time)
#         c = Field2D(h, Nx, Ny)
#         diffOp = DiffOp2D()
    
#         return WaveEq2D(my_mesh, my_time, c, f, diffOp)



