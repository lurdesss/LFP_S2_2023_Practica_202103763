class Inventario:
    def __init__(self, nombre, cantidad, precioUnitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario
        self.ubicacion = ubicacion
    
    def getNombre(self):
        return self.nombre
    def getCantidad(self):
        return self.cantidad
    def getPrecioUnitario(self):
        return self.precioUnitario
    def getUbicacion(self):
        return self.ubicacion
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

inv1 = Inventario('Arándanos', '150', 'BodegaA')
print(inv1.nombre)

class Cargar:
    def __init__(self, nombreC, cantidadC, ubicacionC):
        self.nombreC = nombreC
        self.cantidadC = cantidadC
        self.ubicacionC = ubicacionC
    
    