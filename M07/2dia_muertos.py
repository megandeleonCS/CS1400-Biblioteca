
# Tarea 2: El Registro de los Ancestros (Diccionarios y Conjuntos)

# Tarea 2: Registro de visitas y ofrendas asignadas

# Diccionario con el ancestro (llave) y su platillo favorito (valor)
altares_familiares = {
    "Abuela Coco": "Tamales de dulce",
    "Tío Héctor": "Mole poblano",
    "Bizabuelo Julio": "Atole de chocolate"
}

# Lista con flores traídas por los visitantes (contiene duplicados)
flores_recibidas = ["Cempasúchil", "Nube", "Cempasúchil", "Terciopelo",
 "Nube", "Cempasúchil"]

#4. Iteración en Diccionarios: Escribe un bucle for utilizando el método .items()
 #para imprimir una frase por cada ancestro.
#(Ejemplo de salida esperada: "Para Abuela Coco preparamos: Tamales de dulce").

for nombres, plato in altares_familiares.items():
 print(f"Para {nombres} preparamo: {plato}.")
 
#5. Usa los métodos .keys() y .values() por separado para mostrar en pantalla
#  únicamente los nombres de los ancestros y luego únicamente los platillos.
for nombres in altares_familiares.keys():
 print(nombres)


for valores in altares_familiares.values():
  print(valores)
#6. Uso de Sets (Conjuntos): Para evitar contar flores repetidas en el inventario,
#  convierte la lista flores_recibidas en un set usando la función set().
flore_unicas = set(flores_recibidas) 
print(flore_unicas)
#7. Reflexión: ¿Cuántos elementos tenía la lista original de flores y cuántos quedaron
 #en el conjunto? ¿Por qué los conjuntos (sets) son ideales para la limpieza de datos?
 #Había 6 elementos, después del conjunto solo quedaron 3. El conjunto es ideal para la limpieza de datos porque elimina los duplicados.
