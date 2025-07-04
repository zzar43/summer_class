
from abc import ABC, abstractmethod
from src import *

class WaveEq(ABC):

    @abstractmethod
    def solve(self):
        pass

class WaveEq1d(WaveEq):

    def solve(self):
        my_mesh = Mesh1D()
        my_mesh.initialize()
        my_time = MyTime()
        my_time.initialize()
        f = Source(my_time)
        pass

class WaveEq2d(WaveEq):

    def solve(self):
        pass






class EqFactory(ABC):

    @abstractmethod
    def get_mesh(self) -> Mesh:
        pass

    @abstractmethod
    def get_diff_op(self) -> DiffOp:
        pass

class Eq1d(EqFactory):

    def get_mesh(self) -> Mesh:
        return Mesh1D()
    
    def get_diff_op(self) -> DiffOp:
        return DiffOp1D()
    
    def get_solver(self) -> WaveEq:
        my_mesh = self.get_mesh()
        my_mesh.initialize()
        diffOp = self.get_diff_op()

        my_time = MyTime()
        my_time.initialize()
        c = Field1D()
        c.initialize()
        f = Source(my_time)
        f.set_position(200)
        f.set_ricker_wavelet(0.5, 0.02)

        return WaveEq1D(my_mesh, my_time, c, f, diffOp)

class Eq2d(EqFactory):

    def get_mesh(self) -> Mesh:
        return Mesh2D()
    
    def get_diff_op(self) -> DiffOp:
        return DiffOp2D()


def main():

    # eq = WaveEq()


if __name__ == "__main__":


    main()