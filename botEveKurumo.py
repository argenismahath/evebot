import pyautogui
from PIL import Image
import json
from pytesseract import *
import PhotoTaker
import TextProcessing
import mause
ruta_archivo="data/json.json"
# PhotoTaker.takePhoto()
# Leer el archivo JSON
with open(ruta_archivo, "r") as archivo:
    datos = json.load(archivo)

# Acceder a los datos leídos
# print("Anomalia:", datos["Anomalia"])
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open("captura.png")

resultado = pytesseract.image_to_string(img)

if resultado:
    mause.moveMause(PhotoTaker.left, PhotoTaker.top)

#detecta si el texto de la captura de la anomalia es el mismo que el del archivo json
isAnomalie= TextProcessing.textProcessing(resultado)

print(resultado.replace("\n", " "))
