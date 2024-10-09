## REALIZAR UNA MULTIPLICACIÓN ENTRE DOS O MÁS NÚMEROS Y MUESTRA EL RESULTADO ##

num_1 = 5
num_2 = 10

resultado_multiplicacion = num_1 * num_2

print("El resultado de la multiplicación es: ", resultado_multiplicacion)

# También se pueden agregar más números.
num_1 = 5
num_2 = 10
num_3 = 2
num_4 = 7

resul_mult_varios_num = num_1 * num_2 * num_3 * num_4

print(f'''
El resultado de la multiplicar más de dos números es: 
{resul_mult_varios_num}
''')

# Otra forma es ingresando mediante 'int' e 'input' los valores que queremos obtener.
num_1 = int(input("Ingrese primer número: "))
num_2 = int(input("Ingrese segundo número: "))

resul_mult_varios_num = num_1 * num_2

print(f'''
El resultado de múltiplicar
{num_1} con {num_2} es -> {resul_mult_varios_num}
''')
