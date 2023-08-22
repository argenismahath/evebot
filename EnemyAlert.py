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
    # PhotoTaker.enemiesCheck()
    def calcular_similitud_imagenes(imagen1, imagen2, win_size=7):
            # Leer las imágenes y convertirlas a escala de grises
        img1 = io.imread(imagen1)
        img2 = io.imread(imagen2)
        img1_gray = color.rgb2gray(img1)
        img2_gray = color.rgb2gray(img2)

            # Calcular el SSIM entre las imágenes con el tamaño de ventana específico y data_range
        similitud = compare_ssim(img1_gray, img2_gray, win_size=win_size, data_range=img1_gray.max() - img1_gray.min())

        return similitud

        # PhotoTaker.target()

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
    # PhotoTaker.enemiesCheck()
    # time.sleep(2)
        # Ejemplo de uso:
    # nombre_imagen_original = "EnemiesClear.png"
    # nombre_imagen_comparar = "Enemies.png"

    # nuevo_ancho = 800
    # nuevo_alto = 600

    # ruta_imagen_redimensionada = await redimensionar_imagen(nombre_imagen_original, nuevo_ancho, nuevo_alto)
    # similitud = calcular_similitud_imagenes(nombre_imagen_original, nombre_imagen_comparar)

    # print(f"La imagen redimensionada se ha guardado en: {ruta_imagen_redimensionada}")
    # print(f"La similitud entre las imágenes es: {similitud}")
    print(enemy)
    # if(similitud<0.97 and enemy==False):
    #     print("ingresar a la estacion XD")
    #     enemy=True
    #     # mause.dock()
    #     time.sleep(20)

    # elif(similitud>0.98 and enemy==True):
    #     print("salir de la estacion XD")
    #     mause.unDock()
    #     enemy=False
    #     time.sleep(20)
    # print(similitud>98, enemy==True)

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