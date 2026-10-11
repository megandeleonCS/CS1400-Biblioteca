
from api import obtener_coordenadas

print("[TEST] Iniciando pruebas de la API...")

# Prueba 1: Ciudad válida con acentos o espacios
print("\n--- Probando una ciudad válida (Bogotá) ---")
resultado_bogota = obtener_coordenadas("Bogotá ")
print(resultado_bogota)

# Prueba 2: Otra ciudad válida en otro país
print("\n--- Probando otra ciudad (Tokio) ---")
resultado_tokio = obtener_coordenadas("Tokyo")
print(resultado_tokio)

# Prueba 3: Ciudad inventada o que no existe (para probar el manejo de errores)
print("\n--- Probando un lugar falso (AtlantisXYZ) ---")
resultado_falso = obtener_coordenadas("AtlantisXYZ123")
print(resultado_falso)

print("\n[FIN] Pruebas finalizadas.")

# TODO 1: Cual es el resultado al correr test_api?
# 
# TODO 2: Agrega estas lineas para arreglar el problema con los acentos.
# import sys
# sys.stdout.reconfigure(encoding='utf-8')
# TODO 3: Intenta con otra ciudad. 
"""
Si quieres probar ciudades que se llaman igual en distintos países
(por ejemplo, San José en Costa Rica y San José en California, EE. UU.),
puedes escribir la consulta de manera más específica como "San Jose, Costa Rica"
"""
#TODO 4: