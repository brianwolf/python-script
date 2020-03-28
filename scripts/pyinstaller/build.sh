source ./scripts/pyinstaller/ambiente.sh


printf "### Borrando archivos generados anteriores \n"
rm -fr build/ dist/
rm -fr ${NOMBRE_PROYECTO}.spec


printf "### Ejecutando Pyinstaller \n"
pyinstaller \
${CARPETA_PROYECTO}/${ARCHIVO_PY_INICIADOR} \
--clean \
--onefile \
--name ${NOMBRE_PROYECTO} \
--log-level ${NIVEL_LOG}
