import restaurante
from POO.restaurante import cliente


def encarregar_camarero(self)
    if self.mesa == 'ocupada':
        llamar_camarero()
    pass

restaurante.Mesa.encarregar_camarero = encarregar_camarero()

class Camarero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponibilidad = 'libre'
        self.mesa_encarregada = None

    def verificar_disponibilidad(self):
        if self.disponibilidad == 'libre':
            return True
        return False

    def llamar_camarero(self):
        if self.disponibilidad == 'libre':
            self.disponibilidad = 'ocupada'
            self.mesa_encarregada = cliente.mesa_asignada

    def liberar_camarero(self):
        if self.disponibilidad and self.mesa_encarregada == 'ocupada' and cliente.mesa_asignada:
            self.disponibilidad = 'libre'
            self.mesa_encarregada = None