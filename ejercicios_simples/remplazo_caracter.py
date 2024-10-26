## REEMPLAZA UN CARÁCTER EN UNA CADENA ##

# Utilizamos '.replace()' para el remplazo del caracter deseado.
cadena = "python"
cambio_caract = cadena.replace("p", "P")

print("Resultado del cambio: ", cambio_caract)

# También se puede pedir el ingreso de la letra a cambiar al usuario.
ingreso = input("Ingrese Letra: ")
cambio_caract = cadena.replace("p", ingreso)

print("Resultado del cambio: ", cambio_caract)

