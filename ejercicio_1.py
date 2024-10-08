## SUMANDO DOS NÚMEROS Y MOSTRAR SU RESULTADO ##

num_1 = 2
num_2 = 10

resultado_suma = num_1 + num_2

# Una forma de realizar el print es...
print(resultado_suma)

# Otra forma agregando texto es...
print("La suma de ambos números es: ", resultado_suma)

# Otra forma es utilizando el método '.format'
print("La suma de {} y {} es igual a {}".format(num_1, num_2, resultado_suma))

# O también puedes utilizar el método f-string que sirve para dar formato a las cadenas de texto, permitiéndonos también, agregar llaves {}. 
# Utilizando las tres comillas podemos insertar un string con todas las líneas que deseemos.
print(f'''
RESULTADO DE LA OPERACIÓN:
      
       {num_1}
    +
       {num_2}
    --------
       {resultado_suma}
      
      ''')