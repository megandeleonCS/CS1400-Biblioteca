# gestion_tienda.py

# Este módulo contiene las funciones para gestionar el inventario de la tienda.
# Crear las 3 funciones que se describen a continuación:
# Una para agregar un producto, debe recibir inventario, nombre y precio.
# Esta debe tener un try except ValueError para manejar el error si el precio no es un número.
# Otra para buscar el precio de un producto, debe recibir inventario y nombre. Utiliza .get()
# Y una última función para listar todos los productos, debe recibir el inventario.
# Tener una opcion por si esta vacio el inventario.

# No te olvides de agregar comenantarios a cada función explicando qué hace y cómo funciona.

def agregar_producto(inventario, nombre, precio):
    """
    Agrega o actualiza un producto en el diccionario.
    Maneja el error si el precio no es un número.
    """
    try:
        # Convertimos a float para asegurar que sea un número
        precio_num = float(precio)
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si no se puede convertir a número, devolvemos False
        return False

def buscar_precio(inventario, nombre):
    """
    Busca un producto y devuelve su precio. 
    Retorna None si no existe.
    """
    # Usamos .get() para evitar que el programa falle si la llave no existe
    return inventario.get(nombre, None)

def listar_productos(inventario):
    """
    Imprime todos los productos usando un bucle for.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
          print(f"• {producto}: ${precio:.2f}")

#Ejercicio
def main():
    #creamos el inventario como un diccionario vacío
    inventario = {}

    #ejemplo de agregar productos
    print("agregando productos...")
    agregar_producto(inventario, "Manzanas", 1.50)
    agregar_producto(inventario, "Pan", 2.00)

    #intento de agregar algo con precio inválido
    if not agregar_producto(inventario, "Leche", "dos"):
        print("Error: El precio debe ser un número.")

    #Listar los productos
    listar_productos(inventario)

    #buscar un precio
    producto_a_buscar = "Pan"
    precio = buscar_precio(inventario, producto_a_buscar)
    if precio is not None:
        print(f"\nEl precio de {producto_a_buscar} es: ${precio:.2f}")
    else:
        print(f"\n{producto_a_buscar} no se encuentra en el inventario.")

if __name__ == "__main__":
    main()