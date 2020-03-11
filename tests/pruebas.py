import inspect
from dataclasses import dataclass


@dataclass
class Prueba:
    v1: str
    v2: int = 0

    def __eq__(self, valule):
        if self.v1 == valule.v1:
            return True
        return False


print(Prueba(v1='asd'))
