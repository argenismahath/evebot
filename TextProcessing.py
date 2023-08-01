import json
import re

def textProcessing(text):
    text= text.replace("\n", " ")
    text= text.replace("’", " ")
    text= text.replace("‘", " ")
    text= text.replace('"', " ")
    text = re.sub(r'\d+', ' ', text)
    text = text.strip()  # Eliminar espacios en blanco al inicio y al final del texto

    print(text)

    ruta_archivo = "data/json.json"
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)

    if datos["Anomalia"] == text.replace("\n", " "):
        return True
    else:
        return False