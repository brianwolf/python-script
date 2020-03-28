import argparse
import os
import sys

import yaml

from ambiente import obtener_valor, parsear_variables_de_ambiente
from script import ejecutar


def cargar_ruta_resources() -> str:
    return f'{sys._MEIPASS}/resources' if hasattr(
        sys, '_MEIPASS') else 'resources'


def cargar_version_script():
    with open(f'{_ruta_resources}/version.txt') as version_archivo:
        return version_archivo.read()


def cargar_config_yml(ruta_config_yml: str) -> dict:
    with open(ruta_config_yml) as params_yaml_archivo:
        params_yaml = yaml.safe_load(params_yaml_archivo)

    return parsear_variables_de_ambiente(params_yaml)


if __name__ == "__main__":

    _ruta_resources = cargar_ruta_resources()

    _version_script = cargar_version_script()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', help='Archivo de parametros .yml', default='config.yml')
    parser.add_argument('-v', '--version',  help='Version del script',
                        action='version', version=_version_script)

    args = parser.parse_args()

    ejecutar(cargar_config_yml(args.file))
