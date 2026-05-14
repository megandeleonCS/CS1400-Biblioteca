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
#Esta funcion agrega un producto al inventario o actualiza su precio, ademas recibe tres parametros
#inventario: diccionario donde se guardan los productos, nombre: nombre del producto y precio: precio del producto.
#Usa try/except para manejar el error si el precio no es un número.
#Agrega o actualiza un producto en el diccionario.

    """
    Agrega o actualiza un producto en el diccionario.
    Maneja el error si el precio no es un número.
    """
    try:
        # Convertimos el inventario a precio
        precio_num = float(precio)
        #Se guarda el numero en el diccionario
        inventario[nombre] = precio_num
        return True
    except ValueError:
        # Si el precio no es valido, devuelve False
        print("Error: el precio debe ser un número.")
        return False

def buscar_precio(inventario, nombre):
    #Busca el precio de un producto dentro del inventario.
    #Utiliza el método .get() para evitar errores si el producto no existe.
    #Si no se encuentra, devuelve None.
    
    """
    Busca un producto y devuelve su precio. 
    Retorna None si no existe.
    """
    # Usamos .get() para evitar que el programa falle o que devuelva error si el producto no existe no existe
    return inventario.get(nombre, None)

def listar_productos(inventario):
    #Esta funcion se ejecuta con el for para buscar un producto como se ve a continuacion
    """
    Imprime todos los productos usando un bucle for.
    """
    if not inventario:
        print("\n> El inventario está vacío.")
    else:
        print("\n--- Inventario Actual ---")
        for producto, precio in inventario.items():
            print(f"• {producto}: ${precio:.2f}")
  
  
  #Ejemplo de ejercicio
from gestion_tienda import agregar_producto, buscar_precio, listar_productos

# Crear inventario vacío
inventario = {}

# Agregar productos (usa float dentro de la función)
agregar_producto(inventario, "manzana", "1.50")
agregar_producto(inventario, "pan", "2.20")
agregar_producto(inventario, "leche", "3.10")

# Intentar agregar un precio incorrecto
if not agregar_producto(inventario, "huevos", "dos"):
    print("Error: el precio debe ser un número")

# Buscar precios (usa .get())
#El get hace que no devuelva error sino none que podria ser no hay?
print("\nBuscando productos...")
print("Precio de manzana:", buscar_precio(inventario, "manzana"))
print("Precio de queso:", buscar_precio(inventario, "queso"))

# Mostrar inventario
listar_productos(inventario)
        