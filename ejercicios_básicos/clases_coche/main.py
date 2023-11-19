class Vehiculo():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    
    def __str__(self):
        return f"el coche de la marca {self.marca} tiene un color {self.color}"
    
class vehiculo_Mas(Vehiculo):
    def __init__(self, marca, color, potencia, numero_puertas):
        Vehiculo.__init__(self, marca, color)
        self.potencia = potencia
        self.numero_puertas = numero_puertas
        
    def __str__(self):
        return Vehiculo.__str__(self) + f", también tiene una potencia de {self.potencia} km/h y tiene {self.numero_puertas} puertas"
        
    
nuevo_coche = Vehiculo('ferrari', 'rojo')
print(nuevo_coche)
print("--------------------------------------------")
nuevo_coche2 = vehiculo_Mas('BMW', 'azul', '250', '4')
print(nuevo_coche2)