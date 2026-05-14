# test_tienda.py
from gestion_tienda import agregar_producto, buscar_precio
#He agreado listar productos
def run_tests():
    mi_inventario = {}
    print("--- Iniciando Pruebas de 'La Tiendita' ---")

    # Prueba 1: Agregar producto válido
    res1 = agregar_producto(mi_inventario, "Manzana", 1.50)
    if res1 and "Manzana" in mi_inventario:
        print("✅ Prueba 1 (Agregar): PASADA")
    else:
        print("❌ Prueba 1 (Agregar): FALLADA")

    # Prueba 2: Manejo de error (texto en lugar de número)
    res2 = agregar_producto(mi_inventario, "Pera", "caro")
    if res2 == False:
        print("✅ Prueba 2 (Error Handling): PASADA")
    else:
        print("❌ Prueba 2 (Error Handling): FALLADA")

    # Prueba 3: Buscar precio existente
    precio = buscar_precio(mi_inventario, "Manzana")
    if precio == 1.50:
        print("✅ Prueba 3 (Buscar): PASADA")
    else:
        print("❌ Prueba 3 (Buscar): FALLADA")

    # Prueba 4: Actualizar precio existente
    agregar_producto(mi_inventario, "Manzana", 1.80)
    if mi_inventario["Manzana"] == 1.80:
        print("✅ Prueba 4 (Actualizar): PASADA")
    else:
        print("❌ Prueba 4 (Actualizar): FALLADA")

    print("\n--- Fin de las pruebas ---")

if __name__ == "__main__":
    run_tests()

    #El test inco que el codigo paso las pruebas