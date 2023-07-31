from PIL import ImageGrab
import time

values = {1: 0, 2: 72, 3: 144, 4: 216, 5:288}

def takePhoto(number):
        #posicion de la primera captura
    left = 1192

        #inicia desde la primera anomalia
    top = 60

    top= top+values[number]

    # Ancho y alto del área a capturar
    width = 100
    height = 70

    # Captura de pantalla del área específica
    screenshot = ImageGrab.grab(bbox=(left, top, left + width, top + height))

    # Guardar la captura de pantalla en un archivo
    nombre_archivo = "captura.png"
    screenshot.save(nombre_archivo)



    # Mostrar la ruta del archivo donde se guardó la captura de pantalla
    print(f"Captura de pantalla guardada en: {nombre_archivo}")

photoCounter=0

def target():
    #posicion de la  captura de target
    X,Y=820, 455
        
    # Ancho y alto del área a capturar
    width = 65
    height = 65

    # Captura de pantalla del área específica
    screenshot = ImageGrab.grab(bbox=(X, Y, X + width, Y + height))

    # Guardar la captura de pantalla en un archivo
    nombre_archivo = f"captura1.png"
    screenshot.save(nombre_archivo)

    print(f"Captura de pantalla guardada en: {nombre_archivo}")

def enemiesCheck():
    X=130
    Y=575

    width = 200
    height = 55

    screenshot = ImageGrab.grab(bbox=(X, Y, X + width, Y + height))
    nombre_archivo = f"Enemies.png"
    screenshot.save(nombre_archivo)
    print(f"Captura de pantalla guardada en: {nombre_archivo}")

# takePhoto()
# # target()
# enemiesCheck()
# time.sleep(10)
# top=top+72
# takePhoto()

#alto de los iconos de anomalias 
# X=1256, Y=269
# Posición del cursor: X=1266, Y=339