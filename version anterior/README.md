# Python-Scripts

> Estructura para ejecutar sripts de python como si fuesen scripts de linux

Esto permite un mejor lenguaje que *bash* para hacer cosas muchas mas copadas

![alt text](docs/img/script.jpg)

---

## :open_book: Documentacion adicional

* [Instalacion con Docker](docs/docker.md)
* [Instalacion con Python](docs/python.md)

---

## :tada: Uso

Luego de haber instalado el proyecto y creado el ejecutable, ejecutarlo como cualquier otro script desde la raiz del proyecto

* `./dist/{NOMBRE_DEL_EJECUTABLE}`

## :package: Despliegue

La aplicacion se despliega de forma automatica utilizando *CircleCI* cada vez que se realiza un merge a la rama *master*,
para ello utiliza los scripts dentro de la carpeta `scripts/`, es decir que ejecutar los scripts manualmente es similar a lo que ejecutan las tasks dentro de los jobs del pipeline de circleci

Este despliegue consiste en:

**Contruccion**:

* Construir el ejecutable con docker mediante el script de *docker/build.sh*

**Subir nueva version**:

* Subir el nuevo ejecutable dentro de un repo de *GitHub* distinto para administrar las versiones
* Generar un Tag en ambos repos con la nueva version creada
* Hacer un push en el repo de versiones

## :earth_americas: Paginas

* [Docker Hub Python](https://hub.docker.com/_/python)
* [CircleCI](https://circleci.com/)
* [Emoticones del Readme](https://github.com/ikatyang/emoji-cheat-sheet)

## :grin: Autor

> **Brian Lobo**

* Github: [brianwolf](https://github.com/brianwolf)
* Docker Hub:  [brianwolf94](https://hub.docker.com/u/brianwolf94)
