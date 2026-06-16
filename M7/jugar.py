import random
print("en este juego necesitas elegir si quieres ser piedra (1) , papel (2) , tijera (3) veamos quien gana ")
seguir = input("¿Quieres jugar? si/no: ")
#creamos el bucle segun lo que diga nuestra variable seguir 
while seguir == "si":
    print("en este juego necesitas elegir entre piedra (1), papel (2) o tijeras (3).")
    eleccion =int(input("elige entre 1, 2 o 3: "))
#creamos una variable randon de 1 a 3    
    eleccion_pc = random.randint(1, 3)
# creamos una variable vacia     
    puntos = 0

#creamos condicionales
    if eleccion == eleccion_pc:
        print("empate")
    elif (eleccion == 1 and eleccion_pc == 3) or (eleccion == 2 and eleccion_pc == 1) or (eleccion == 3 and eleccion_pc == 2):
        puntos += 1
        print("ganaste")
    #agregamos puntos a nuestra variabe puntos         
        
    else:
        print("perdiste")

    seguir = input("quieres jugar otra vez? si/no: ")

    if seguir == "no":

        print("gracias por jugar, tu puntaje final es: ", puntos)
        
# si decidimos no jugar nos aparece un mensaje 
if seguir == "no":
    print("nos vemos en otro momento")