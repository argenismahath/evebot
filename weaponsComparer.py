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

    promedio_similitud = total_similitud / len(otras_imagenes)
    return promedio_similitud

async def calcWeaponOn(imagen_Take, otras_imagenes):
    promedio_similitud = await calcular_promedio_similitud(imagen_Take, otras_imagenes)
    print(f"Promedio de similitud al encender el arma: {promedio_similitud}")
    return promedio_similitud

async def calWeaponOff(imagen_Take, otras_imagenes):
    promedio_similitud = await calcular_promedio_similitud(imagen_Take, otras_imagenes)
    print(f"Promedio de similitud al apagar el arma: {promedio_similitud}")
    return promedio_similitud

# Rutas de las imágenes a comparar
imagen_Take = "weapons.png"

imagenesOff = [
    "WeaponOff/weapons1.png",
    "WeaponOff/weapons2.png",
    "WeaponOff/weapons3.png",
    "WeaponOff/weapons4.png",
    "WeaponOff/weapons5.png",
    "WeaponOff/weapons6.png",
    "WeaponOff/weapons7.png",
    "WeaponOff/weapons8.png",
    "WeaponOff/weapons9.png",
    "WeaponOff/weapons10.png",
    "WeaponOff/weapons11.png",
    "WeaponOff/weapons12.png",
    "WeaponOff/weapons13.png",
    "WeaponOff/weapons14.png",
    "WeaponOff/weapons15.png",
]

imagenesOn = [
    "WeaponOn/weapons1.png",
    "WeaponOn/weapons2.png",
    "WeaponOn/weapons3.png",
    "WeaponOn/weapons4.png",
    "WeaponOn/weapons5.png",
    "WeaponOn/weapons6.png",
    "WeaponOn/weapons7.png",
    "WeaponOn/weapons8.png",
    "WeaponOn/weapons9.png",
    "WeaponOn/weapons10.png",
    "WeaponOn/weapons10.png",
    "WeaponOn/weapons11.png",
    "WeaponOn/weapons12.png",
    "WeaponOn/weapons13.png",
    "WeaponOn/weapons14.png",
    "WeaponOn/weapons15.png",
]

async def main():
    probabilitie1= await calcWeaponOn(imagen_Take, imagenesOn)
    probabilitie2=await calWeaponOff(imagen_Take, imagenesOff)
    if probabilitie1>probabilitie2:
        return True
    else:
        return False
    
# Ejecutar el código asincrónico
asyncio.run(main())
