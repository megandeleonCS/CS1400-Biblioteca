"""1. Función de saludo"""
def saludo(nombre):
   print(f"Hola, {nombre}!")

saludo("Megan")
saludo("Ana")

"""2. Función para calcular el área de un rectángulo"""
def area_rectangulo(largo, ancho):
    return largo * ancho

# Probando la función del área
resultado = area_rectangulo(10, 5)
print(f"El área del rectángulo es: {resultado}")

"""3. Class (Ejemplo Gato)"""
class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def maullar(self):
        return "¡Miau!"
    
tu_gato = Gato("Luna", 2)
print(f"{tu_gato.nombre} dice: {tu_gato.maullar()}")

"""4. Clase propia (Ejemplo Lámpara)"""
class Lampara:
    def __init__(self):
        self.encendida = False

    def interruptor(self):
        self.encendida = not self.encendida
        estado = "encendida" if self.encendida else "apagada"
        print(f"La lámpara está {estado}")

mi_lampara = Lampara()
mi_lampara.interruptor()

"""5. Tiempo (Manejo de I/O y Lógica)"""
class Tiempo:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self._normalize()

    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
    def _normalize(self):
        # Lógica de desbordamiento (de segundos a minutos, etc.)
        self.minutos += self.segundos // 60
        self.segundos %= 60
        self.horas += self.minutos // 60
        self.minutos %= 60
        self.horas %= 24 # Reinicia el reloj a las 00:00 si pasa de 24h

    def incrementar_tiempo(self, horas, minutos, segundos):
        self.segundos += segundos
        self.minutos += minutos
        self.horas += horas
        self._normalize()
        return self

# Funciones auxiliares
def tiempo_a_int(tiempo):
    return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos
    
def int_a_tiempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return Tiempo(horas, minutos, segundos)
    
def sumar_tiempo(tiempo, horas, minutos, segundos):
    total_segundos = tiempo_a_int(tiempo) + (horas * 3600) + (minutos * 60) + segundos
    return int_a_tiempo(total_segundos)

# Pruebas finales
mi_hora = Tiempo(14, 30, 15)
print("Hora inicial:", mi_hora)

nueva_hora = sumar_tiempo(mi_hora, 2, 50, 30)
print("Nueva Hora (función):", nueva_hora)

mi_hora.incrementar_tiempo(1, 45, 30)
print("Hora incrementada (método):", mi_hora)

#Mi propia clase
#Funcion de despedida
def despedida(nombre):
    # Escribe tu código aquí
    print(f"Adiós, {nombre}!")

# Prueba de la función
despedida("Megan")
despedida("Ana")
