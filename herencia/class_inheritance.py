
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

## Se agrega un nuevo objeto por herencia, utilizando los atributos de la clase padre.
class Moto(Vehiculo):
  def __init__(self, color, velocidad, estado, motor, ruedas, tipo) -> None:
    super().__init__(color, velocidad, estado, motor)
    self.ruedas = ruedas
    self.tipo = tipo
  
  def __str__(self) -> str:
    return "Moto de color {} que alcanza una velocidad de {}kms/hs, su estado es {}, consta de un motor {}, tiene {} ruedas y su modelo es {}.".format(self.color, self.velocidad, self.estado, self.motor, self.ruedas, self.tipo)
  
  

## Impresión directa de la clase y sus valores pasados directamente.
print(Vehiculo('verde', 350, 'usado', 'V8'))

## Impresión de la clase mediante una variable generada previamente para luego ser llamada para imprimir.
secon_print = Avion('rojo', 700, 'nuevo', 'Boeing 747', 6, 10.000, 8)
print(secon_print)

## En este caso se imprimen los valores mediante las diversas variables
# También se pueden ingresar los datos a través de la solicitud al usuario
color = input("Ingrese color: ")
velocidad = 500
estado = input("Ingrese estado de moto: ")
motor = 'brrtx2000'
ruedas = 2
modelo = '1500cc'
print(f'''
-------------------------------------------------------------------------------
  {Moto(color, velocidad, estado, motor, ruedas, modelo)}
-------------------------------------------------------------------------------
      ''')

''' 
RECUERDA QUE CUANDO UTILIZAMOS 'super().' NO SE UTILIZA EN EL CONSTRUCTOR 
DE LA CALSE QUE LO LLAMA 'self' PERO AL UTILIZAR EL NOMBRE DE LA CLASE, 
EN ESTE CASO 'Vehiculo().' EN EL CONSTRUCTOR CUANDO ES LLAMADO POR OTRA 
CLASE, SE DEBE UTILIZAR 'self'.

SIN ENVARGO, EN LOS CONSTRUCTORES DE TODAS LAS CLASES CORRESPONDIENTES
SI SE DEBE UTILIZAR 'self' YA QUE PERTENECE A CADA CONSTRUCTOR COMO SUS 
ATRIBUTOS CORRESPONDIENTES PARA PODER SER LLAMADOS Y UTILIZADOS EN EL 
CÓDIGO, HACIENDO REFERENCIA AL CONTENIDO DEL OBJETO CON EL QUE ESTÁ 
ASOCIADA.
'''

