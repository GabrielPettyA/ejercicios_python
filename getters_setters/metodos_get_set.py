
## SE GENERA LA CLASE CON SU CONSTRUCTOR PARA DETERMINAR LA INICIALIZACIÓN DE SUS ATRIBUTOS.

class MetodoGetSet:
  def __init__(self, owner_account, balance, coin_type) -> None:
    self.__owner_account = owner_account
    self.__balance = balance
    self.__coin_type = coin_type

## A continuación se emplea los métodos getters y setters para poder obtener los datos de las variables encapsuladas y poder modificarlos.

## Primero se emplea el método getters para disponer de la información de cada atributo.
  def get_owner_account(self):
    return self.__owner_account
  
  def get_balance(self):
    return self.__balance
  
  def get_coin_type(self):
    return self.__coin_type
  
  ## Ahora se llama al método setters para poder modificar los valores deseados de la clase MetodoGetSet
  def set_balance(self, new_balance):
    self.__balance = new_balance
  
  def set_coin_type(self, new_coin_type):
    self.__coin_type = new_coin_type
    
## Llamamos al objeto y le pasamos los parámetros.
datos = MetodoGetSet('Peralta, Agustina', 200000, 'Pesos')

## Imprimimos los valores pasados y obtenidos gracias al método getters
print(f'''
      IMPRESIÓN POR MÉTODO GETTERS
      ----------------------------
      Titular Cuenta   : {datos.get_owner_account()}
      Saldo Disponible : {datos.get_balance()}
      Tipo de Moneda   : {datos.get_coin_type()} 
      ''')

## Generamos los nuevos valores, en este caso de balance y coin_type, gracias al método setters.
datos.set_balance(10000)
datos.set_coin_type('Dolares')

## Imprimimos los nuevos valores generados gracias al método setters.
print(f'''
      CUENTA MODIFICADA POR METODO SETTERS E IMPRESA POR MÉTODO GETTERS
      -----------------------------------------------------------------
      Titular Cuenta   : {datos.get_owner_account()}
      Saldo Disponible : {datos.get_balance()}      <--- Modificado por setters
      Tipo de Moneda   : {datos.get_coin_type()}    <--- Modificado por setters
      ''')

