import cv2
import pytesseract
from PIL import Image
# import PhotoTaker

# Configurar el comando de Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Definir una función para reemplazar letras similares a números
def reemplazar_similares(texto):
    replacements = {
        'o': '0',
        'O': '0',
        's': '5',
        'S': '5',
        'l': '1',
        'L': '1',
        'i': '1',
        'z':'2'
        # Agrega más reemplazos según sea necesario
    }
    
    for char, replacement in replacements.items():
        texto = texto.replace(char, replacement)
    
    return texto

def extraer_texto_de_imagen(nombre_imagen):
    img = cv2.imread(nombre_imagen, cv2.IMREAD_GRAYSCALE)
    
    # Aplicar un filtro de umbralización para resaltar los números
    _, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

    # Obtener el texto (números) de la imagen usando Tesseract OCR
    resultado = pytesseract.image_to_string(Image.fromarray(img_bin), config='--psm 6 outputbase digits')
    
    print(resultado)
    # Reemplazar letras similares a números
    resultado_corregido = reemplazar_similares(resultado)
    
    return resultado_corregido

def main():
    # Ruta de la imagen de la que quieres extraer el texto
    nombre_imagen = "imagen_modificada.png"

    

    # # Cargar la imagen
    # imagen = cv2.imread('imagen_modificada.png')
    # # Puntos de inicio y fin de la línea
    # x1, y1 = 303, 0
    # x2, y2 = 303, 100

    # # Color de la línea en formato BGR (azul, verde, rojo)
    # color = (0, 0, 255)  # Rojo

    # # Grosor de la línea
    # grosor = 40

    # # Dibujar la línea en la imagen
    # imagen_con_linea = cv2.line(imagen, (x1, y1), (x2, y2), color, grosor)

    # # Guardar la imagen editada
    # cv2.imwrite('captura_agrandada.png', imagen_con_linea)

    # Obtener el texto de la imagen y reemplazar letras similares a números
    texto_extraido = extraer_texto_de_imagen(nombre_imagen)

    # Imprimir el resultado
    print("Texto extraído de la imagen:")
    print(texto_extraido)
main()