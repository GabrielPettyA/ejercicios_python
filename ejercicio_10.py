## INVIRTIENDO UNA CADENA DE TEXTO ##

cadena_text = 'Invertir'

invertir_text = cadena_text[:: -1]

print("Texto invertido: ", invertir_text)

# Ahora generamos una nueva variable para guardar el texto invertido y volver a dejarlo como al comienzo con un nuevo llamado a invertir.
new_cad_text = invertir_text

new_invertir_text = new_cad_text[:: -1]

print("Texto invertido: ", new_invertir_text)
