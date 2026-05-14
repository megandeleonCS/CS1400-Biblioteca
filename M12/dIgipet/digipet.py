# PROYECTO: DigiPet / Mascota Virtual
# Descripción:
# Este programa simula una mascota virtual.
# El usuario debe mantenerla viva controlando su hambre,
# salud y felicidad mientras la mascota envejece.

class DigiPet:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.comida = 100
        self.salud = 100
        self.energia = 100
        self.edad = 0
        self.vivo = True

    def mostrar_estado(self):
        print("\nMascota:", self.nombre)
        print(
            "Felicidad:", self.felicidad,
            "| Nivel de comida:", self.comida,
            "| Salud:", self.salud,
            "| Energía:", self.energia,
            "| Edad:", self.edad
        )

        if self.salud < 30:
            print("Tu mascota está enferma")
        elif self.salud < 70:
            print("Tu mascota está débil")

    def jugar(self):
        self.felicidad = self.felicidad + 12
        self.energia = self.energia - 10
        self.comida = self.comida - 8
        print("\nJugaste con", self.nombre)

    def alimentar(self):
        self.comida = self.comida + 15
        self.salud = self.salud + 5
        print("\nAlimentaste a", self.nombre)

    def pasear(self):
        self.felicidad = self.felicidad + 8
        self.salud = self.salud + 10
        self.energia = self.energia - 8
        self.comida = self.comida - 6
        print("\nPaseaste a", self.nombre)

    def acariciar(self):
        self.felicidad = self.felicidad + 10
        print("\nAcariciaste a", self.nombre)

    def descansar(self):
        self.energia = self.energia + 15
        self.salud = self.salud + 5
        print("\n", self.nombre, "descansó")

    def pasar_tiempo(self):
        self.edad = self.edad + 1
        self.felicidad = self.felicidad - 5
        self.comida = self.comida - 7
        self.salud = self.salud - 4
        self.energia = self.energia - 3
        self.limitar_valores()
        self.verificar_estado()

    def limitar_valores(self):
        self.felicidad = max(0, min(100, self.felicidad))
        self.comida = max(0, min(100, self.comida))
        self.salud = max(0, min(100, self.salud))
        self.energia = max(0, min(100, self.energia))

    def verificar_estado(self):
        if self.comida <= 0:
            print("\nMurió de hambre")
            self.vivo = False
        elif self.salud <= 0:
            print("\nMurió por enfermedad")
            self.vivo = False
        elif self.felicidad <= 0:
            print("\nMurió de soledad")
            self.vivo = False


def main():
    nombre = input("Nombre de tu mascota: ").strip()

    if nombre == "":
        nombre = "Peludito"

    mascota = DigiPet(nombre)

    while mascota.vivo:
        mascota.mostrar_estado()

        print("\n1. Jugar")
        print("2. Alimentar")
        print("3. Pasear")
        print("4. Acariciar")
        print("5. Descansar")
        print("6. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mascota.jugar()
            mascota.pasar_tiempo()
        elif opcion == "2":
            mascota.alimentar()
            mascota.pasar_tiempo()
        elif opcion == "3":
            mascota.pasear()
            mascota.pasar_tiempo()
        elif opcion == "4":
            mascota.acariciar()
            mascota.pasar_tiempo()
        elif opcion == "5":
            mascota.descansar()
            mascota.pasar_tiempo()
        elif opcion == "6":
            print("\nAdiós")
            break
        else:
            print("\nOpción no válida")

    if not mascota.vivo:
        print("\nFin del juego")


if __name__ == "__main__":
    main()