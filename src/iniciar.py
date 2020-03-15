import argparse

import yaml

from ambiente import obtener_valor, parsear_variables_de_ambiente
from script import ejecutar

with open('version.txt') as version_archivo:
    version_script = version_archivo.read()

parser = argparse.ArgumentParser()
parser.add_argument(
    '-f', '--file', help='Archivo de parametros .yml', default='config.yml')
parser.add_argument('-v', '--version',  help='Version del script',
                    action='version', version=version_script)

args = parser.parse_args()

with open(args.file) as params_yaml_archivo:
    params_yaml = yaml.safe_load(params_yaml_archivo)

ejecutar(parsear_variables_de_ambiente(params_yaml))
