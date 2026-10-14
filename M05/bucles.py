#Código 1
# Impresión manual repetitiva
#print("Hola, estudiante")
#print("Hola, estudiante")
#print("Hola, estudiante")
#print("Hola, estudiante")
#print("Hola, estudiante")
#Análisis:
# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
#El problema con el código 1 es que hay que introducir el número de impresiones en relación con el número de alumnos, lo cual sería muy laborioso. Existen maneras de hacerlo de forma más rápida y eficiente.
# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? Explica por qué.
#No, porque el número de asentamientos está fijo en el código. Si el usuario desea un número diferente durante la ejecución, el código manual no puede ajustarse automáticamente.
#Bucle while 
# Intento de repetición con if
#respuesta = input("¿Deseas repetir el proceso? (si/no): ")

#while respuesta == "si":
    #print("Ejecutando el bloque...")
 #   respuesta = input("¿Deseas repetir el proceso? (si/no): ")

#print("Programa finalizado.")
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? Explica por qué sucede esto usando un if.
#El programa terminó poco después del segundo si.
#Modificación 1A (Cambio a while):
#siu
#Sustituye la palabra if por la palabra while en el código anterior y ejecútalo de nuevo.

# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
#Mediante el bucle `while`, el programa repite la condición mientras sea verdadera.
# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?
#no es possible.
#Modificación 1B (Bucle Infinito):
#Comenta la línea respuesta = input(...) que está dentro del bloque while. Ejecuta el programa e introduce "si".

# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?
#Cuando no hay ninguna variable de control, entra en un bucle infinito.
# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.
#Ctrl+C
# Ejemplo de range() simple
#num = int(input("Introduce un número límite: "))

#for i in range(2, 11, 2 ):
#    print("Iteración:", i)
#    Análise:
# 8. Execute o programa e insira o valor 10. Quantas vezes a palavra foi impressa "Iteración"? O número inserido pelo teclado influenciou o resultado desta primeira tentativa?
#No tiene ninguna influencia, porque el furioso no tenía la variable 'num', sino un número fijo.
# 9. Observe a saída numérica i. Qual é o valor inicial e qual é o valor final impresso?

#Valor inicial:0
#Valor final:9

# 10. O número chegou a ser impresso 10no console? Explique por que o Python exclui o limite superior em range().
#El número límite no se incluye en el cálculo porque ranger() comienza a contar desde cero.
# 11. Alterar range(10)para range(0, 10). Há alguma diferença no resultado obtido?
# no
#Modificação 2A (Intervalo com variável limite):
#Altere a linha de intervalo para usar a variável num: range(1, num).
# 12. Execute e insira 20. A contagem parou em 20ou em 19?
#El recuento se detuvo en 20.
# 13. Que ajuste matemático você precisa fazer internamente range()para que a conta inclua exatamente o número inserido pelo usuário?

#Responder: range(1,num + 1)

#Modificação 2B (Uso do argumento Step):
#Modifique a linha a: range(2, 11, 2).

# 14. Execute o programa. Quais valores foram impressos e qual função o terceiro argumento executa dentro dele range(inicio, fin, paso)?
#2,4,6,8,10 El tercer argumento determina el paso de conteo.
# Iteración sobre una cadena de texto
#palabra = "Python"
#
#print("--- Letras de la palabra ---")
#for letra in palabra:
#    print(letra)
#
# Iteración sobre una lista
#frutas = ["manzana", "banana", "cereza"]
#
#print("--- Lista de frutas ---")
#for fruta in frutas:
#    print(fruta)
#Análise:
# 15. No primeiro laço for letra in palabra:, o que a variável representa letraem cada etapa do laço?
#La variable 'letra' recibe una letra de la variable 'palabra' en cada iteración.
# 16. No segundo loop for fruta in frutas:, compare a iteração direta ( for fruta in frutas:) com o acesso por índice ( for i in range(len(frutas)):). Qual das duas opções é mais legível para um iniciante e por quê?
#(for fruta in frutas) es más fácil de leer e incluso de entender, ya que el término más técnico es demasiado confuso.
# Uso de break y continue
#print("Demostración de continue:")
#for num in range(1, 6):
#    if num == 3:
#        continue
#    print("Número:", num)

#print("\nDemostración de break:")
#for num in range(1, 6):
#    if num == 3:
#        break
#    print("Número:", num)
#  Análise:
# 17. Observe a saída da demonstração continue . Qual número está faltando na sequência impressa e por que isso aconteceu?
#En la demostración, continúe cuando llegue a la condición, se omite y continúa a la siguiente línea.
# 18. Observe a saída da demonstração do comando break . Quais números foram impressos e o que a instrução faz breakquando executada?
#En la instrucción `break`, se ejecuta y cuando llega a la condición, termina el bucle en el que se insertó el `break` y pasa a la siguiente línea.
#19. Suponha que você construa um loop while True:para solicitar chaves de acesso. Qual instrução permitiria sair do loop assim que o usuário inserir a chave correta?
#Yo usaría la instrucción break porque finaliza el bucle tan pronto como el usuario introduce la informacion correcta.
#Um padrão comum em programação envolve acumular valores ou contar ocorrências à medida que iteramos.

#Código 6:
#Python
# Acumulador de suma y contador de coincidencias
#numeros = [4, 7, 2, 9, 10, 5]
#suma_total = 0
#mayores_a_cinco = 0

#for num in numeros:
#    suma_total += num  # Acumula la suma
#    if num > 5:
#        mayores_a_cinco += 1  # Incrementa el contador

#print("Suma total:", suma_total)
#print("Cantidad de números mayores a 5:", mayores_a_cinco)
#Análise:
# 20.suma_total Com que valor as variáveis ​​devem ser inicializadas mayores_a_cinco antes de iniciar o loop? O que aconteceria se você as inicializasse dentro do loop?
#Debe comenzar con 0; si comenzara dentro del bucle, no acumularía los valores porque se reiniciaría a cero en cada iteración.
# 21. Explique com suas próprias palavras a diferença entre um acumulador ( suma_total += num) e um contador ( mayores_a_cinco += 1).
#El acumulador suma valores; el contador cuenta cuántas veces sucede algo.
#Seção 7: Normalização de texto com.lower()
#Analise como formatar strings dentro ou fora de um loop para realizar comparações precisas.

#Código 7
#Python
sujeto1 = "Python"
sujeto2 = "python"

if sujeto1 == sujeto2:
    print("Iguales")
else:
    print("Diferentes")
#Análise:
# 22. Observe as variáveis sujeto1​​e sujeto2. Qual é a diferença visual entre os dois textos e qual é o resultado da comparação inicial?
#Cambia la letra "P" inicial a mayúscula y luego a minúscula. Los resultados son diferentes.
# 23. Modifique a condição para if sujeto1.lower() == sujeto2.lower():. Execute o código novamente. Qual resultado você obtém e qual transformação o método realiza .lower()?
#Son iguales porque .lower transforma el texto insertado a minúsculas. Por lo tanto, parecen idénticas.
# 24. Por que é útil aplicar .lower()às respostas do usuário ao trabalhar com entradas dentro de um loop while(por exemplo, ao validar "SI", "Si"ou "si")?
#Dado que la etiqueta `.lower` estandariza la escritura independientemente de la entrada del usuario, podemos eliminar los errores causados ​​por diferencias en el estilo de escritura.