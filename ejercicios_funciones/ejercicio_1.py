## DEFINIR UNA FUNCIÓN QUE TOME DOS O MÁS ARGUMENTOS Y QUE DEVUELVA EL MAYOR DE ELLOS ##

def argumento_max(num1:int, num2:int, num3:int):

## Se realiza un resumen del ejercicio a desarrollar.

  """Se retorna el mayor de los tres números ingresados.

  Args:
      num1 (int): primer número ingresado
      num2 (int): segundo número ingresado
      num3 (int): tercer número ingresado
  Returns:
      int: Mayor de los números
  """
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num3 and num2 > num1:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  elif num1 == num2 or num2 == num3 or num3 == num1:
    print("Error: algo salio mal.\nLos números no pueden ser iguales.")
    exit()
  else:
    raise Exception("ERROR: proceso fallido")
  exit()

    


# Aprovechamos a utilizar lo visto en los ejercicios simples, como es la función '.format()'
mayor = argumento_max(15,12,10)
print("El número mayor es ==> {}".format(mayor))



'''
=================================================================
   También se le puede pedir al usuario que ingrese los números
'''


def other_max(num1:int, num2:int, num3:int):

## Se realiza un resumen del ejercicio a desarrollar.

  """Se retorna el mayor de los tres números ingresados.

  Args:
      num1 (int): primer número ingresado por usuario
      num2 (int): segundo número ingresado por usuario
      num3 (int): tercer número ingresado por usuario
  Returns:
      int: Mayor de los números
  """
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num3 and num2 > num1:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  elif num1 == num2 or num2 == num3 or num3 == num1:
    print("Error: algo salio mal.\nLos números no pueden ser iguales.")
    exit()
  else:
    raise Exception("ERROR: proceso fallido")
  exit()

primero = int(input("Ingrese Primer número:"))
segundo = int(input("Ingrese Segundo número:"))
tercero = int(input("Ingrese Tercer número:"))

# Aprovechamos a utilizar lo visto en los ejercicios simples, como es la función '.format()'
mayor = other_max(primero,segundo,tercero)
print("El número mayor es el ==> {}".format(mayor))



'''
=================================================================
   Otra forma de resolverlo pero más reducido
'''

def argument_num(num1:int, num2:int, num3:int):

## Se realiza un resumen del ejercicio a desarrollar.

  """Se retorna el mayor de los tres números ingresados.

  Args:
      num1 (int): primer número ingresado por usuario
      num2 (int): segundo número ingresado por usuario
      num3 (int): tercer número ingresado por usuario
  Returns:
      int: Mayor de los números
  dado que...
            a > b && a > c
            b > c && b > a
            c > a && c > b
  
  """
  if num1 != num2 and num2 != num3 and num3 != num1:
    if num1 > num2 and num1 > num3:
      return num1
    elif num2 > num1 and num2 > num3:
      return num2
    elif num3 > num2 and num3 > num1:
      return num3
  else:
    pass
  raise Exception("\nError: para operar no puede haber números repetidos") # Capturando el Error.
  



may = argument_num(10,6,1)
print("El número mayor es: {}".format(may))