

class Vehiculo():
  def __init__(self, color, velocidad, estado, motor) -> None:
    self.color = color
    self.velocidad = velocidad
    self.estado = estado
    self.motor = motor
  
  def __str__(self) -> str:
    return "Vehículo de color {} que alcanza una velocidad de {}kms/hs, su estado es {} y tiene un motor {}".format(self.color, self.velocidad, self.estado, self.motor)


class Avion(Vehiculo):
  def __init__(self, color, velocidad, estado, motor, pasajeros, altitud, ventanas) -> None:
    super().__init__(color, velocidad, estado, motor)
    self.pasajeros = pasajeros
    self.altitud = altitud
    self.ventanas = ventanas
  
  def __str__(self) -> str:
    return "Avión de color {}, que alcanza una velocidad de {}kms/hs, su estado es {} con un motor {}, capacidad de pasajeros {}, llega a una altitud de {} mts. y posee {} ventanas.".format(self.color, self.velocidad, self.estado, self.motor, self.pasajeros, self.altitud, self.ventanas)


print(Vehiculo('verde', 350, 'usado', 'V8'))

secon_print = Avion('rojo', 700, 'nuevo', 'Boeing 747', 6, 10.000, 8)
print(secon_print)