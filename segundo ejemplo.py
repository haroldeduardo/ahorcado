import random

palabras = ['java', 'python', 'javascript', 'css']

lenguaje = random.choice(palabras)
palabra_oculta = "_" * len(lenguaje)

intentos = 0
letras_adivinadas = []
while intentos < 6:

    letra = input("Ingresa una letra: ")
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra, ¡intenta otra!")
    elif letra in lenguaje:
        for i in range(len(lenguaje)):
            if lenguaje[i] == letra:
                palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i+1:]
        print("¡Bien hecho! La palabra es:", palabra_oculta)
        if "_" not in palabra_oculta:
            print("¡Felicidades, adivinaste la palabra!")
            break
    else:
        intentos += 1
        print("Letra incorrecta, te quedan", 6-intentos, "intentos.")
        letras_adivinadas.append(letra)
        if intentos == 1:
            print("  O")
        elif intentos == 2:
            print("  O")
            print("  |")
        elif intentos == 3:
            print("  O")
            print(" /|")
        elif intentos == 4:
            print("  O")
            print(" /|\\")
        elif intentos == 5:
            print("  O")
            print(" /|\\")
            print(" /")
        elif intentos == 6:
            print("  O")
            print(" /|\\")
            print(" / \\")
            print("Lo siento, no adivinaste la palabra. La palabra era", lenguaje)
            break