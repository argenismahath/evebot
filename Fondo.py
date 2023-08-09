import cv2
import numpy as np
import EnemyProsessiing

def change_BackGround():
    # Cargar la imagen
    imagen = cv2.imread('Enemies.png')

    # Colores específicos que deseas eliminar (en formato BGR)
    colores_a_eliminar = [(157, 162, 169), (255, 0, 0), (0, 255, 0)]  # Rojo, Azul y Verde

    # Umbral de diferencia de color
    umbral = 80

    # Crear una máscara para cada color a eliminar y combinarlas
    mascaras = [cv2.inRange(imagen, np.array(color) - umbral, np.array(color) + umbral) for color in colores_a_eliminar]
    mascara_combinada = np.logical_or.reduce(mascaras)

    # Invertir la máscara para seleccionar los colores que NO son los colores_a_eliminar
    mascara_invertida = np.logical_not(mascara_combinada)

    # Crear una imagen donde los colores a eliminar sean reemplazados por blanco
    imagen_modificada = np.copy(imagen)
    imagen_modificada[np.where(mascara_combinada)] = 255

    # Guardar la imagen modificada
    cv2.imwrite('imagen_modificada.png', imagen_modificada)
    EnemyProsessiing.main()