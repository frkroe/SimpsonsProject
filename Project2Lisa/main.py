# The Simpsons (Lisa Level)
## Importaciones
import requests 
import datetime
import time
import string
import csv
import os.path

## Maggie: Función de convertir lista de dict a csv y Crear 3 listas/carpetas para guardarlo
def convert(lista, file):
    with file:
        dict_writer = csv.DictWriter(file, lista[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(lista)
listaGen = []
listaLisa = []
listaHomer = []
if not os.path.isdir("General/"):
    os.mkdir("General/")
if not os.path.isdir("Lisa/"):
    os.mkdir("Lisa/")
if not os.path.isdir("Homer/"):
    os.mkdir("Homer/")

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
## Maggie: crear csv's
    if datos["Personaje"] == "Lisa Simpson":
        listaLisa.append(datos)
        fileL = open("Lisa/lisa.csv", "w", newline='')
        convert(listaLisa, fileL)
    elif datos["Personaje"] == "Homer Simpson":
        listaHomer.append(datos)
        fileH = open("Homer/homer.csv", "w", newline='')
        convert(listaHomer, fileH)
    else:
        listaGen.append(datos)
        fileG = open("General/general.csv", "w", newline='')
        convert(listaGen, fileG)
## Lisa: descargar imagen del presonaje y guardarla en la carpeta del mismo (nombre con fecha/ snake_case)
    image = requests.get(dataJSON[0]["image"]).content
    fileName = str(datetime.datetime.now().date()) + "_" + str(datetime.datetime.now().time()).replace(":", ".") + ".png"
    folderName = datos["Personaje"].translate(dictPunct).replace(" ", "_")
    directory = folderName+"/"
    filePath = os.path.join(directory, fileName)
    if not os.path.isdir(directory):
        os.mkdir(directory)
    with open (filePath, "wb") as f:
        f.write(image)
## Lisa: Crear y añadir palabras al diccionario
    word_count(datos["Frase"], counts)
    with open("cuentas.csv", "w", newline='') as csvfile:
        header_key = ["Palabra", "Cuenta"]
        new_val = csv.DictWriter(csvfile, fieldnames=header_key)
        new_val.writeheader()
        for new_k in counts:
            new_val.writerow({"Palabra": new_k, "Cuenta": counts[new_k]})
## Esperar 30 segundos para seguir ejecutando el bucle while
    time.sleep(3)