
## Preguntas para familia_madrigal.py
#1. ¿Qué pasaría si quitas @abstractmethod y creas un Madrigal("Alguien", 30)? Pruébalo y explica qué error aparece y por qué es útil.

#2. En Casita.dia_de_milagros() solo se escribe madrigal.usar_don(). ¿Por qué no necesitamos un if para cada personaje? (Pista: polimorfismo).

#3. ¿Por qué la energía es __energia y no simplemente energia? Intenta hacer familia[0].energia = 500 y luego familia[0].__energia = 500. ¿Qué diferencia notas?

#4. Si quisieras que todos los Madrigal tuvieran una “casa” (habitación), ¿en qué clase lo agregarías y por qué?

## Tareas para programar
#5. Agrega un nuevo personaje, por ejemplo Abuela Alma, con un don propio (como “proteger a la familia”) y añádelo a la lista familia. Observa que no tienes que cambiar nada en Casita.

#6. Modifica Mirabel para que, además, tenga un atributo tiene_gafas = True usando super().__init__(), igual que lo hace Antonio.

#7. Agrega un método esta_cansado() en Madrigal que devuelva True si la energía es menor a 30. Luego haz que dia_de_milagros() salte a quien esté cansado y diga que necesita descansar.

#8. Crea una clase Villano o Visitante que no herede de Madrigal pero tenga también usar_don(). ¿Funciona con dia_de_milagros()? ¿Qué te dice eso sobre cómo funciona Python?

#9. Crea una subclase Antonio que, al cumplir la ceremonia, reciba un don y que el método cumplir_anios() aumente la edad en uno. Después haz que Pepa cambie su estado_de_animo según su energía (si baja de 50, se pone “triste”).

#10. Haz un pequeño menú con input() donde el usuario elija un personaje y use su don, mostrando cómo baja su energía.
Un truco para motivar

Si logras agregar un personaje nuevo sin tocar la clase Casita, ¡ya entendiste el poder del polimorfismo! Esa es justamente la ventaja de la POO: añadir cosas nuevas sin romper lo que ya funciona.