#Práctica 1, problema 1 semana 3. Por: Roland Darcia Fernández.

# Solicite al usuario que ingrese 2 números enteros, y el programa debe poder
# calcular la división entera entre los dos números. Además de del cubo de ambos
# números (Se debe usar la función de potencia).Los resultados deben imprimirse en
# consola.Nota: No se debe incluir el valor de cero para no producir problemas
# en las operaciones.

Primernumero  = int (input ( " Solicite el primer número entero " ))

Segundonumero = int (input ( " Solicite el segundo número entero " ))

Divisionentera = Primernumero / Segundonumero

PrimernumeroalCubo   =  Primernumero**3

SegundonumeroalCubo  =  Segundonumero**3

print ( " Resultado de la división entera: " , Divisionentera, " Resultado primer numero al cubo: ", PrimernumeroalCubo, " Resultado segundo numero al Cubo: " , SegundonumeroalCubo,)

