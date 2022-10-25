# The Simpsons (Lisa Level)
## Importaciones
import requests 
import datetime
import time
import string
import csv
import os.path

if not os.path.isdir("app/"):
    os.mkdir("app/")

## Lisa: Quitar signos de punctuación
dictPunct = str.maketrans("","", string.punctuation)
del dictPunct[ord("'")]

while True:
## obtener datos de la API
    response_API = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    dataJSON = response_API.json()
    datos = {"Personaje": dataJSON[0]["character"], "Frase": dataJSON[0]["quote"]}

        
## Lisa: descargar imagen del presonaje y guardarla en la carpeta del mismo (nombre con fecha/ snake_case)
    image = requests.get(dataJSON[0]["image"]).content
    fileName = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time()).replace(":", ".") + ".png"
    directory = "app/"+datos["Personaje"].translate(dictPunct).replace(" ", "_")+"/"
    filePath = os.path.join(directory, fileName)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open (filePath, "w") as f:
        f.write(image)

##Maggie: crear archivos csv para cada personaje
    fileName2 = datos["Personaje"] +".csv"
    filePath2 = os.path.join(directory, fileName2)
    with open(filePath2, 'a') as f:
        w = csv.DictWriter(f, datos)
        #w.writeheader()
        w.writerow(datos)

## Esperar 30 segundos para seguir ejecutando el bucle while
    time.sleep(3)