#Marcos Alves oct 01.2026
"""
# Conteo descendente
#Contagem Reversa com range() pronto e funcionando.
num = int(input("Introduce el número inicial: "))

for i in range(num, 0, -1):
    print("Conteo:", i)

    # Conteo descendente
num = int(input("Introduce el número inicial: "))

for i in range(num, -1, -2):
    print("Conteo:", i)
# 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?

#Inicio:10 Fin: 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
#para que el conteo se realice en orden inverso.
# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
#Porque el número que ponemos al final no cuenta; siempre se refiere a un número anterior.
#Práctica de Sección:
# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:

#Respuesta: range( _______ , _______ , _______ )
"""
"""
Previsões de saída (Insira o resultado exato):
import math

decNum = -34.5678
intNum = 9

print( round(decNum, 2) )   # Línea A
print( round(decNum, 0) )   # Línea B
print( int(decNum) )        # Línea C
print( abs(decNum) )        # Línea D

print( math.pow(intNum, 2) ) # Línea E
print( math.sqrt(intNum) )   # Línea F
# 5. Resultado da Linha A round(decNum, 2)? -34.57

# 6. Resultado da Linha B round(decNum, 0)? -35.0

# 7. Resultado da Linha C int(decNum)? -34 (Dica: Ela arredonda ou trunca decimais?) trunca

# 8. Resultado da Linha D abs(decNum)? 34.5678

# 9. Resultado da Linha E math.pow(intNum, 2)? 81.0

# 10. Resultado da Linha F math.sqrt(intNum)? 3.0
"""
"""
#Seção 3: Comparando textos usando ASCII/Unicode
#Análise:
# 11. Antes de executar: Qual você acha que será o resultado retornado por max()?
miMax = max("Banano", "manzana", "Zanahoria")
print("El máximo es:", miMax)

#Previsão: Zanahoria
# 12. Execute o código. Qual foi o resultado retornado?

#Resultado: manzana


# 13. Sabendo que na tabela ASCII as letras maiúsculas têm valores numéricos menores do que as letras minúsculas , explique por que "manzana"foi escolhido o valor maior em comparação com o "Zanahoria".
#Valores de la tabla ASCII
A= 65
B= 66
a= 97
b= 98

# 14. Altere a função de max()para min(). Qual valor você obtém agora e por quê?
miMax = min("Banano", "manzana", "Zanahoria")
print("El minimo es:", miMax)
#Resultado: banano, Porque, además, las letras minúsculas tienen más peso.
"""
"""

#Seção 4: Aplicação Prática – Física e Matemática
#A polícia de trânsito calcula a velocidade v de um carro a partir do comprimento d da marca de frenagem usando a fórmula: v = \sqrt{20 \cdot d} .

#Código 4.1:
#Python
import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(20 * d )

print("Velocidad estimada del auto:", round(v, 2), "km/h")
#Análise:
# 15. Complete a tarefa v =no código acima usando a math.sqrt()função e a fórmula fornecidas. Escreva a linha completa abaixo:

#Responder: v = math.sqrt(20 * d )
"""
"""
#Seção 5: Segmentação da Cadeia ( Fatiamento )
#O fatiamento permite extrair substrings usando a sintaxe cadena[inicio:fin:paso].

#Código 5.1:
#Python
nombre = "Building Puentes"

print("Índice 0:", nombre[0])
print("Segmento:", nombre[9:16])
#Análise:
# 16. Qual caractere é impresso exatamente nombre[0]? B

# 17. Em que posição exata (índice) se encontra o espaço em branco entre as duas palavras? 8

# 18. Modifique os índices nombre[X:Y]para extrair e imprimir exatamente a palavra "Puentes".

#Opção com 2 valores: nombre[ 9 : 16 ]

#Opção com limite implícito: nombre[9 : ]
"""
"""
#Seção 6: Filtragem e Inspeção de Caracteres em Cadeias de Caracteres
#Podemos usar loops combinados com condicionais para inspecionar e filtrar tipos específicos de caracteres em um texto.

#Código 6.1:
#Python
texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)
#Análise:
# 19. Execute o programa e digite o texto "3 tigres en 2 árboles". Qual valor ele imprime contador_numeros? 2

# 20. Observe a condição do if. Explique como o Python avalia se um caractere individual é um dígito numérico usando os operadores >=e <=.
#20. Python compara carácter por carácter y comprueba si: >=0 y =<9; si lo es, lo cuenta como 1 carácter.
"""
Seção 7: Investigação de Métodos de String
Investigue a funcionalidade dos seguintes métodos na documentação oficial do Python ou no W3Schools e explique brevemente sua finalidade:

# 21. Método .rfind('a'):

Descrição:Busca dónde aparece algo por última vez en el texto.
# 22. Método .isalpha():

Descrição:Comprueba si el texto contiene solo letras.

# 23. Método .isdigit():

Descrição:Comprueba si el texto contiene solo dígitos.