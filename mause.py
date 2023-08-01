import pyautogui
import time

def moveMause(left, top, distance):
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

    #impulsar
    pyautogui.dragTo(nueva_x-350, nueva_y+100, duration=1.0)

    #320 = 19
    #325 = 22km
    #330 =26km
    # 350= 37km
    # 360= 41km
    # 370= 45km?
    # 390= 55km
    # 420= 69km
    # 430= 76km
    # 440= 80km
    # 450= 84km
    # 480 = 100km
    time.sleep(2)

    # Soltar el botón del mouse
    pyautogui.mouseUp()

    time.sleep(20)

    # pyautogui.click(855, 490)
    
def targering(x, y):
    #mover el mause 
    pyautogui.moveTo(x, y, duration=1)

    #click
    pyautogui.click(x, y)


def dock():
    #mover el mause to open menu
    pyautogui.moveTo(1193, 29, duration=.5)
    pyautogui.click(1193, 29)

    #mover el mause y dar click a la opcion de base
    pyautogui.moveTo(1236, 141, duration=.5)
    pyautogui.click(1236, 141)

    time.sleep(2)
    #mover y dar click en estacion (citadel) 
    pyautogui.moveTo(1259, 92, duration=.5)
    pyautogui.click(1259, 92)

    #mover y acoplar
    pyautogui.moveTo(959, 103, duration=.5)
    pyautogui.click(959, 103)

def unDock():
    print("undocking")

    #mover el mause y desacoplar
    pyautogui.moveTo(1236, 259)
    pyautogui.click()

