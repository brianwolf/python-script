. ../scripts/pyinstaller/ambiente.env

# cd ${CARPETA_PROYECTO}

ls

printf "### Borrando archivos generados anteriores \n\n"
rm -fr dist/


printf "### Ejecutando Pyinstaller \n\n"
pyinstaller \
${ARCHIVO_PY_INICIADOR} \
--clean \
--onefile \
--name ${NOMBRE_PROYECTO} \
--log-level ${NIVEL_LOG} \
--add-data="version.txt:resources" \
# --specpath specs \
# --distpath dist \
# --workpath build

printf "### Borrando archivos innecesarios \n\n"
rm -fr build/ specs/

# cd ..