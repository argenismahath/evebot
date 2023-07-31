from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage import io, color
import mause
import PhotoTaker
import keyboard
import pyautogui
import time

def redimensionar_imagen(nombre_imagen, nuevo_ancho, nuevo_alto):
    # Abrir la imagen
    imagen = Image.open(nombre_imagen)

    # Redimensionar la imagen
    imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

    # Guardar la imagen redimensionada
    nueva_ruta = f"imagen_redimensionada_{nuevo_ancho}x{nuevo_alto}.jpg"
    imagen_redimensionada.save(nueva_ruta)

    return nueva_ruta

def cal_image():
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
    time.sleep(2)
    # Ejemplo de uso:
    nombre_imagen_original = "captura0.png"
    nombre_imagen_comparar = "captura1.png"

    nuevo_ancho = 800
    nuevo_alto = 600

    ruta_imagen_redimensionada = redimensionar_imagen(nombre_imagen_original, nuevo_ancho, nuevo_alto)
    similitud = calcular_similitud_imagenes(nombre_imagen_original, nombre_imagen_comparar)

    print(f"La imagen redimensionada se ha guardado en: {ruta_imagen_redimensionada}")
    print(f"La similitud entre las imágenes es: {similitud}")
    if(similitud>=0.45):
        print("se targeteará")
        mause.targering(845, 475)

        #*************** C A M B I A R    A    A T A Q U E *********#
        time.sleep(1.5)
        tecla="b"
        keyboard.press(tecla)
        time.sleep(0.1)  # Esperar un tiempo (en segundos)
        keyboard.release(tecla)
        return True
    return False

def remove_alpha_channel(image_path):
    img = Image.open(image_path)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    return img

#revisa si esta o no en la base dockeado
def isInBase():
    time.sleep(3)
    captura = pyautogui.screenshot()
    captura.save("completeCap.png")

    # Eliminar el canal alfa de la imagen capturada antes de convertirla a escala de grises
    captura_rgb = remove_alpha_channel("completeCap.png")
    captura_rgb.save("completeCap_no_alpha.png")

    # Leer las imágenes y convertirlas a escala de grises
    img1 = io.imread("baseDock.png")
    img2 = io.imread("completeCap_no_alpha.png")

    if img1.shape[-1] == 4:  # Si la imagen tiene 4 canales (RGBA), conviértela a RGB
        img1 = color.rgba2rgb(img1)

    img1_gray = color.rgb2gray(img1)
    img2_gray = color.rgb2gray(img2)
    win_size = 7

    # Calcular el SSIM entre las imágenes con el tamaño de ventana específico y data_range
    similitud = compare_ssim(img1_gray, img2_gray, win_size=win_size, data_range=img1_gray.max() - img1_gray.min())

    return similitud

# if isInBase() > 0.9:
#     print("La imagen está en la base.")
# else:
#     print("La imagen no está en la base.")