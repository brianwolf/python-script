source ./scripts/ambiente.sh

rm -fr build/ dist/
rm -fr ${NOMBRE_PROYECTO}.spec

pyinstaller \
iniciar.py \
--clean \
--onefile \
--name ${NOMBRE_PROYECTO} \
--log-level ${LOG_NIVEL} \
