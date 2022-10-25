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
  dataJSON = response_API.json()
  datos = {"personaje": dataJSON[0]["character"], "Frase": dataJSON[0]["quote"]}
    ## guardar los datos en 3 archivos .csv diferentes
  listaGen.append(datos)
  fileG = open("app/General/general.csv", "w", newline='')
  convert(listaGen, fileG)
  if datos["personaje"] == "Lisa Simpson":
    listaLisa.append(datos)
    fileL = open("app/Lisa/lisa.csv", "w", newline='')
    convert(listaLisa, fileL)
  elif datos["personaje"] == "Homer Simpson": 
    listaHomer.append(datos)
    fileH = open("app/Homer/homer.csv", "w", newline='')
    convert(listaHomer, fileH)
    ## esperar 30 segundos para seguir ejecutando el bucle while
  time.sleep(30)