from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage import io, color
import mause
import PhotoTaker
import keyboard
import datetime
import pyautogui
import time
import asyncio

async def redimensionar_imagen(nombre_imagen, nuevo_ancho, nuevo_alto):
    # Abrir la imagen
    imagen = Image.open(nombre_imagen)

    # Redimensionar la imagen
    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

    # Guardar la imagen redimensionada
    nueva_ruta = f"imagen_redimensionada_{nuevo_ancho}x{nuevo_alto}.jpg"
    imagen_redimensionada.save(nueva_ruta)

    return nueva_ruta


enemy=False
async  def enemyCheck():
    global enemy

    result= PhotoTaker.enemiesCheck()
    if result[0] > 0 or result[1] > 0:
        print("hay enemigos :,V a las ", datetime.datetime.now())
        enemy=True
        print("ingresar a la estacion XD")
        mause.dock()
        time.sleep(20)
    else:
        enemy=False
    return enemy

counter =0

async def periodic_enemy_check():
    while counter < 1000:
        await asyncio.sleep(10)
        await enemyCheck()


# Iniciar el bucle de eventos de asyncio
# loop = asyncio.get_event_loop()
# Iniciar la función asincrónica que se ejecutará cada 10 segundos
# asyncio.ensure_future(periodic_enemy_check())

# Ejecutar el bucle de eventos para permitir que las tareas asincrónicas se ejecuten
# loop.run_forever()
# asyncio.run(enemyCheck())