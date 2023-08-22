import pyautogui
from PIL import Image
import json
from pytesseract import *
import PhotoTaker
import TextProcessing
import datetime
import mause
import time
import keyboard
import comeToAnomalie
import asyncio
# import EnemyAlert
import fight

whileCounter = 1
closeWhileII=False

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def takePhotografie(number):
    # Toma la captura de pantalla y la guarda como captura.png
    PhotoTaker.takePhoto(number)

ruta_archivo = "data/json.json"

# Leer el archivo JSON
with open(ruta_archivo, "r") as archivo:
    datos = json.load(archivo)

async def checkAnomaliesImage():
    global whileCounter
    
    print(whileCounter)
    takePhotografie(whileCounter)
    time.sleep(2.5)
    img = Image.open("captura.png")

    resultado = pytesseract.image_to_string(img)

    # Detecta si el texto de la captura de la anomalia es el mismo que el del archivo json
    isAnomalie = TextProcessing.textProcessing(resultado)

    # print(isAnomalie)
    if isAnomalie:
        await mi_funcion_asincronica(whileCounter)
        whileCounter=6

    else:
        whileCounter = whileCounter + 1
    
    return isAnomalie

# # Corregir el bucle
# while not checkAnomaliesImage() and whileCounter < 6:
#     whileCounter = whileCounter + 1

async def main():
    global whileCounter

    # mause.unDock()

    result= PhotoTaker.enemiesCheck()
    if result[0] > 0 or result[1] > 0:
        print("hay enemigos :,V a las ", datetime.datetime.now())
    else:
        mause.unDock()
        time.sleep(20)
        # mause.dock()
        mause.openAnomalieMenu()

        while whileCounter < 6:
            await checkAnomaliesImage() 
        #     print("hace click")

    # Llamar a la función asincrónica con await

async def mi_funcion_asincronica(num):
        # print(PhotoTaker.values[whileCounter])
        
        mause.moveMause(1192, PhotoTaker.values[num], datos["Salto"])
        time.sleep(10)
        await comeToAnomalie.abegingScanner()
        print("pass")
        await fight.startFight()
        time.sleep(30)
        await fight.activar_comeToAnomalie()
        # EnemyAlert.periodic_enemy_check()



# Llamar a la función principal asincrónica
asyncio.run(main())