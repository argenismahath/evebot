from PIL import Image
import Fondo

def improveImgCapacitor( ):
    ruta_imagen="Capacitor/Capacitor.png"
    factor=2.0
    imagen_original = Image.open(ruta_imagen)
    ancho_original, alto_original = imagen_original.size
    ancho_nuevo = int(ancho_original * factor)
    alto_nuevo = int(alto_original * factor)
    imagen_ampliada = imagen_original.resize((ancho_nuevo, alto_nuevo), Image.ANTIALIAS)
    imagen_ampliada.save("Capacitor/Capacito_upgrade.png")  # Guarda la imagen ampliada en un archivo
    Fondo.change_BackGroundCapacitor()
    return imagen_ampliada


# imagen_ampliada = agrandar_imagen()
