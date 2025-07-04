from abc import ABC, abstractmethod

from src.basic import *
from src.field import *
from src.source import *
from src.diffop import *
from src.solver import *

class EquationFactory(ABC):

    @abstractmethod
    def make_mesh(self) -> Mesh:
        pass

    @abstractmethod
    def make_diff_op(self) -> DiffOp:
        pass

    @abstractmethod
    def make_equation(self) -> WaveEq:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Equation1d(EquationFactory):

    def make_mesh(self) -> Mesh:
        Nx = 401
        h = 1 / (Nx-1)
        return Mesh1D(h, Nx)

    def make_diff_op(self) -> DiffOp:
        return DiffOp1D()

    def make_equation(self) -> WaveEq:
        return WaveEq1D()

    def __str__(self) -> str:
        return '1d equation factory class'

class Equation2d(EquationFactory):

    def make_mesh(self) -> Mesh:
        Nx, Ny = 401, 401
        h = 1 / (Nx-1)
        return Mesh2D(h, Nx, Ny)

    def make_diff_op(self) -> DiffOp:
        return DiffOp2D()

    def make_equation(self) -> WaveEq:
        return WaveEq2D()

    def __str__(self) -> str:
        return '2d equation equation class'

def make_factory() -> EquationFactory:

    factories = {
        "1d": Equation1d(),
        "2d": Equation2d(),
    }

    while True:
        dim = input("Please input the dimension you like: ")
        if dim in factories:
            return factories[dim]
        print("Please type 1d, 2d, or 3d.")

def make_equation() -> WaveEq:

    eqClass = make_factory()

    tau = 1 / 1000
    Nt = 1301
    # sigma = 0.02
    sigma = float(input("Please input the sigma you like: "))
    mid = 0.3
    my_time = MyTime(tau, Nt)
    f = Source(my_time)
    f.set_position(201)
    f.set_ricker_wavelet(mid, sigma)

    my_mesh = eqClass.make_mesh()
    diffOp = eqClass.make_diff_op()
    eq = eqClass.make_equation()

    eq.initialize(my_mesh, my_time, f, diffOp)

    return eq