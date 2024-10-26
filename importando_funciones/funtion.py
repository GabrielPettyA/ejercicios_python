
## Generación de la clase con sus funciones
class Person():
  def __init__(self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age
  
  ## En esta función se pasa la estructura del print solicitado y con los datos pasados desde 'import_funtion.py'
  def __str__(self):
    return "nombre: {}, apellido: {}, edad: {}".format(self.name, self.last_name, self.age)



