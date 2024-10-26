## CALCULAR EL AREA DE UN CIRCULO CON UN RADIO DETERMINADO ##

# En este caso empezamos a utilizar las librerías disponibles para python

import math

radio = 3
area = math.pi * radio ** 2 # con el '** 2' se eleva el valor al cuadrado

print("El área es -> ", area)

'''Otra forma de hacerlo es que el radio a determinar del area lo introduzca 
el usuario, para ello utilizamos "int" ya que nos referimos al ingreso de un
número y lo incorporamos a "input" para que lo podamos cargar al sistema.
'''
other_radio = int(input("Ingrese el número deseado: "))
new_area = math.pi * other_radio ** 2 # con el '** 2' se eleva el valor al cuadrado

print("El área que desea saber es: ", new_area)
