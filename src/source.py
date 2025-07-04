import numpy as np

from src.basic import MyTime

class Source:

    def __init__(self, my_time: MyTime):
        self.t = my_time.t
        self.val = np.zeros(my_time.Nt)
        self.pos = None

    def set_position(self, pos):
        self.pos = pos

    def set_ricker_wavelet(self, mid, sigma):
        tt = self.t - mid
        self.val = ( 1 - (tt/sigma)**2 ) * np.exp(-1 * tt**2 / (2 * sigma**2))

