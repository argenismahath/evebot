import time
import imageComparer
import PhotoTaker

# Función asincrónica que se ejecutará periódicamente
def escanear():
    #toma captura del escaner
    PhotoTaker.target()
    similitud= imageComparer.cal_image()
    print("Temporizador: Se ejecutó la función.")

    # Definir el intervalo de tiempo (en segundos) para llamar nuevamente la función
    intervalo = 5

    # Esperar durante el intervalo de tiempo antes de llamar a la función nuevamente
    time.sleep(intervalo)
    print(similitud)
    return similitud
   
def begingScanner():
    for _ in range(10):
        similitud= escanear()
        if similitud:
            break
