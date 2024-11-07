class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.estado = 'libre'

    def reservar(self):
        if self.estado == 'libre':
            self.estado = 'ocupada'
            return True
        return False

    def liberar(self):
        if self.estado == 'ocupada':
            self.estado = 'libre'
            return True
        return False

    def verificar_estado(self):
        return self.estado

class Pedido:
    def __init__(self):
        self.items = []
        self.estado = 'en perparacion'

    def agregar_item(self, item):
        self.items.append(item)

    def remover_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calcular_total(self):
        return sum(item.precio for item in self.items)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

class Menu:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, descripcion, precio):
        self.items.append(ItemMenu(nombre, descripcion, precio))

    def renover_item(self, nombre):
        self.items = [item for item in self.items if item.nombre != nombre]

    def mostrar_menu(self):
        for item in self.items:
            print(f'{item.nombre}:{item.descripcion} - {item.precio}€')

class ItemMenu:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesa_asignada = None
        self.pedido_actual = Pedido()

    def asignar_mesa(self, mesa):
        self.mesa_asignada = mesa

    def realizar_pedido(self, items):
        for item in items:
            self.pedido_actual.agregar_item(item)

    def ver_cuenta(self):
        total = self.pedido_actual.calcular_total()
        print(f'Total a pagar: {total}€')
        return total

class Restaurante:
    def __init__(self):
        self.mesas = []
        self.menu = Menu()
        self.clientes = []

    def anadir_mesa(self, numero, capacidad):
        self.mesas.append(Mesa(numero, capacidad))

    def remover_mesa(self, numero):
        self.mesas = [mesa for mesa in self.mesas if mesa.numero != numero]

    def mostrar_mesas_disponibles(self):
        for mesa in self.mesas:
            if mesa.verificar_estado() == 'libre':
                print(f'Mesa {mesa.numero} (Capacidad: {mesa.capacidad}) esta disponible.')

    def hacer_reserva(self, cliente, numero_mesa):
        for mesa in self.mesas:
            if mesa.numero == numero_mesa and mesa.reservar():
                cliente.asignar_mesa(mesa)
                self.clientes.append(cliente)
                print(f'Mesa {numero_mesa} reservada para {cliente.nombre}.')
                return True
        print(f'Mesa {numero_mesa} no esta disponible.')
        return False

    def gestionar_pedido(self, cliente, items):
        if cliente in self.clientes:
            cliente.realizar_pedido(items)
            print(f'Pedido realizado para {cliente.nombre}.')
        else:
            print('Cliente no registrado.')

    def mostrar_menu(self):
        self.menu.mostrar_menu()

    def escoger_items_del_menu(self, cliente):
        if cliente in self.clientes:
            self.mostrar_menu()
            items_seleccionados = []
            while True:
                item_nombre = input("Ingrese el nombre del item que desea (o 'fin' para terminar)")
                if item_nombre.lower() == 'fin':
                    break
                item_encontrado = next((item for item in self.menu.items if item.nombre.lower() == item_nombre), None)
                if item_encontrado:
                    items_seleccionados.append(item_encontrado)
                else:
                    print('Item no encontrado. Intente de nuevo.')
            self.gestionar_pedido(cliente, items_seleccionados)
        else:
            print('Cliente no registrado.')


    def mostrar_cuenta(self, cliente):
        if cliente in self.clientes:
            cliente.ver_cuenta()
        else:
            print('Cliente no registrado')

restaurante = Restaurante()
restaurante.anadir_mesa(1, 4)
restaurante.anadir_mesa(2, 2)

restaurante.menu.agregar_item('pizza', 'Deliciosa pizza picante', 10.0)
restaurante.menu.agregar_item('ensalada', 'Fresca ensalda verde', 7.0)

cliente = Cliente('Matteo')
restaurante.mostrar_mesas_disponibles()
restaurante.hacer_reserva(cliente, 1)
restaurante.mostrar_mesas_disponibles()
print('Menu:')
restaurante.escoger_items_del_menu(cliente)
restaurante.mostrar_cuenta(cliente)


