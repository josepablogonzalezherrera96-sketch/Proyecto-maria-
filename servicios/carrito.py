class Carrito:

    def __init__(self):
        self.items = []

    def agregar(self, juego, cantidad):
        if cantidad > juego.stock:
            raise Exception("No hay suficiente stock")

        juego.reducir_stock(cantidad)

        self.items.append({
            "juego": juego,
            "cantidad": cantidad
        })

    def eliminar(self, nombre):
        self.items = [i for i in self.items if i["juego"].nombre != nombre]

    def total(self):
        return sum(i["juego"].precio * i["cantidad"] for i in self.items)

    def mostrar(self):
        for i in self.items:
            print(f'{i["juego"].nombre} x{i["cantidad"]} = ${i["juego"].precio * i["cantidad"]}')
