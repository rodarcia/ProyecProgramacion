# Ejercicio 6 semana 2 Desarrolle un programa que solicite la distancia
# de su casa a la Universidad, el costo por kilómetro, la cantidad de días
# a la semana que viaja a la Universidad y que calcule el costo total
#de trasladarse por cuatrimestre.

distancia  = int (input ( "Solicite la distancia de la casa a la U: " ))

costo      = int (input ( "Solicite el costo por Kilometro : " ))

cantidaddias = int (input ( " Solicite la catidad de dias a la semana: " ))

resultado    = (((( distancia * cantidaddias ) * costo ) *15 ) * 2 )

print ( " El costo total de traladarse por cuatrimestre a la u es = ", resultado )
