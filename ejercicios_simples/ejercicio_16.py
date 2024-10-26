
## EJERCICIO DE FIBONACCI ##

'''
a, b = 0, 1
a, b = b, a+b
=> a=b and b=a+b
'''

def my_fib(num):
  a, b = 0, 1
  while a < num:
    print(a, end=" ")
    a, b = b, a+b

my_fib(300)


# Otra forma de hacer FIBONACCI guardando resultados en lista

list_bibonacci = []
def new_fibonacci(num):
  a, b = 0, 1
  while a < num:
    list_bibonacci.append(a)
    a, b = b, a+b

new_fibonacci(300)
print(f'''
      Resultado de listado Fibonacci
      {list_bibonacci}
      ''')

# Otra manera es ingresando el valor a ser analizado por el sistema Fibonacci


list_par_fib = []
list_imp_fib = []
other_list_fib = []
def other_fib(n):
  a, b = 0, 1
  while a < n:
    other_list_fib.append(a)
    a, b = b, a+b



  
  for index in other_list_fib:
    if index % 2 == 0:
      list_par_fib.append(index)
      
    else:
      list_imp_fib.append(index)

  print("IMPAR: ", list_imp_fib)
  print("PAR: ", list_par_fib)

valor_ingresado = int(input("Ingrese valor: "))

other_fib(valor_ingresado)
print("Result Total: ", other_list_fib)
list_concat = print("Concatenando: ", list_par_fib + list_imp_fib)
