# utils.py

def limpiar_y_tokenizar(texto):
<<<<<<< HEAD
  
    #Limpia el texto convirtiéndolo a minúsculas y eliminando ruido básico.
    #Devuelve una lista de palabras (tokens).
    
=======
    """
    Limpia el texto convirtiéndolo a minúsculas y eliminando ruido básico.
    Devuelve una lista de palabras (tokens).
    """
>>>>>>> 28c742b1d312d6b479870bc681b3edbbbad66ea5
    # Paso 1: Convertir a minúsculas con .lower()
    texto = texto.lower()
    
    # Paso 2: Reemplazos . con espacio y , con espacio usando .replace() (puedes añadir más si es necesario)
    texto = texto.replace(".", " ")
    texto = texto.replace(",", " ")
<<<<<<< HEAD
   
    
    # Paso 3: Dividir en palabras usando .split()
    palabras = texto.split()

     # Devuelve la lista de palabras
    
    return palabras

resultado = limpiar_y_tokenizar("Comenzar es, quizás, el acto más valiente que un ser humano puede realizar.")

for palabras in resultado:
    print(palabras)
=======
    
    # Paso 3: Dividir en palabras usando .split()
     palabras = texto.split()
    # Devuelve la lista de palabras
    return palabras

resultado = limpiar_y_tokenizar("Comenzar es, quizás, el acto más valiente que un ser humano puede realizar.")
for palabras in resultado:
    print(palabras)
>>>>>>> 28c742b1d312d6b479870bc681b3edbbbad66ea5
