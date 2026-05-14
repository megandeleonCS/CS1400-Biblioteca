# --- Diaro de      Digital ---

# Aqui tu funcion menu()

from datetime import datetime
menu = ()

def menu():
    print("\n1. Escribir")
    print("2. Leer")
    print("3. Salir")
    return input("Seleccione una opcion: ")

while True:
    opcion = menu()

    if opcion == "1":
        entrada = input("Escribe tu pensamiento: ")
        fecha = datetime.now()

        archivo = open("diario.txt", "a")
        archivo.write(f"- [{fecha}] {entrada}\n")
        archivo.close()

        print("Entrada guardada.")

    elif opcion == "2":
        try:
            archivo = open("diario.txt", "r")
            print("\nContenido del diario:")
            print(archivo.read())
            archivo.close()
        except FileNotFoundError:
            print("No existe el archivo.")

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opcion no valida.")



