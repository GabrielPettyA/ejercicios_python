
'''
SE SOLICITA UNA LONGITUD PARA QUE EL SISTEMA
GENERE UNA CLAVE AUTOMÁTICA CON VALORES SELECCIONADOS
POR EL PROPIO SISTEMA
'''

# Primero se importan 'random' para las elecciones automáticas por el sistema.
import random
# También se importa 'string' para verificar las cadenas utilizadas automáticamente.
import string as str 

# Inicio de la función.
def clave_auto():
  
  # Se determina que tipos de datos queremos en nuestras claves y los volcamos en la variable 'valores'.
  valores = str.ascii_letters + str.digits + str.ascii_uppercase + str.ascii_lowercase
  
  # Se solicita al usuario el ingreso de la cantidad de valores que formará la clave.
  longitud = int(input("Ingrese longitud de clave: "))
  
  '''
  Con " ".join - logramos unir los valores que vamos a obtener automáticamente
  mediante --> random.choice(valores) el cual nos devuelve los valores de la
  secuencia que emos pasado como argumento.
  Por último con el bucle 'for' logramos determinar que longitud debe manejar
  el sistema antes de arrojar nuestra clave.
  '''
  clave = " ".join(random.choice(valores) for index in range(longitud))
  
  # Imprimimos la clave obtenida en la variable 'clave'.
  print(f'''
        -------------------------------
        La clave generada es:
                            
                    {clave}
        -------------------------------
        ''')

# Llamamos a la función.
clave_auto()

# Fin de función


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# Otra forma de hacerlo es utilizando los boolean.

def other_clave_auto():
  
  valore = str.ascii_letters + str.digits + str.ascii_uppercase + str.ascii_lowercase
  
  long = 8
  if long > 0:
    cont = True
    clave2 = " ".join(random.choice(valore) for index in range(long))
    
    if cont:
      print(f'''
      -------------------------------
      La clave:
                          
                  {clave2}
      -------------------------------
      ''')

  else:
    cont = False
    print("ERROR: falta ingresar longitud de clave.")

other_clave_auto()



