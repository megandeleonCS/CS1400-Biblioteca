
nombre = input("Hola, ¿Cual es tu nombre? ")
print("Hola   " + nombre)

segundonombre = input("¿Cual es tu segundo nombre?   ")
     
apellido = ("¿Cual es tu apellido?  ")

nombrecompleto = input("¿Cual es tu nombre completo    " )

casada = input("¿Eres casada?  (si/no):   ") 

edad = input("Thais, ¿que edad tienes?   ")

beneficios = input("¿Tiene beneficios tener tu edad? (si/no):  ")
beneficio1 = input("¿Tienes entradas de precio reducido  (si/no):  ")
beneficio2 = input("¿Tenes Mejor salario por antiguedad (si/no):  ")

if beneficios.lower()  ==  "si":
    print("beneficios posibles:   ")
    print("1. Entradas de precio reducido")
    print("2. Mejor salario por antiguedad")
else:
    print("No hay beneficios registrados   ")
#practica 2112025
#al usar al .lower()para evitar problemas con el si
#el if ejecuta las repuestas afirmativas
#else se usa como la otra alternativa en caso de que sea no alguna de las repuestas.