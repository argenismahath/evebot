import cv2
import pytesseract
from PIL import Image
import PhotoTaker

# Configurar el comando de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
lastShield=100
async def procesar_imagen():
    global lastShield
    try:
        PhotoTaker.Capacitor()
        # Cargar la imagen en escala de grises
        img = cv2.imread("Capacitor/Capacitor.png", cv2.IMREAD_GRAYSCALE)

        # Aplicar un filtro de umbralización para resaltar los números
        _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

        # Obtener el texto (números) de la imagen usando Tesseract OCR
        resultado = pytesseract.image_to_string(Image.fromarray(img_bin), config='--psm 6 outputbase digits')

        # Filtrar solo los dígitos
        numeros = ''.join(filter(str.isdigit, resultado))

        numero_entero = int(numeros)
        if lastShield-numero_entero>40:
            print("seguro error de lectura")
            return 100
        lastShield=numero_entero
        print(numero_entero)
        return numero_entero

    except Exception as e:
        # Manejo de errores: si ocurre alguna excepción, se imprimirá el mensaje de error
        print(f"Error al procesar la imagen: {e}")
        return None