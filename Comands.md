# Comandos en el terminal

## Crear archivo de requirements:
pip install pipreqs
pipreqs ./

## Construir docker image
docker build -t nombreImage .
docker run -d nombreImage

## Probar si el contenedor realmente funcione
*el contenedor tiene que estar ejecutando para poder entrar en ello*
docker exec -it nombreContenedor bash
*listrar los objetos que lleva*
ls
*leer el archivo (ver output del contenido)*
tail -f nombreArchivo