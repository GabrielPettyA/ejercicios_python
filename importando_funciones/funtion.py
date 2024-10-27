
## Generación de la clase con sus funciones
class Person():
  def __init__(self, name, last_name, age, height, profession):
    self.name = name
    self.last_name = last_name
    self.age = age
    self.height = height
    self.profession = profession
  
  ## En esta función se pasa la estructura del print solicitado y con los datos pasados desde 'import_funtion.py'
  def __str__(self):
    espacio = '-'*22
    print = (f'''
            {espacio}
             nombre   : {self.name}, 
             apellido : {self.last_name}, 
             edad     : {self.age}, 
             altura   : {self.height}, 
             profesión: {self.profession}
    ''')
    return print

'''
TAMBIÉN SE PUEDE UTILIZAR EN 'def __str__(self):' de la siguiente forma...
def __str__(self):
  return super().__str__() + "Aca va texto {}, otro texto {}
  etc, etc".format(self.ejemplo, self.ejemplo......)
  
QUEDARÍA:
return super().__str__() + "nombre: {}, apellido: {}, edad: {}, altura: {}, profesión: {}".format(self.name, self.last_name, self.age, self.height, self.profession)


return "nombre: {}, apellido: {}, edad: {}, altura: {}, profesión: {}".format(self.name, self.last_name, self.age, self.height, self.profession)
'''


