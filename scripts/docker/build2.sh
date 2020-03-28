printf "### Borrando archivos generados anteriores \n"
rm -fr dist/ build/ specs/

printf "### Ejecutando Pyinstaller con Docker \n"
docker run -it --rm \
-v $(pwd):/usr/src:rw \
python:3.8 /bin/sh -c "
    cd /usr/src

    pip install \
        -r src/requirements.txt \
        --upgrade pip
    
    ./scripts/pyinstaller/build.sh

    rm -fr build/ specs/

    chmod 777 . -R
    "
