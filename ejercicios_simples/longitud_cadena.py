## CREAR UNA CADENA DE TEXTO Y MOSTRAR SU LONGITUD ##

cadena_texto = "Hola Mundo"

'''
Con decimos longitud nos referimos a la cantidad de caracteres 
que forman el string de la cadena de texto. 
Para lo que se utilizará la función 'len()', la cual nos cuenta
los caracteres existentes en nuestra cadena de texto incluyendo
los espacio entre cada palabra dejado entre cada palabra que 
forma la cadena.
'''
longitud_texto = len(cadena_texto)

# Aprovechamos el '.format()' para imprimir el resultado.
print("La longitud de la cadena de texto es: {}".format(longitud_texto))

