import random

class Player:
    # Método init
    def __init__(self):
        self.score = 0
        self.totalRoll = 0

    # Método para lanzar los dados
    def roll(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        self.totalRoll = dado1 + dado2

    def __str__(self):
        return "Score: " + str(self.score)

    # Método para sumar puntos
    def addToScore(self):
        self.score += 1


def main():
    player1 = Player()
    player2 = Player()

    choice = ""

    while choice != "quit":
        choice = input("Presiona ENTER para lanzar los dados o escribe 'quit': ")

        if choice == "quit":
            break

        player1.roll()
        player2.roll()

        print("Player 1 lanzó:", player1.totalRoll)
        print("Player 2 lanzó:", player2.totalRoll)

        if player1.totalRoll > player2.totalRoll:
            player1.addToScore()
            print("Player 1 gana la ronda")
        elif player2.totalRoll > player1.totalRoll:
            player2.addToScore()
            print("Player 2 gana la ronda")
        else:
            print("Empate")

        print("Player 1:", player1)
        print("Player 2:", player2)
        print()

    # Determinar ganador final
    if player1.score > player2.score:
        print("Player 1 gana el juego")
        print("El usuario gana")
    elif player2.score > player1.score:
        print("Player 2 gana el juego")
        print("El usuario pierde")
    else:
        print("El juego terminó en empate")


if __name__ == "__main__":
    main()
    