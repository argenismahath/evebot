import asyncio
import keyboard
import time
import comeToAnomalie

Shield = False

# Resto del código...

async def powerShield():
    keyboard.press("1")
    time.sleep(0.1)
    keyboard.release("1")
    # time.sleep(.9)
    keyboard.press("2")
    time.sleep(0.1)
    keyboard.release("2")

async def PowerWeapons():
    keyboard.press("a")
    keyboard.release("a")
    keyboard.press("d")
    keyboard.release("d")
    keyboard.press("t")
    keyboard.release("t")

async def powerredific():
    keyboard.press("r")
    time.sleep(0.5)
    keyboard.release("r")
    keyboard.press("f")
    time.sleep(0.5)
    keyboard.release("f")

async def powerShieldReparer():
    keyboard.press("3")
    time.sleep(0.5)
    keyboard.release("3")

async def startFight():
    if not Shield:
        await powerShield()
    time.sleep(.9)
    await PowerWeapons()

async def activar_comeToAnomalie():
    while True:
        # Usar await para obtener el valor real de la similitud
        next= await comeToAnomalie.abegingScannerFight()
        print("********************")
        print(next)
        print("********************")

        if next:
            startFight()
            print("activar armas")
        await asyncio.sleep(10)

    
