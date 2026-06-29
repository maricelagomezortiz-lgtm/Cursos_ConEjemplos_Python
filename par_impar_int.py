# Interactivo
# Cambio de tipo ya que la funcion input nos devuelve una cadena de texto

numero = int(input("Dame un número:"))

if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")