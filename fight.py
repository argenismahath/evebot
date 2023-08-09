import asyncio
import keyboard
import time
import comeToAnomalie
import weaponsComparer
import PhotoTaker
import capacitorProsessing
import FinishFightReport
import mause
import EnemyAlert

Shield = False
Weapons=False
ShieldReparer=False

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
    time.sleep(0.1)
    keyboard.release("r")
    keyboard.press("f")
    time.sleep(0.1)
    keyboard.release("f")

async def powerShieldReparer():
    keyboard.press("3")
    time.sleep(0.1)
    keyboard.release("3")

async def startFight():
    global Weapons

    PhotoTaker.weapons()

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
    
    #revisar la imagen tomada
    probabilitie= await FinishFightReport.main()

    if probabilitie:
        mause.dock()
        # break

        #si visualmente las armas estan apaagadas
        #pero si en las variables esta encendido junto al escudo
        #se encenderan las armas
    if poweWeapons==False and Weapons and Shield:
        await PowerWeapons()
        Weapons=True    
    
    time.sleep(.9)
    await powerredific()

async def activar_comeToAnomalie():
    global ShieldReparer
    global Weapons
    global Shield


    while True:
        await EnemyAlert.enemyCheck()
        poweWeapons= await weaponsComparer.main()

        #Tomar foto del espacio
        PhotoTaker.ShipCheck()

        

        shieldDamage= await capacitorProsessing.procesar_imagen()
        
        if shieldDamage is not None:
            shieldDamage=shieldDamage
        else:
            shieldDamage=100
        
        if ShieldReparer and shieldDamage<70:
            ShieldReparer=True 
        elif shieldDamage<70 and ShieldReparer == False:
            ShieldReparer=True
            await powerShieldReparer()
        elif shieldDamage>80 and ShieldReparer:
            ShieldReparer=False
            await powerShieldReparer()

        # Usar await para obtener el valor real de la similitud
        next= await comeToAnomalie.abegingScannerFight()
        print("********************")
        print(next)
        print(ShieldReparer)
        print(shieldDamage)
        print("********************")

        if next:
            await startFight()
            print("activar armas")
        await asyncio.sleep(6)

    
