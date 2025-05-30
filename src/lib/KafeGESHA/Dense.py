from global_utils import check_sig
from TypeUtils import gesha_t, cadena_t
from lib.KafeGESHA.Gesha import Gesha

class Dense(Gesha):
    def __init__(self):
        self.a = 5
        super().__init__()

    @check_sig([2], [gesha_t], [cadena_t])
    def fit(self, text):
        print(text)

    def add(self):
        pass
