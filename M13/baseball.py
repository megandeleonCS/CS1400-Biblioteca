class BaseballPlayer:
    def __init__(self):
        self.name = "none"
        self.number = "none"
        self.batting_avg = 0.0

    def print_info(self):
        print("Nombre: " + self.name)
        print("Número: " + str(self.number))
        print("Promedio de bateo: " + str(self.batting_avg))

    # Método para calcular el promedio de bateo
    def calculate_batting_avg(self, hits, at_bats):
        if at_bats > 0:
            self.batting_avg = hits / at_bats
        else:
            self.batting_avg = 0.0

def main():
    # Jugador 1
    player1 = BaseballPlayer()
    player1.name = "Juan"
    player1.number = 10

    # Jugador 2 (segunda instancia)
    player2 = BaseballPlayer()
    player2.name = "Thais"
    player2.number = 25

    # Calcular promedio del jugador 1
    player1.calculate_batting_avg(30, 100)

    # Imprimir promedio del jugador 1
    print("Promedio de bateo del jugador 1:", player1.batting_avg)

    print("\nInformación completa del jugador 1:")
    player1.print_info()

    print("\nInformación del jugador 2:")
    player2.print_info()


if __name__ == "__main__":
    main()