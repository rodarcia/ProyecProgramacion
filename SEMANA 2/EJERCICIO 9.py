# Ejercicio 9 de la semana 2. Desarrolle un programa que le solicite al usuario
# sus ingresos mensuales y sus gastos mensualespor alimentación.
# Con esta información el programa debe mostrar el porcentaje que gasto
# que corresponde al rubro de alimentación y el porcentaje que queda disponible
# para otros rubros.

ingresos  = int (input( " Solicite la cantidad de sus ingresos: "))

gastosdealimentación = int (input( " Solicite gastos de alimentación "))

porcentajedealimentación = (( gastosdealimentación / ingresos)* 100)

porcentajedelodisponible = ( 100-(porcentajedealimentación))

print ( " El porcentaje de gastos de alimentación y el  porcentaje de lo disponible: " , porcentajedealimentación , porcentajedelodisponible )


 
