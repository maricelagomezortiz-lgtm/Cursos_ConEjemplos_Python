# La suma de gauss establece que la suma de una 
# secuencia de números
# consecutiva de calcula multiplicando el total
# de numeros por la suma del primero y el ultimo
# y se divide entre 2 

#probando 1+2+3+4+5

numero = 5
suma_acumulada =  0

#usamos ciclo for para iterar
for i in range(1, numero + 1 ):
    suma_acumulada+=i

#aplicamos la formula
suma_formula = 0
suma_formula = numero * (numero + 1) / 2

print(f"Suma Acumulada = {suma_acumulada}")
print(f"Suma Formula Gauss = {suma_formula}")

#Woow comprobada!




