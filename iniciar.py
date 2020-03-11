import argparse

import yaml

from ambiente import parsear_variables_de_ambiente
from script import ejecutar

_NOMBRE_ARCHIVO_YML = 'config.yml'
_AYUDA_ARCHIVO_YML = 'Archivo de parametros .yml'
_NOMBRE_CORTO_YML = '-f'
_NOMBRE_LARGO_YML = '--file'


parser = argparse.ArgumentParser()
parser.add_argument(_NOMBRE_CORTO_YML, _NOMBRE_LARGO_YML,
                    help=_AYUDA_ARCHIVO_YML, default=_NOMBRE_ARCHIVO_YML)

args = parser.parse_args()

params_yaml = yaml.safe_load(open(args.file))

ejecutar(parsear_variables_de_ambiente(params_yaml))
