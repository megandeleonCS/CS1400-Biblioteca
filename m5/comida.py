#Todo 1
print('bienvenido al programa de comidas de latinoamerica')
#todo 2
print('a continuacion se mostraran algunas comidas tipicas de latinoamericana\ntacos, tamales, ceviche, gorditas, pupusas')
#todo 3
comida = input("ingrese una comida: ")

#todo 4
comida = comida.lower()
#todo 5
if comida == "tamales":
    print("los tamales son de Centroamerica")
elif comida == "tacos":
    print("los tacos son de Mexico")    
elif comida == "ceviche":
    print("el ceviche es de Peru") 
elif comida == "gorditas":
    print("las gorditas son de Mexico") 
elif comida == "pupusas":
    print("las pupusas son de El Salvador")
else:
    print("no hay comidas disponibles") 