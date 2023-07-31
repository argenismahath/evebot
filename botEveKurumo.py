import pyautogui
from PIL import Image
import json
from pytesseract import *
import PhotoTaker
import TextProcessing
import mause
import time
import comeToAnomalie
import asyncio
# import EnemyAlert
import fight

whileCounter = 1

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def takePhotografie(number):
    # Toma la captura de pantalla y la guarda como captura.png
    PhotoTaker.takePhoto(number)

ruta_archivo = "data/json.json"

# Leer el archivo JSON
with open(ruta_archivo, "r") as archivo:
    datos = json.load(archivo)

def checkAnomaliesImage():
    takePhotografie(whileCounter)
    time.sleep(2.5)
    img = Image.open("captura.png")

    resultado = pytesseract.image_to_string(img)

    # Detecta si el texto de la captura de la anomalia es el mismo que el del archivo json
    isAnomalie = TextProcessing.textProcessing(resultado)

    # print(isAnomalie)
    return isAnomalie

# Corregir el bucle
while not checkAnomaliesImage() and whileCounter < 6:
    whileCounter = whileCounter + 1

async def mi_funcion_asincronica():
    if checkAnomaliesImage():
        print(PhotoTaker.values[whileCounter])
        mause.moveMause(1192, PhotoTaker.values[whileCounter], datos["Salto"])
        time.sleep(10)
        await comeToAnomalie.abegingScanner()
        print("pass")
        await fight.startFight()
        time.sleep(30)
        await fight.activar_comeToAnomalie()
        # EnemyAlert.periodic_enemy_check()

async def main():
    whileCounter = 1

    # Corregir el bucle
    while not checkAnomaliesImage() and whileCounter < 6:
        whileCounter = whileCounter + 1
        print("hace click")

    # Llamar a la función asincrónica con await
    await mi_funcion_asincronica()

# Llamar a la función principal asincrónica
asyncio.run(main())