import cv2
import pytesseract
from PIL import Image
import PhotoTaker
import time
import asyncio

# Configurar el comando de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
lastShield=100
async def procesar_imagen():
    global lastShield
    try:
        PhotoTaker.Capacitor()
        # Cargar la imagen en escala de grises
        # img = cv2.imread("Capacitor/Capacitor.png", cv2.IMREAD_GRAYSCALE)
        img = cv2.imread("Capacitor/Capacito_upgrade.png", cv2.IMREAD_GRAYSCALE)

        # Aplicar un filtro de umbralización para resaltar los números
        _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

        # Obtener el texto (números) de la imagen usando Tesseract OCR
        resultado = pytesseract.image_to_string(Image.fromarray(img), config='--psm 6 outputbase digits')

        # Filtrar solo los dígitos
        numeros = ''.join(filter(str.isdigit, resultado))

        numero_entero = int(numeros)
        print("capacitor ", numero_entero)

        if numero_entero<60:
            print("encender escudo reparador")
            return True
        elif numero_entero>60 and numero_entero<80:
            print("mantener encendido el escudo")
            return True
        else:
            print("esta seguro")
            return False
        
        return numero_entero

    except Exception as e:
        # Manejo de errores: si ocurre alguna excepción, se imprimirá el mensaje de error
        print(f"Error al procesar la imagen: {e}")
        return None

# for _ in range(15):
#     asyncio.run(procesar_imagen())
#     time.sleep(15)
