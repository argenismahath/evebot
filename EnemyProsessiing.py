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
    
    print(resultado, "**")
    # Reemplazar letras similares a números
    resultado_corregido = reemplazar_similares(resultado)
    
    return resultado_corregido

def main():
    # Ruta de la imagen de la que quieres extraer el texto
    nombre_imagen = "imagen_modificada.png"

    texto_extraido = extraer_texto_de_imagen(nombre_imagen)
    texto_extraido = texto_extraido.replace("-", "")
    texto_extraido = texto_extraido.split()

    # Inicializar la variable result con un valor predeterminado
    result = [0, 0]

    # Asegurarse de que la lista tenga al menos dos elementos
    if len(texto_extraido) >= 2:
        # Verificar si el segundo elemento es None
        if texto_extraido[1] is None:
            texto_extraido[1] = '0'  # Cambiamos None por '0'
    
            # Actualizar la lista result con los dos primeros elementos
        result = [int(texto_extraido[0]), int(texto_extraido[1])]
    
    # Imprimir el resultado
    print("Texto extraído de la imagen:")
    print(result)
    return result