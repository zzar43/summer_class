import numpy as np

from src.basic import *
from src.field import *
from src.source import *
from src.diffop import *

class WaveEq1D:

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


class WaveEq2D:

    def __init__(self, my_mesh: Mesh2D, my_tine:MyTime, c: Field2D, f:Source, diffOp:DiffOp2D) -> None:
        pass



