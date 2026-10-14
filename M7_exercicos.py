"""
num_salon = {
    "Murphy": 304,
    "Feiz": 336,
    "Mack": 207,
    "Ball": 227,
    "Bristow": 321,
    "Cruz": 101

}
num_salon["DeLeon"] = 147
num_salon["Hernandez"] = 323
print("La longitud es", len(num_salon))

# Agregar un elemento adicional al diccionario
num_salon["Valle"] = 216
print("La lengitud ahora es ", len(num_salon))

print( num_salon.get("Valle") )
print( num_salon["Murphy"])
"""
"""
import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
refugioOriginal = copy.deepcopy(animalesRefugiados)
animalesRefugiados["perro"] += 2
animalesRefugiados["huron"] = 2
animalesRefugiados["gato"] -= 3
animalesRefugiados["serpiente"] = 4
print(animalesRefugiados)

if animalesRefugiados["perro"]> 50:
    print("lleno")

if "raton" not in animalesRefugiados:
    print("No ratones")


print(refugioOriginal)
"""
# Ejemplo de conteo de palabras
text = "sana sana curita de rana sana sana pomada de sapo sana sana hoy y manana manana y hoy"

lst = text.split()
plbList = dict()

for x in lst:
    if x not in plbList:
        plbList[x] = 1
    else:
        plbList[x] += 1

for i in plbList:
    print (i, plbList[i])

# Ejemplo de conteo de calificaciones
notas = "A A A B B A C A B C C E A B A C C C A B B B A B A A A C D A B B C C A A A B A B A C A B B A"
listaNotas = notas.split()
notasDiccionario = dict()

for i in listaNotas:
  if i not in notasDiccionario:
    notasDiccionario[i] = 1
  else:
    notasDiccionario[i] += 1

for i in notasDiccionario:
  print(i, notasDiccionario[i])  