import asyncio
import PhotoTaker
import imageComparer

async def escanear():
        # Toma captura del escáner
        PhotoTaker.target()

        # Se encarga de dar click y obtiene la similitud
        similitud = imageComparer.cal_image()
        print("Temporizador: Se ejecutó la función.")

        # Definir el intervalo de tiempo (en segundos) para llamar nuevamente la función
        intervalo = 5

        # Esperar durante el intervalo de tiempo antes de llamar a la función nuevamente
        await asyncio.sleep(intervalo)
        return similitud

async def abegingScanner():
    for _ in range(10):
        similitud = await escanear()
        print(similitud)
        print("similitud*********")

        if similitud:
            return similitud

async def abegingScannerFight():
    similitud = await escanear()
    print(similitud)
    print("similitud*********")

    if similitud:
        return similitud
