import asyncio
import keyboard
import time
import comeToAnomalie
import weaponsComparer

Shield = False
Weapons=False
# Resto del código...

async def powerShield():
    global Shield
    keyboard.press("1")
    time.sleep(0.1)
    keyboard.release("1")
    # time.sleep(.9)
    keyboard.press("2")
    time.sleep(0.1)
    keyboard.release("2")
    Shield= not Shield

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
    global Weapons

    poweWeapons= await weaponsComparer.main()
    #si el escudo esta apaga
    #las armas estan apagadas
    #y visualemente esta las armas apaagadas, se encenderan las armas
    if Shield==False and Weapons==False and poweWeapons==False:
        await PowerWeapons()
        Weapons=True

    #si el escudo esta apagado se encenderá
    if Shield==False:
        await powerShield()
    
    #si visualmente las armas estan apaagadas
    #pero si en las variables esta encendido junto al escudo
    #se encenderan las armas
    if poweWeapons==False and Weapons and Shield:
        await PowerWeapons()
        Weapons=True


    time.sleep(.9)

async def activar_comeToAnomalie():
    while True:
        # Usar await para obtener el valor real de la similitud
        next= await comeToAnomalie.abegingScannerFight()
        print("********************")
        print(next)
        print("********************")

        if next:
            await startFight()
            print("activar armas")
        await asyncio.sleep(10)

    
