import argparse

from src.codigo import ejecutar
from src.modelo import Argumento
from src.parametros import _lista_args

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--var", help="increase output verbosity", default='default')

args = parser.parse_args()
print(args._get_kwargs())
