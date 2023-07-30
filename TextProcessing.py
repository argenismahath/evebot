import json

def textProcessing(text):
    text = text.strip()  # Eliminar espacios en blanco al inicio y al final del texto
    print("text: ", text.replace("\n", " "))
    ruta_archivo = "data/json.json"
    with open(ruta_archivo, "r") as archivo:
        datos = json.load(archivo)

    if datos["Anomalia"] == text.replace("\n", " "):
        return True
    else:
        return False