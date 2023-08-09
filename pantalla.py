import pyautogui
import cv2
import numpy as np
import EnemyProsessiing

# Dimensiones del área de la pantalla que deseas capturar
x = 45
y = 389
width = 230
height =70

# Captura de pantalla
screenshot = pyautogui.screenshot(region=(x, y, width, height))
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Redimensiona la captura para agrandarla
enlarged_screenshot = cv2.resize(screenshot, None, fx=2, fy=2)

# Guardar la captura agrandada en un archivo de imagen
cv2.imwrite('captura_agrandada.png', enlarged_screenshot)

EnemyProsessiing.main()