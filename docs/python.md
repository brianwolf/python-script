# :stars: Instalacion con Python 3.8 y Pyinstaller

> Para esto **se toma como directorio raiz** la carpeta `src/` por lo que todos los
comandos mostrados se ejecutan dentro de esta carpeta

![alt text](img/python.png)

## Ambiente virtual

Existen scripts hechos para la creacion del ambiente virtual

* Ejecutar `./scripts/python/env.sh`

Para salir de la virtual env ejecutar `deactivate`
En caso de querer actualizar el archivo **requirements.txt** se puede ejecutar `./scripts/python/update-requirements.sh`

## Instalacion con PyInstaller

Estando dentro del ambiente virtual:

* Ejecutar `./scripts/pyinstaller/build.sh`

## Carpetas generadas

* **./dist**: contiene el ejecutable generado

---

[Volver al readme principal](../README.md)