# main.py
# Este es el programa principal para gestionar la tienda.
# Los nombres de las funciones deben concoradr con los siguientes:
from gestion_tienda import agregar_producto, buscar_precio, listar_productos

    # Aqui se muestra el menú de opciones al usuario
    # El usuario puede elegir entre ver el inventario, agregar un producto, buscar un precio o salir.
    # El programa seguirá ejecutándose hasta que el usuario elija salir.
    # TODO #1 Completa el menú de opciones imprimiendo un mensaje y las opciones
    
    # Aqui se muestra el menú de opciones al usuario
    # El usuario puede elegir entre ver el inventario, agregar un producto, buscar un precio o salir.

def mostrar_menu():
      print("\n=== MENÚ DE LA TIENDA ===")
      print("1. Ver inventario")
      print("2. Agregar producto")
      print("3. Buscar precio")
      print("4. Salir")

    # TODO #2 iniciar un diccionario vacio 
def ejecutar_programa():

    mi_inventario = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            listar_productos(mi_inventario)

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            exito = agregar_producto(mi_inventario, nombre, precio)

            if exito:
                print(f"✅ '{nombre}' guardado correctamente.")
            else:
                print("❌ Error: El precio debe ser un número (ej: 10.50).")

        elif opcion == "3":
            nombre = input("¿Qué producto buscas?: ")
            precio = buscar_precio(mi_inventario, nombre)

            if precio is not None:
                print(f"🔍 El precio de '{nombre}' es ${precio:.2f}")
            else:
                print(f"⚠️ El producto '{nombre}' no existe.")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Buen día!")
            break

        else:
            print("🚫 Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    ejecutar_programa()    
def ejecutar_programa():
    mi_inventario = {}
    
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            listar_productos(mi_inventario)

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            exito = agregar_producto(mi_inventario, nombre, precio)
            if exito:
                print(f"✅ '{nombre}' guardado correctamente.")
            else:
                print("❌ Error: El precio debe ser un número (ej: 10.50).")

        elif opcion == "3":
            nombre = input("¿Qué producto buscas?: ")
            precio = buscar_precio(mi_inventario, nombre)
            if precio is not None:
                print(f"🔍 El precio de '{nombre}' es ${precio:.2f}")
            else:
                print(f"⚠️ El producto '{nombre}' no existe.")

        elif opcion == "4":
            print("Saliendo del sistema... ¡Buen día!")
            break
        
        else:
            print("🚫 Opción no válida, intenta de nuevo.")

# El programa se ejecutará desde aquí
if __name__ == "__main__":
    ejecutar_programa()