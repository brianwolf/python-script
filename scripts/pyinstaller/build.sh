source ./scripts/pyinstaller/ambiente.sh


echo "### Borrando archivos generados anteriores"
echo 
rm -fr build/ dist/
rm -fr ${NOMBRE_PROYECTO}.spec


echo "### Ejecutando Pyinstaller"
echo
pyinstaller \
${ARCHIVO_PY_INICIADOR} \
--clean \
--onefile \
--name ${NOMBRE_PROYECTO} \
--log-level ${NIVEL_LOG} \
