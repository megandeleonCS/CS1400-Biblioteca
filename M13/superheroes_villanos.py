import random

# Clase Player representa a cada jugador del juego
class Player:

    # Constructor: inicializa nombre, puntos de vida y fuerza
    def __init__(self, name):
        self.name = name              # Nombre del jugador
        self.life_points = 100        # Cada jugador comienza con 100 puntos de vida
        self.strength = 0             # Fuerza inicial en 0

    # Método para generar la fuerza del jugador
    # Genera un número aleatorio entre 1 y 20 (simula el ataque)
    def setStrength(self):
        self.strength = random.randint(1, 20)

    # Método para recibir daño
    # Reduce los puntos de vida según el daño recibido
    def receiveDamage(self, damage):
        self.life_points -= damage

        # Si la vida baja de 0, se ajusta a 0
        if self.life_points < 0:
            self.life_points = 0


def main():
    # Crear dos jugadores: superhéroe y villano
    hero = Player("Spidey")
    villain = Player("Doc Oct")

    # El juego continúa mientras ambos tengan vida
    while hero.life_points > 0 and villain.life_points > 0:

        # Mostrar los puntos de vida actuales
        print("\nPuntos de vida de", hero.name + ":", hero.life_points)
        print("Puntos de vida de", villain.name + ":", villain.life_points)

        # Solicitar acción al usuario
        choice = input("\nPresiona 'h' para luchar o 'q' para salir: ")

        # Si el usuario decide salir, el juego termina
        if choice == "q":
            print("\n¡Gracias por jugar!")
            break

        # Si el usuario decide atacar
        if choice == "h":

            # Ambos jugadores generan su fuerza aleatoria
            hero.setStrength()
            villain.setStrength()

            # Mostrar las fuerzas generadas
            print("\nFuerza de", hero.name + ":", hero.strength)
            print("Fuerza de", villain.name + ":", villain.strength)

            # Comparar las fuerzas
            if hero.strength > villain.strength:
                # El villano recibe daño (diferencia de fuerzas)
                damage = hero.strength - villain.strength
                villain.receiveDamage(damage)
                print(villain.name, "recibe", damage, "puntos de daño.")

            elif villain.strength > hero.strength:
                # El héroe recibe daño
                damage = villain.strength - hero.strength
                hero.receiveDamage(damage)
                print(hero.name, "recibe", damage, "puntos de daño.")

            else:
                # Si las fuerzas son iguales, no hay daño
                print("Empate. Nadie recibe daño.")

    # Determinar el ganador final
    if hero.life_points == 0:
        print("\n¡" + villain.name + " gana la batalla!")
    elif villain.life_points == 0:
        print("\n¡" + hero.name + " gana la batalla!")
    else:
        print("\nJuego terminado por el usuario.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()