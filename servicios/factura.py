import json
from datetime import datetime

class Factura:

    @staticmethod
    def generar(nombre_cliente, carrito, archivo):
        data = {
            "cliente": nombre_cliente,
            "fecha": str(datetime.now()),
            "items": [],
            "total": carrito.total()
        }

        for i in carrito.items:
            data["items"].append({
                "nombre": i["juego"].nombre,
                "cantidad": i["cantidad"],
                "precio": i["juego"].precio
            })

        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
