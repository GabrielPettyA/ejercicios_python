
'''
TAMBIÉN SE PUEDE UTILIZAR NUEVAMENTE LA ESTRUCTURA
FIBONACCI PARA OBTENER LOS MÚLTIPLOS DE LOS NÚMEROS 
QUE GENERA AUTOMÁTICAMENTE LA PROPIA MULTIPLICACIÓN INICIANDO, EN ESTE CASO, POR EL NÚMERO PAR '2'.
'''

list = []

def multiplo_auto(n1):
  a, b = 0, 1
  while a < n1:
    a, b = b, a*2 # Se puede utilizar cualquier multiplicador superior a 1 (ejemplo: 1.01 etc.)
    if a != 0 and a != b and a != 1:
      list.append(a)
    else:
      pass

rango = int(input("Ingrese Rango: "))
multiplo_auto(rango) # Se llama a la función y se pasa la variable que guarda el rango seleccionado.

list.pop(-1) # Se elimina de la lista el último valor que queda por fuera del rango seleccionado.

print("La multiplicación generada es:\n", list)



