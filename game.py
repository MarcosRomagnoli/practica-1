import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_fallos=5
fallos=1

# Lista para almacenar las letras adivinadas
guessed_letters = []

#Funcion que setea la dificultad con s
def mostrar_palabra(dificultad ,secret_word, guessed_letters):
    if (dificultad==1):
        vocales = "aeiou"
        displayed_word = ""
        for letter in secret_word:
            if letter in vocales or letter in guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
        return displayed_word
    elif (dificultad==2):
        displayed_word = secret_word[0] + "_" * (len(secret_word) - 2) + secret_word[-1]
        for letter in guessed_letters:
            if letter in secret_word:
                for i in range(1, len(secret_word) - 1):
                    if secret_word[i] == letter:
                        displayed_word = displayed_word[:i] + letter + displayed_word[i + 1:]
        return displayed_word
    else:
        letters = ["_" if letter not in guessed_letters else letter for letter in secret_word]
        return "".join(letters)
 



print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print("")
print ("Dificultad facil = 1")
print ("Dificultad media = 2")
print ("Dificultad dificil = 3")

dificultad= int(input("Elija su dificultad"))


# Mostrarla palabra en base a su dificultad
word_displayed = mostrar_palabra(dificultad,secret_word,guessed_letters)

print(f"Palabra: {word_displayed}") 


while fallos<max_fallos and word_displayed != secret_word: # corrección de que corte cuando la  palabra es adivinada
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     # Verificar si la letra ya ha sido adivinada
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word and letter != "": # corrección del bug
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         fallos+=1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = mostrar_palabra(dificultad,secret_word,guessed_letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta:  {secret_word}")
         break
else:
     print(f"¡Oh no! Has alcanzado tus {max_fallos} fallos.")
     print(f"La palabra secreta era: {secret_word}")