import argparse
import sys
from os import path

import yaml

from ambiente import obtener_valor, parsear_variables_de_ambiente
from script import ejecutar

_ruta_base = sys._MEIPASS if hasattr(sys, '_MEIPASS') else ''
_ruta_resources = path.join(_ruta_base, 'resources')
_ruta_archivo_version = path.join(_ruta_resources, 'version.txt')
_ruta_archivo_config_yml = path.join(_ruta_base, 'config.yml')


def cargar_version_script(ruta_archivo: str):
    with open(ruta_archivo) as version_archivo:
        return version_archivo.read()


def cargar_config_yml(ruta_config_yml: str) -> dict:
    if not path.exists(ruta_config_yml):
        salir_con_error(
            f'Archivo yml de configuracion {ruta_config_yml} no encontrado')

    with open(ruta_config_yml) as params_yaml_archivo:
        try:
            params_yaml = yaml.safe_load(params_yaml_archivo)
        except Exception as _:
            salir_con_error('Archivo yml no valido')

    return parsear_variables_de_ambiente(params_yaml)


def salir_con_error(mensaje: str):
    print(f'Error: {mensaje}')
    sys.exit(0)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--file', help='Archivo de parametros .yml', default=_ruta_archivo_config_yml)
    parser.add_argument('-v', '--version',  help='Version del script',
                        action='version', version=cargar_version_script(_ruta_archivo_version))

    args = parser.parse_args()

    ejecutar(cargar_config_yml(args.file))
