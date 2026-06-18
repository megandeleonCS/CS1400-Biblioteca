"""
Tarea en casa #3: Calculadora de GPA
En este programa, el usuario ingresará el porcentaje actual de cada materia que está cursando
y el número de créditos de cada materia. El programa convertirá cada porcentaje a un valor de GPA
en una escala de 4.0, y luego calculará el GPA final del semestre basado en los créditos de cada materia.
"""

# Función, con un parametro, para convertir porcentaje a GPA en una escala de 4.0
def porcentaje_a_gpa(porcentaje):
    if porcentaje >= 93:
        return 4.0
    # TODO 1: Completa la función para convertir el porcentaje a GPA usando la escala estándar.
def porcentaje_a_gpa(porcentaje):
    if porcentaje >= 93:
        return 4.0
    elif porcentaje >= 86:
        return 3.0
    elif porcentaje >= 79:
        return 2.0
    else:
        return 0.0

# TODO #2: Pedir cuántas materias tiene el usuario, y asignarlo a un variable (recuerda convertirlo a un entero).

creditos = 00
num_materias = int(input("¿Cuántas materias tienes este semestre? "))


# Inicializar variables para acumular puntos y créditos
total_puntos = 0.0
total_creditos = 0

for i in range(num_materias):
    porcentaje = float(input(f"Ingrese el porcentaje actual de la materia #{i+1} (ejemplo: 87.5): "))
    creditos = float(input(f"Ingrese los créditos de la materia #{i+1}: "))
    
    gpa = porcentaje_a_gpa(porcentaje)
    total_puntos += gpa * creditos
    total_creditos += creditos

# TODO #3: Utiliza un if/else para calcular el GPA final dividiendo los puntos totales entre los créditos totales,
#  y mostrar el resultado al usuario con un mensaje claro.
# por ejemplo si los creditos totales son mayores que 0
# entonces calcula el GPA final y muestra el resultado
# de lo contrario muestra un mensaje indicando que no se ingresaron materias válidas.
# Si no, imprimir un mensaje indicando que no se ingresaron materias válidas o algo similar.
if total_creditos > 0:
    gpa_final = total_puntos / total_creditos
    print(f"Tu GPA estimado para el semestre es: {gpa_final:.2f}")
else:
    print("No se ingresaron materias válidas. Por favor, ingresa al menos una materia con créditos mayores a 0.")
# TODO #4: En que otra situacion podrias usar una funcion como esta?
# 
# 
#     

#Salida esperada
#Ingrese el porcentaje actual de la materia #1 (ejemplo: 87.5): 91
#Ingrese los créditos de la materia #1: 3
#Ingrese el porcentaje actual de la materia #2 (ejemplo: 87.5): 84
#Ingrese los créditos de la materia #2: 4
#Ingrese el porcentaje actual de la materia #3 (ejemplo: 87.5): 78
#Ingrese los créditos de la materia #3: 2

#Tu GPA estimado para el semestre es: 2.98
