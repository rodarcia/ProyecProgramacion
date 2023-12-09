# Ejercicio 7 de la semana 2 Desarrolle un programa que solicite al usuario
# la edad de 5 personas y le muestre cuál es la edad promedio.

persona1  = int ( input ( " Solicite la edad de la persona 1: "))
persona2  = int ( input ( " Solicite la edad de la persona 2: "))
persona3  = int ( input ( " Solicite la edad de la persona 3: "))
persona4  = int ( input ( " Solicite la edad de la persona 4: "))
persona5  = int ( input ( " Solicite la edad de la persona 5: "))

resultado  = (( persona1 + persona2 +persona3 + persona4+ persona5)/ 5 )

print ( " La edad promedio de las 5 personas " , resultado )
