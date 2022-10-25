# The Simpsons (Lisa Level)
## Importaciones
import requests 
import time
import string
import csv
import os.path
## Crear directorio para meter los resultados
if not os.path.isdir("app/"):
    os.mkdir("app/")
## Lisa: Quitar signos de punctuación
dictPunct = str.maketrans("","", string.punctuation)
del dictPunct[ord("'")]
## Lisa: Funcción de contar palabras para crear diccionario
counts = dict()
def word_count(str, counts):
    words = str.split()
    for word in words:
        word = word.translate(dictPunct).lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

while True:
## obtener datos de la API
    response_API = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
    dataJSON = response_API.json()
    datos = {"Personaje": dataJSON[0]["character"], "Frase": dataJSON[0]["quote"]}
## Lisa: descargar imagen del presonaje y guardarla en la carpeta del mismo (nombre con fecha/ snake_case)
    image = requests.get(dataJSON[0]["image"]).content
    fileName = datos["Personaje"].translate(dictPunct).replace(" ", "_") + ".png"
    directory = "app/"+datos["Personaje"].translate(dictPunct).replace(" ", "_")+"/"
    filePath = os.path.join(directory, fileName)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open (filePath, "wb") as f:
        f.write(image)
## Maggie: crear archivos csv de frases para cada personaje
    fileName2 = datos["Personaje"] +".csv"
    filePath2 = os.path.join(directory, fileName2)
    with open(filePath2, 'a', newline='') as f:
        w = csv.DictWriter(f, datos.keys())
        w.writerow(datos)
## Lisa: Crear y añadir palabras al diccionario
    word_count(datos["Frase"], counts)
    with open("app/cuentas.csv", "w", newline='') as csvfile:
        header_key = ["Palabra", "Cuenta"]
        new_val = csv.DictWriter(csvfile, fieldnames=header_key)
        new_val.writeheader()
        for new_k in counts:
            new_val.writerow({"Palabra": new_k, "Cuenta": counts[new_k]})
## Esperar 30 segundos para seguir ejecutando el bucle while
    time.sleep(3)