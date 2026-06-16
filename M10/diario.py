# --- Diaro de Tiffany Digital ---
import datetime
# Aqui tu funcion menu()
def menu():
    print("Bienvenido al Diario de Tiffany Digital")
    print("1. Escribir una nueva entrada")
    print("2. Leer el diario")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion
#Aqui tu if/elif/elif/else statement con las opciones del menu
while True:
    opcion = menu()
    if opcion == "1":
        # Entrada de datos
        entrada = input("Escribe tu pensamiento de hoy: ")
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Guardar en archivo
        with open("diario.txt", "a") as archivo:
            archivo.write(f"{fecha}: {entrada}\n")
        print("Entrada guardada.")
    elif opcion == "2":
        # Leer el archivo y mostrarlo
        print("Entradas en el diario:")
        with open("diario.txt", "r") as archivo:
            for linea in archivo:
                print(linea.strip())
    elif opcion == "3":
        #salir del programa
        print("¡Hasta luego!")
        break
    else:
        #else para manejar opciones no válidas
        print("Opción no válida. Por favor, selecciona una opción válida.")
