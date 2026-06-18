# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
if edad >= 18 and tiene_permiso == True:
    print("puedes salir")
else:
    print("no tienes permiso")


# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
if es_finde == True or tiene_permiso == True:
    print("tienes permitido salir")
else:
    print("no tienes permitido salir")


# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
not tiene_permiso


# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 

edad_conducir = 20
tiene_carro = False
tiene_licensia = True

if edad_conducir >= 18 and tiene_licensia == True:
    print("puedes conducir, pero con cuidado")

if tiene_licensia == True or tiene_carro == True:
    print("puedes practicar manejando")

not tiene_licensia




