
## Generación de la clase padre para su posterior reutilización

class Vehiculo():
  def __init__(self, color, velocidad, estado, motor) -> None:
    self.color = color
    self.velocidad = velocidad
    self.estado = estado
    self.motor = motor
    
## Se utiliza el método __str__ para imprimir los resultados esperados
  def __str__(self) -> str:
    return "Vehículo de color {} que alcanza una velocidad de {}kms/hs, su estado es {} y tiene un motor {}".format(self.color, self.velocidad, self.estado, self.motor)


## Se crea una nueva clase la cual utiliza los atributos, mediante la herencia, de la clase Vehiculo

class Avion(Vehiculo):
  def __init__(self, color, velocidad, estado, motor, pasajeros, altitud, ventanas) -> None:
    ## Se llaman al constructor de la clase Vehiculo para poder utilizar sus atributos
    super().__init__(color, velocidad, estado, motor)
    ## Se puede llamar ('super().' o también con su nombre, 'Vehiculo.') recuerda agregar el punto entre la clase y su constructor.
    self.pasajeros = pasajeros
    self.altitud = altitud
    self.ventanas = ventanas

  def __str__(self) -> str:
    return "Avión de color {}, que alcanza una velocidad de {}kms/hs, su estado es {} con un motor {}, capacidad de pasajeros {}, llega a una altitud de {} mts. y posee {} ventanas.".format(self.color, self.velocidad, self.estado, self.motor, self.pasajeros, self.altitud, self.ventanas)

## Impresión directa de la clase y sus valores pasados directamente.
print(Vehiculo('verde', 350, 'usado', 'V8'))

## Impresión de la clase mediante una variable generada previamente para luego ser llamada para imprimir.
secon_print = Avion('rojo', 700, 'nuevo', 'Boeing 747', 6, 10.000, 8)
print(secon_print)