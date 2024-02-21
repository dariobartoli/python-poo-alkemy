class Bicicleta():
    def __init__(self, marca, rodado, precio, velocidad):
        self.marca = marca
        self.rodado = rodado
        self.precio = precio
        self.velocidad = velocidad
    
    def acelerar(self, velocidadEsperada):
        while(self.velocidad > velocidadEsperada):
            self.velocidad += 1
            print(f'acelerando {self.velocidad}')
        print("Velocidad alcanzada")

    def frenar(self):
        while(self.velocidad >0):
            self.velocidad -= 1
            print(f'bajando velocidad {self.velocidad}')
        print("Frenaste")


    def estado(self):
        print(f'Marca: {self.marca}')
        print(f'Rodado: {self.rodado}')
        print(f'Precio: {self.precio}')
        print(f'Velocidad: {self.velocidad}')

bicicleta1 = Bicicleta("Tomasseli", 29, 100000, 8)

bicicleta1.estado()
        