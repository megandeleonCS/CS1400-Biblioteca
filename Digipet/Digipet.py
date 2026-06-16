import random

class DigiPet:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.comida = 100
        self.salud = 100
        self.vivo = True

    def mostrar_estado(self):
        print(f"\n--- {self.nombre} ---")
        print(f"Felicidad: {self.felicidad} | Comida: {self.comida} | Salud: {self.salud}")

    def alimentar(self):
        print(f"Alimentaste a {self.nombre}.")
        self.comida += 20
        if self.comida > 100: self.comida = 100

    def jugar(self):
        print(f"Jugaste con {self.nombre}!")
        self.felicidad += 15
        self.comida -= 10

    def pasar_tiempo(self):
        # Cada turno la mascota envejece un poco
        self.felicidad -= 5
        self.comida -= 10
        self.salud -= 5
        
        if self.felicidad <= 0 or self.comida <= 0 or self.salud <= 0:
            self.vivo = False

# Lógica principal del juego
mi_mascota = DigiPet("Tammy")

while mi_mascota.vivo:
    mi_mascota.mostrar_estado()
    print("1. Jugar\n2. Alimentar\n3. Salir")
    opcion = input("¿Qué quieres hacer? ")

    if opcion == "1":
        mi_mascota.jugar()
    elif opcion == "2":
        mi_mascota.alimentar()
    elif opcion == "3":
        break
    
    mi_mascota.pasar_tiempo()

if not mi_mascota.vivo:
    print(f"Oh no, {mi_mascota.nombre} ha muerto. ¡Inténtalo de nuevo!")