
## EJERCICIO FIBONACCI ##

# Se toman dos valores y se realiza una continuidad de valores sumando los dos anterioores.

## Del 0 al 100 debería mostrar los siguientes números: 0 1 1 2 3 5 8 13 21 34 55 89 ##

def my_fibonacci(num):
  '''
  a, b = 0, 1
  a = b
  b = a+b
  '''
  
  a, b = 0, 1
  while a < num:
    print(a, end=" ") # En este caso solo imprime los valores.
    a, b = b, a+b

my_fibonacci(100)


## OTRA FORMA DE HACERLO ES CREANDO E IMPRIMIENDO UNA LISTA CON LOS VALORES

def new_fibonacci(n):
  list_fibnacci = []
  
  a, b = 0, 1
  
  while a < n:
    list_fibnacci.append(a) # En este caso se guardan los valores en una lista.
    a, b = b, a+b
  
  print("\nResultado Lista: ", list_fibnacci)
  

new_fibonacci(100)


## OTRA FORMA SERÍA AGREGANDO EL RANGO A RECORRER SEGÚN LO DESEE EL USUARIO

def new_fib(n):
  list_fib = []
  
  a, b = 0, 1
  
  while a < n:
    list_fib.append(a)
    a, b = b, a+b    
  
  print("\nResultado Lista: ", list_fib)
  
rango = int(input("Ingrese rango: "))
new_fib(rango)

'''
También se puede poner la lista por fuera de la función:
list_fib = []
def new_fib(n):
    etc.
    etc...

En lo personal, si solo será utilizada por una función determinada,
es mejor ubicarla dentro de la misma, salvo que querams imprimirla
fuera de la función.
'''

## COMO MUESTRO LOS VALORES OBTENIDOS DESDE LAS VARIABLES ? ##

'''
Primero debes recordar que python va a tomar un valor más
del rango que estableces, por lo que tienes que considerar que
al pasarle el valor de "a" y "b", el segundo es el más alto, por
lo tanto debes restarle al último valor de "b" el último valor 
de "a" obteniendo así los valores correspondientes al rango que 
solicitaste como se puede ver en el ejemplo a continuación.
'''
def b_fib(n):

  list_b = []
  
  a, b = 0, 1
  
  while a < n:
    a, b = b, a+b
    
    # Imprimimos valor b - a = resultado
    print(f'''
          Valor "b" {b} restando valor "a" {a} = {b-a}
          '''
          )
    # guardamos en lista para mostrarlo ordenado
    resta = b-a
    list_b.append(resta)
    
  print("\nResultado Lista 'b': ", list_b)

  
rango = int(input("Ingrese rango: "))
b_fib(rango)




import math
def a_fib(n):

  list_b = []
  
  a, b = 0, 1
  
  while a < n:
    a, b = b, a+b
    
    # Imprimimos valor b - a = resultado
    print(f'''
          Valor "a" {a} restando valor "b" {b} = {a-b}
          '''
          )
    # guardamos en lista para mostrarlo ordenado
    resta = a-b
    result = resta * -1 # Recuerda que los valores te van a dar en negativo, por eso debes multiplicarlo con '-1' pasandolos así a positivo.

    list_b.append(result)
    
  print("\nResultado Lista 'a': ", list_b)

  
rango = int(input("Ingrese otro rango: "))
a_fib(rango)
  