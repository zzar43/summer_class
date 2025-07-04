import numpy as np

from src.basic import *
from src.field import *
from src.source import *
from src.diffop import *

class WaveEq1D:

    def __init__(self, my_mesh: Mesh1D, my_time: MyTime, c: Field1D, f: Source, diffOp: DiffOp1D) -> None:
        self.my_mesh = my_mesh
        pass

    def solve(self):
        pass

    def time_update(self):
        pass

class WaveEq2D:

    def __init__(self, my_mesh: Mesh2D, my_tine:MyTime, c: Field2D, f:Source, diffOp:DiffOp2D) -> None:
        pass



