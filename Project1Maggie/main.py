# The Simpsons (Maggie Level)
## Importaciones
import requests
import time
import csv
## Función de convertir una lista de diccionarios a csv
def convert(lista, file):
  with file:
    dict_writer = csv.DictWriter(file, lista[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(lista)
## Crear 3 listas para guardar los datos obtenidos de la API
listaGen = []
listaLisa = []
listaHomer = []

while True:
## obtener datos de la API, guardar todos en un archivo .json y convertirlos en un diccionario
  response_API = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
  dataJSON = response_API.json()
  datos = {"Personaje": dataJSON[0]["character"], "Frase": dataJSON[0]["quote"]}
## guardar los datos en 3 archivos .csv diferentes
  listaGen.append(datos)
  fileG = open("General/general.csv", "w", newline='')
  convert(listaGen, fileG)
  if datos["Personaje"] == "Lisa Simpson":
    listaLisa.append(datos)
    fileL = open("Lisa/lisa.csv", "w", newline='')
    convert(listaLisa, fileL)
  elif datos["Personaje"] == "Homer Simpson": 
    listaHomer.append(datos)
    fileH = open("Homer/homer.csv", "w", newline='')
    convert(listaHomer, fileH)
## esperar 30 segundos para seguir ejecutando el bucle while
  time.sleep(30)