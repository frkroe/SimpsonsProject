# The Simpsons (Maggie Level)
    ## Importaciones:
import requests
import time
import csv

    ## Función de convertir lista de dict a csv
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
    ## obtener datos de la API, guardar todos en un archivo .json y convertirlos en dict
  response_API = requests.get('https://thesimpsonsquoteapi.glitch.me/quotes')
  data = response_API.json()
  dataJSON = {"personaje": data[0]["character"], "Frase": data[0]["quote"]}
    ## guardar los datos en 3 archivos .csv diferentes
  if dataJSON["personaje"] == "Lisa Simpson":
    listaLisa.append(dataJSON)
    fileL = open("Lisa/lisa.csv", "w", newline='')
    convert(listaLisa, fileL)
  elif dataJSON["personaje"] == "Homer Simpson": 
    listaHomer.append(dataJSON)
    fileH = open("Homer/homer.csv", "w", newline='')
    convert(listaHomer, fileH)
  else:
    listaGen.append(dataJSON)
    fileG = open("General/general.csv", "w", newline='')
    convert(listaGen, fileG)
    ## esperar 30 segundos para seguir ejecutando el bucle while
  time.sleep(30)