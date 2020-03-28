. ./scripts/pyinstaller/ambiente.env


printf "\nBorrando archivos generados anteriores \n"
rm -fr dist/


printf "\nEjecutando Pyinstaller \n\n"
pyinstaller \
${CARPETA_PROYECTO}${ARCHIVO_PY_INICIADOR} \
--clean \
--onefile \
--name ${NOMBRE_PROYECTO} \
--log-level ${NIVEL_LOG} \
--add-data="src/resources/version.txt:resources"


printf "\nBorrando archivos innecesarios \n\n"
rm -fr build/ *.spec