"""
Tarea en casa #2: Calculadora de precio de entrada al cine
En este programa, el usuario ingresará su edad y si es fin de semana o no.
El programa calculará el precio de la entrada al cine basado en la edad del usuario
 y si es fin de semana o no, usando una estructura de control if/else anidada.
"""
def calcular_precio_entrada():
    edad = int(input("cual es tu edad?: "))
    fin_de_semana = input("es fin de semana? (si/no): ")
    fin_de_semana = fin_de_semana.lower()
    #TODO 1: Pedir al usuario su edad y usar un variable para ver si es fin de semana
    #  Intenta usar la funcion .lower() por si el usuario escribe "Sí" o "sí" o "SI" o algo similar. 

    #TODO 2: Usar if/else anidados para calcular el precio de la entrada
    #  al cine basado en las siguientes reglas:
    # menores de 12 años pagan $5 los fines de semana y $3 entre semana,
    # mayores de 65 años pagan $6 los fines de semana y $4 entre semana,
    # y todos los demás pagan $10 los fines de semana y $7 entre semana.
    if edad < 12:
        if fin_de_semana == "si":
            precio = 5
        else:
            precio = 3
    elif edad > 65:
        if fin_de_semana == "si":
            precio = 6
        else:
            precio = 4
    else:
        if fin_de_semana == "si":
            precio = 10
        else:
            precio = 7
    
        

    #TODO 3: Imprimir el precio de la entrada al cine con un mensaje claro.
    # Por ejemplo, "El precio de tu entrada es: $5.00" intenta usar un f string para formatear.

    print(f"El precio de tu entrada es: ${precio:.2f}")

calcular_precio_entrada()