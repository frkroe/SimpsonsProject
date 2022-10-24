import requests 
#1 descargar 
url = 'https://thesimpsonsquoteapi.glitch.me/quotes'
response_API = requests.get(url)
datosjson = response_API.json()
datos = {"personaje": datosjson[0]["character"], "frase": datosjson[0]["quote"]}
print(f'La frase de {datos["personaje"]} es: {datos["frase"]}')

'''## descargar imagen
### en while-bucle cada imagen necesita un nombre individual (p.ej. con id())
img_data = requests.get(datosjson[0]["image"]).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)'''