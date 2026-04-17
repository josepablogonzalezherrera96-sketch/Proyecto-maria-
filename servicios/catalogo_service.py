import json
import csv
from modelos.videojuego import *

class CatalogoService:

    @staticmethod
    def cargar_json(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            data = json.load(f)

        catalogo = []
        for j in data:
            catalogo.append(CatalogoService.crear_objeto(j))
        return catalogo

    @staticmethod
    def crear_objeto(j):
        if j["consola"] == "PS5":
            return JuegoPS5(**j)
        elif j["consola"] == "XBOX":
            return JuegoXbox(**j)
        else:
            return JuegoNintendo(**j)

    @staticmethod
    def guardar_json(ruta, catalogo):
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump([j.to_dict() for j in catalogo], f, indent=4)

    @staticmethod
    def agregar_juego(catalogo, juego):
        for j in catalogo:
            if j.id == juego.id:
                raise Exception("ID repetido")
        if juego.precio < 0 or juego.stock < 0:
            raise Exception("Datos inválidos")

        catalogo.append(juego)
