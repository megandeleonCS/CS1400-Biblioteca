"""
La familia Madrigal de Encanto: un ejemplo de Programación Orientada a Objetos.

Conceptos que se muestran:
  1. Clases y objetos
  2. Herencia (Madrigal -> personajes con don)
  3. Polimorfismo (cada don se usa de forma distinta)
  4. Encapsulamiento (atributo privado: la energía)
  5. Métodos especiales (__str__)
  6. Composición (la Casita contiene a los Madrigal)
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------
# CLASE BASE (abstracta): todo Madrigal comparte estas cosas
# ---------------------------------------------------------------
class Madrigal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.__energia = 100  # atributo privado (encapsulamiento)

    # --- Encapsulamiento: solo se accede a la energía con estos métodos ---
    @property
    def energia(self):
        return self.__energia

    def gastar_energia(self, cantidad):
        self.__energia = max(0, self.__energia - cantidad)

    def descansar(self):
        self.__energia = 100
        print(f"😴 {self.nombre} descansa y recupera toda su energía.")

    # --- Cada hijo DEBE definir su propio don (polimorfismo) ---
    @abstractmethod
    def usar_don(self):
        pass

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - Energía: {self.energia}%"


# ---------------------------------------------------------------
# CLASES HIJAS: heredan de Madrigal y redefinen usar_don()
# ---------------------------------------------------------------
class Mirabel(Madrigal):
    def usar_don(self):
        print(f"🔍 {self.nombre} no tiene don mágico, ¡pero tiene el don de ser valiente!")
        self.gastar_energia(5)


class Isabela(Madrigal):
    def usar_don(self):
        print(f"🌸 {self.nombre} hace crecer flores y cactus por todos lados.")
        self.gastar_energia(15)


class Luisa(Madrigal):
    def usar_don(self):
        print(f"💪 {self.nombre} levanta un burro como si nada.")
        self.gastar_energia(25)


class Julieta(Madrigal):
    def usar_don(self):
        print(f"🍲 {self.nombre} cocina arepas que sanan cualquier herida.")
        self.gastar_energia(10)


class Pepa(Madrigal):
    def __init__(self, nombre, edad, estado_de_animo="feliz"):
        super().__init__(nombre, edad)  # llama al constructor del padre
        self.estado_de_animo = estado_de_animo

    def usar_don(self):
        clima = {
            "feliz": "☀️ sale el sol",
            "triste": "🌧️ empieza a llover",
            "enojada": "⛈️ cae una tormenta con rayos",
        }
        print(f"{clima[self.estado_de_animo]} porque {self.nombre} está {self.estado_de_animo}.")
        self.gastar_energia(15)


class Dolores(Madrigal):
    def usar_don(self):
        print(f"👂 {self.nombre} escucha un susurro a kilómetros de distancia.")
        self.gastar_energia(10)


class Camilo(Madrigal):
    def usar_don(self):
        print(f"🎭 {self.nombre} se transforma en otra persona. ¡Qué travieso!")
        self.gastar_energia(20)


class Antonio(Madrigal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.animales = ["jaguar", "tucán", "capibara", "coatí"]

    def usar_don(self):
        print(f"🐆 {self.nombre} habla con los animales: {', '.join(self.animales)}.")
        self.gastar_energia(10)


class Bruno(Madrigal):
    def usar_don(self):
        print(f"🔮 {self.nombre} ve el futuro... pero ¡no hablamos de Bruno!")
        self.gastar_energia(30)


# ---------------------------------------------------------------
# COMPOSICIÓN: la Casita "tiene" una lista de Madrigal
# ---------------------------------------------------------------
class Casita:
    def __init__(self):
        self.habitantes = []

    def dar_bienvenida(self, madrigal):
        self.habitantes.append(madrigal)
        print(f"🏠 La Casita le da la bienvenida a {madrigal.nombre}.")

    def mostrar_familia(self):
        print("\n👨‍👩‍👧‍👦 FAMILIA MADRIGAL:")
        for madrigal in self.habitantes:
            print("  •", madrigal)  # usa __str__

    def dia_de_milagros(self):
        """Polimorfismo: llamamos usar_don() en todos sin importar su clase."""
        print("\n✨ ¡Comienza el día de los milagros! ✨")
        for madrigal in self.habitantes:
            madrigal.usar_don()


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
if __name__ == "__main__":
    casita = Casita()

    familia = [
        Mirabel("Mirabel", 15),
        Isabela("Isabela", 21),
        Luisa("Luisa", 19),
        Julieta("Julieta", 50),
        Pepa("Pepa", 48, estado_de_animo="enojada"),
        Dolores("Dolores", 22),
        Camilo("Camilo", 17),
        Antonio("Antonio", 5),
        Bruno("Bruno", 52),
    ]

    for persona in familia:
        casita.dar_bienvenida(persona)

    casita.mostrar_familia()
    casita.dia_de_milagros()
    casita.mostrar_familia()  # la energía bajó

    print()
    familia[-1].descansar()  # Bruno descansa
    print(familia[-1])
