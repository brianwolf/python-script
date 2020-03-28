source ./scripts/docker/ambiente.sh


printf "### Borrando archivos generados anteriores \n"
rm -fr src/dist/ src/build/ src/specs/

printf "### Ejecutando Pyinstaller con Docker \n"
docker run -it --rm \
-v $(pwd)/src:${CARPETA_PROYECTO}:rw \
python:3.8 /bin/sh -c "
    cd ${CARPETA_PROYECTO}
    
    pip install \
        -r requirements.txt \
        --upgrade pip
    
    pyinstaller ${ARCHIVO_PY_INICIADOR} \
        --clean \
        --onefile \
        --name ${NOMBRE_PROYECTO} \
        --log-level ${NIVEL_LOG} \
        --specpath ./specs

    chmod 777 . -R
    "
