# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?

if edad >= 16 and tiene_permiso == True:
    print('Esta correcto la expresion con el and')

# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso
if es_finde == True or tiene_permiso == True:
    print('Esta correcto la expresion con el or')


# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
if not es_finde == True:
    print('Esta correcta la expresion booleana not')

# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
Edad_para_tomar = int(input('Que edad tienes? '))
conduccion = input('Estas manejando? s/n: ')
conduccion = conduccion.lower()
if Edad_para_tomar > 21 and conduccion == 'n':
    print('Si puedes tomar bebidas alcoholicas')
else:
    print('No puedes tomar bebidas alcoholicas')


print('hola')