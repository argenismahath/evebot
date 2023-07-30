import pyautogui
import time

def moveMause(left, top):
    # Obtener la posición actual del mouse
    x, y = left, top
    # Mover el mouse mientras mantiene presionado el botón izquierdo (arrastrar)
    nueva_x, nueva_y = x - 100, y + 100

    #mover para abrir el menu de warp
    pyautogui.moveTo(nueva_x+150, nueva_y, duration=1)

    # Hacer clic en la posición actual
    pyautogui.click(nueva_x+150, nueva_y)

    #ir a la pocicion de warp
    pyautogui.moveTo(nueva_x-180, nueva_y+100, duration=1)

    # Hacer clic en la posición actual
    # pyautogui.click(nueva_x-180, nueva_y+100)

#impulsar a 100
    pyautogui.dragTo(nueva_x-480, nueva_y+100, duration=1.0)

    # Soltar el botón del mouse
    pyautogui.mouseUp()

    time.sleep(20)

    pyautogui.click(855, 490)
    

# X=1191, Y=311
# Posición del cursor: X=957, Y=407

def targering(x, y):
    #mover el mause 
    pyautogui.moveTo(x, y, duration=1)

    #click
    pyautogui.click(x, y)
