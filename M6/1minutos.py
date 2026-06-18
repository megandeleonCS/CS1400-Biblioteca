"""
Tarea en Casa #1: Cálculo Básico de Factura con Validación Simple
En este programa, el usuario ingresará la cantidad de minutos usados en un servicio telefónico.
El programa validará que la entrada sea un número válido, y luego calculará el costo total
basado en una tarifa fija para los primeros 1000 minutos y una tarifa adicional para los minutos extra.
"""

# TODO 1: Pedir al usuario cuantos minutos (redondeado al mas cercano entero) ha usado, y asignarlo a una variable.

entrada = input("Ingresa la cantidad de minutos usados: ")


# 3. Usar una instrucción if  y isdigit() para verificar si el número es válido
if not entrada.isdigit():
    print("Error: Ingresa un número válido.")
    exit()  # Termina el programa si la entrada no es válida
    #TODO #2: Terminar el programa. 
        
    # Si la entrada no es válida
    # (puedes usar 'return' o 'exit()').
    # El 'return' asume que está en una función o que quiere terminar
    # Aquí simulamos terminar el programa si la entrada no es válida
    # Podrías usar sys.exit() en un script real

else:
    # Continuar solo si la entrada es válida
    # Calcular el cargo final (aunque este cálculo solo es el base, el principal está en el if/else)  
    minutos_usados = int(entrada)
    
    tarifa_base = 20.00
    # TODO #3: Calcular el costo total con if/else. Si el uso es menos o igual a 1000 son $20.
    # Si el uso es mayor a 1000, entonces se cobra $20 por los primeros 1000 minutos,
    # y $0.05 por cada minuto extra. 
    if minutos_usados <= 1000:
        costo_total = tarifa_base
    else:
        minutos_extra = minutos_usados - 1000
        costo_total = tarifa_base + (minutos_extra * 0.05)
    # Imprimir el total a pagar con un mensaje claro
    # Tomen notas del variable usado. Usamos 'minutos_usados' en lugar de 'minutos'
    # para coincidir con la variable
    print(f"Usaste {minutos_usados} minutos, tu factura es de ${costo_total:.2f}")

# Ejemplo de impresión final:
# Usaste 1004 minutos, tu factura es de $20.20