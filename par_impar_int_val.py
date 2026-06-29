# Interactivo
# Cambio de tipo ya que la funcion input nos devuelve una cadena de texto

es_numero = True

while True:
    
    try:
        numero = int(input("Dame un número:"))
        es_numero = True
    except Exception as e:
        print("Valor Invalido")
        es_numero = False
        
    if es_numero:
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")        
        break
    
