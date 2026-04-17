class VideoJuego:
    def __init__(self, id, nombre, categoria, precio, esrb, stock, consola):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._esrb = esrb
        self._stock = stock
        self._consola = consola

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    def reducir_stock(self, cantidad):
        if cantidad > self._stock:
            raise Exception("Stock insuficiente")
        self._stock -= cantidad

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "categoria": self._categoria,
            "precio": self._precio,
            "esrb": self._esrb,
            "stock": self._stock,
            "consola": self._consola
        }


class JuegoPS5(VideoJuego):
    pass


class JuegoXbox(VideoJuego):
    pass


class JuegoNintendo(VideoJuego):
    pass
