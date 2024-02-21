class Animal:
    def __init__(self,cant_patas, tipo):
        self.cant_patas = cant_patas
        self.tipo = tipo
    def moverse(self):
        pass
    
class Perro(Animal):
    def __init__(self, cant_patas, tipo, nombre, raza):
        super().__init__(cant_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    def moverse(self):
        return "Estoy caminando"
    
class Aguila(Animal):
    def __init__(self, cant_patas, tipo):
        super().__init__(cant_patas, tipo)
    def moverse(self):
        return "Estoy volando"

perro1 = Perro(4, "vertebrado", "Coqui", "dalmata")

print("Nombre:", perro1.nombre)
