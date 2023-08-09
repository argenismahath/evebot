from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage import io, color
import asyncio

async def calcular_similitud_imagenes(imagen1, imagen2):
    # Leer las imágenes y convertirlas a escala de grises
    img1 = io.imread(imagen1)
    img2 = io.imread(imagen2)
    img1_gray = color.rgb2gray(img1)
    img2_gray = color.rgb2gray(img2)

    # Calcular el SSIM entre las imágenes con el tamaño de ventana específico y data_range
    similitud = compare_ssim(img1_gray, img2_gray, data_range=img1_gray.max() - img1_gray.min())

    return similitud

async def calcular_promedio_similitud(imagen_Take, otras_imagenes):
    total_similitud = 0

    for imagen in otras_imagenes:
        similitud = await calcular_similitud_imagenes(imagen_Take, imagen)
        total_similitud += similitud

    promedio_similitud = total_similitud / len(imagenesReference)
    return promedio_similitud

async def calcShip(imagen_Take, imagenesReference):
    promedio_similitud = await calcular_promedio_similitud(imagen_Take, imagenesReference)
    print(f"Promedio de que hay nave enemigas: {promedio_similitud}")
    return promedio_similitud


# Rutas de las imágenes a comparar
imagen_Take = "ship/shipVoid.png"


imagenesReference = [
    "ship/shipCheck1.png",
    "ship/shipCheck2.png",
]

async def main():
    probabilitie=await calcShip(imagen_Take, imagenesReference)
    if probabilitie<0.10:
        return True
    else:
        return False
    
# Ejecutar el código asincrónico
# asyncio.run(main())
