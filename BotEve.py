import asyncio
import PhotoTaker
import datetime
import time
import mause
from pytesseract import *
from PIL import Image
import TextProcessing
import json
import comeToAnomalie
import fight



pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ruta_archivo = "data/json.json"

# Leer el archivo JSON
with open(ruta_archivo, "r") as archivo:
    datos = json.load(archivo)

def checkEnmies():
    #tomar la imagen del area de enemigos
    enemieDetecte=False
    while not enemieDetecte:
        result= PhotoTaker.enemiesCheck()
        if result[0] > 0 or result[1] > 0:
            print("hay enemigos a las ", datetime.datetime.now())
            print("no salir de la estacion XD")
            time.sleep(20)
        else:
            #Cambiar la variable para que se apage el bucle
            enemieDetecte=True
            #desacopla de la estacion si no hay enemigos
            mause.unDock()
            time.sleep(20)
            # mause.dock()

def checkAnomalies():
    counter=1
    while counter<6:
        # Toma la captura de pantalla y la guarda como captura.png
        PhotoTaker.takePhoto(counter)
        time.sleep(2.5)
        img = Image.open("captura.png")
        resultado = pytesseract.image_to_string(img)
        isAnomalie = TextProcessing.textProcessing(resultado)
        if isAnomalie:
            return counter

        counter=+1
    return False


async def main():
    checkEnmies()
    mause.openAnomalieMenu()
    result= checkAnomalies()
    if result!=False:
        #mueve e impulsa la nave al obbbjetivo
        mause.moveMause(1192, PhotoTaker.values[result], datos["Salto"])
        time.sleep(10)

        #empieza a detectar si ya se puede escanear
        comeToAnomalie.abegingScanner()
        await fight.startFight()
        

    
if __name__ == "__main__":
    asyncio.run(main())
# if __name__==main():
# 