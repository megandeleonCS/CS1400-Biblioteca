# -*- coding: utf-8 -*-
"""
==========================================================
 PROGRAMA DE DEMOSTRACION: ENTRADA / SALIDA EN PYTHON
==========================================================
Este programa tiene tres partes:

  PARTE 1: Entrada y salida basica (input / print)
  PARTE 2: (Extra) Consumir una API que devuelve JSON
  
Como ejecutarlo:
    python entrada_salida.py
"""

# ----------------------------------------------------------
# IMPORTACIONES
# ----------------------------------------------------------
import json                 # Para convertir texto JSON en diccionarios
import random               # Para elegir un refran al azar
import urllib.request       # Para hacer peticiones HTTP (viene con Python)
import urllib.error         # Para capturar errores de red


# ==========================================================
# LOS REFRANES DE LA ABUELA
# ==========================================================
# Un diccionario guarda parejas "clave: valor".
# Aqui la clave es el refran y el valor es lo que significa.
# TODO 1:  Agregar al menos un refran de tu familia: solo copia el formato.
REFRANES = {
    "Haz el bien y no mires a quien.":
        "Ayuda a los demas sin esperar nada a cambio.",

    "El leon juzga por su condicion.":
        "Cada quien cree que los demas piensan y actuan como uno.",

    "Uno pone y Dios dispone.":
        "Hacemos planes, pero la vida decide el resultado.",

    "Agua que no has de beber, dejala correr.":
        "Si algo no te conviene o no te toca, no te metas.",
}


def refran_al_azar():
    """Devuelve una pareja (refran, significado) elegida al azar."""
    # list(REFRANES.items()) convierte el diccionario en una lista de parejas.
    # random.choice() elige una de esas parejas al azar.
    return random.choice(list(REFRANES.items()))


def decir_refran(introduccion="Como decia la abuela:"):
    """Muestra un refran al azar con su significado."""
    # Desempaquetamos la pareja en dos variables.
    refran, significado = refran_al_azar()

    print()
    print(f"  {introduccion}")
    print(f'     "{refran}"')
    print(f"     (Es decir: {significado})")
    print()


def decir_refran_especifico(refran):
    """Muestra un refran en particular (no al azar) con su significado."""
    # REFRANES[refran] busca el significado usando el refran como clave.
    print()
    print(f'  La abuela diria: "{refran}"')
    print(f"     (Es decir: {REFRANES[refran]})")
    print()


# ==========================================================
# PARTE 1: ENTRADA Y SALIDA BASICA
# ==========================================================
def parte_uno_entrada_salida():
    """Pide datos al usuario con input() y los muestra con print()."""

    print("=" * 50)
    print("  PARTE 1: Entrada y salida basica")
    print("=" * 50)

    # Empezamos con un refran de bienvenida, como lo haria la abuela.
    decir_refran("Antes de empezar, la abuela dice:")

    # input() PIDE informacion al usuario (entrada). Siempre devuelve texto.
    nombre = input("Hola! Como te llamas? ")

    # TODO ¿Qué hace este bloque try/except ValueError?
    # ¿Qué pasaría si el usuario escribe “veinte” y quitamos ese bloque?

    try:
        edad = int(input("Cuantos anos tienes? "))
    except ValueError:
        print("Eso no parece un numero. Usare 0 como edad.")
        edad = 0

    comida = input("Cual es tu comida favorita? ")

    # ------------------------------------------------------
    # SALIDA: mostramos los datos de varias formas distintas
    # ------------------------------------------------------
    print()
    print(f"Mucho gusto, {nombre}!")                 # f-string
    
    # TODO ¿Como usamos acentos en espanol, otra vez?
    print("Tienes", edad, "anos.")                   # comas
    print("Tu comida favorita es " + comida + ".")   # concatenacion con +

    anos_para_100 = 100 - edad
    print(f"Te faltan {anos_para_100} anos para cumplir 100.")

    # ------------------------------------------------------
    # DECISIONES (if / elif / else): la abuela opina segun la edad
    # ------------------------------------------------------
    if edad >= 60:
        # Si ya tiene experiencia, le toca el refran de la sabiduria.
        decir_refran_especifico("Agua que no has de beber, dejala correr.")
    elif edad >= 18:
        # Un adulto con planes: "Uno pone y Dios dispone".
        decir_refran_especifico("Uno pone y Dios dispone.")
    else:
        # Para los jovenes, el consejo mas importante de todos.
        decir_refran_especifico("Haz el bien y no mires a quien.")

    # Devolvemos el nombre para reutilizarlo en la parte 2.
    return nombre


# ==========================================================
# PARTE 2 (EXTRA- si tienes tiempo): CONSUMIR UNA API JSON
# ==========================================================
#TODO ¿Que hace este api?
def parte_dos_api_json(nombre):
    """Consulta una API publica que responde en formato JSON."""

    print()
    print("=" * 50)
    print("  PARTE 2 (EXTRA): Usando una API JSON")
    print("=" * 50)

    # JSONPlaceholder: API gratuita de pruebas con usuarios falsos.
    url_base = "https://jsonplaceholder.typicode.com/users/"

    entrada = input("Elige un numero de usuario del 1 al 10: ")

    # .isdigit() es True solo si el texto contiene unicamente numeros.
    if not entrada.isdigit():
        print("Debes escribir un numero. Terminando esta parte.")
        return

    url = url_base + entrada
    print(f"Consultando: {url}")

    try:
        # urlopen() hace la peticion GET; timeout=10 evita esperar para siempre.
        with urllib.request.urlopen(url, timeout=10) as respuesta:
            texto_json = respuesta.read().decode("utf-8")

        # json.loads() convierte el texto JSON en un diccionario de Python.
        datos = json.loads(texto_json)

        if not datos:
            print("No se encontro ese usuario.")
            return

        # Accedemos a los valores con corchetes ["clave"].
        print()
        print(f"Resultado para {nombre}:")
        print("-" * 30)
        print(f"Nombre completo : {datos['name']}")
        print(f"Usuario         : {datos['username']}")
        print(f"Correo          : {datos['email']}")

        # Datos ANIDADOS: un diccionario dentro de otro.
        print(f"Ciudad          : {datos['address']['city']}")
        print(f"Empresa         : {datos['company']['name']}")

        # json.dumps() convierte un diccionario de vuelta a texto JSON.
        print()
        print("Direccion en formato JSON:")
        print(json.dumps(datos["address"], indent=2, ensure_ascii=False))

        # Todo salio bien: la abuela aprueba.
        decir_refran_especifico("Haz el bien y no mires a quien.")

    except urllib.error.HTTPError as error:
        # El servidor respondio, pero con un codigo de error (404, 500...).
        print(f"Error del servidor: codigo {error.code}")
        # Cuando algo sale mal por culpa de otros, la abuela tiene un refran.
        decir_refran_especifico("Uno pone y Dios dispone.")

    except urllib.error.URLError as error:
        # No se pudo ni conectar (sin internet, DNS caido, etc.).
        print(f"No se pudo conectar a internet: {error.reason}")
        decir_refran_especifico("Uno pone y Dios dispone.")

    except json.JSONDecodeError:
        # La respuesta llego, pero no era un JSON valido.
        print("La respuesta no tiene un formato JSON valido.")
        decir_refran_especifico("Agua que no has de beber, dejala correr.")


# ==========================================================
# PARTE 3: JUEGO "COMPLETA EL REFRAN" (entrada/salida con refranes)
# ==========================================================

def parte_tres_juego_refranes():
    """Muestra la primera mitad de un refran y el usuario adivina la otra."""

    print()
    print("=" * 50)
    print("  PARTE 3: Completa el refran de la abuela")
    print("=" * 50)

    refran, _ = refran_al_azar()   # "_" significa: ignoro el significado

    # Dividimos el refran en dos mitades usando las palabras.
    palabras = refran.split()              # "Uno pone y Dios" -> lista
    mitad = len(palabras) // 2             # // = division entera
    primera_parte = " ".join(palabras[:mitad])    # primeras palabras
    segunda_parte = " ".join(palabras[mitad:])    # palabras restantes

    print(f'La abuela empieza: "{primera_parte} ..."')
    intento = input("Como sigue? ")

    # Comparamos ignorando mayusculas, puntos y espacios sobrantes.
    # .lower() = minusculas, .strip() = quita espacios, .rstrip(".") = quita punto.
    limpio_intento = intento.lower().strip().rstrip(".")
    limpio_correcto = segunda_parte.lower().strip().rstrip(".")

    if limpio_intento == limpio_correcto:
        print("Muy bien! La abuela estaria orgullosa.")
    else:
        print("Casi! El refran completo es:")
        print(f'   "{refran}"')


# ==========================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ==========================================================
def main():
    """Funcion principal: ejecuta las partes en orden."""
    nombre = parte_uno_entrada_salida()

    # .lower() pasa a minusculas y .strip() quita espacios sobrantes.
    respuesta = input("\nQuieres probar la parte extra con la API? (si/no): ")
    if respuesta.lower().strip() in ("si", "s", "yes", "y"):
        parte_dos_api_json(nombre)
    else:
        # Si no quiere la API, la abuela tiene el refran perfecto.
        print("Esta bien, saltamos la parte extra.")
        decir_refran_especifico("Agua que no has de beber, dejala correr.")

    # Segunda pregunta: el juego de refranes.
    respuesta = input("Quieres jugar a completar un refran? (si/no): ")
    if respuesta.lower().strip() in ("si", "s", "yes", "y"):
        parte_tres_juego_refranes()

    # Despedida con un refran al azar.
    decir_refran("Para despedirnos, la abuela dice:")
    print(f"Fin del programa. Hasta luego, {nombre}!")


# Ejecuta main() solo si corremos este archivo directamente.
if __name__ == "__main__":
    main()
