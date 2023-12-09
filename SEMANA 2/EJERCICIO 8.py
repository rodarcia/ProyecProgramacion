# Ejercicio 8 de la semana 2 Desarrolle un programa que solicite al usuario la
# cantidad de horas semanales trabajadas, el precio que se le paga por hora
# y que calcule el salario mensual. Considere que se debe aplicar una deducción

#del 10.5% por cargas sociales y 5% por asociación solidarista.
#Asuma que cada mes cuenta con 4.2 semanas.

horas  = int (input ( " Solicite la cantidad de horas semanales trabajadas: "))
 
preciohora = int ( input ( " Solicie el precio que se paga por hora: " ))

resultado = (( horas * preciohora) * 4.2) - ( 0.155 * (( horas * preciohora )* 4.2))


print ( " El salario mensual menos las deducciones es: " , resultado)                                              
