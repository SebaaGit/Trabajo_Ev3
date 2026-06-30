# Juego Cachipún + Karaoke 
# Henry Inzunza - Guillermo De la Cruz - Sebastian Pacheco
# mira henry

# IMPORTACIONES Biblioteca webbrowser
import webbrowser

# FUNCIÓN: CACHIPÚN
def cachipun():

    print("=== CACHIPÚN ===")
    print("1 = Piedra")
    print("2 = Papel")
    print("3 = Tijera")

    jugador1 = int(input("Jugador 1: "))
    jugador2 = int(input("Jugador 2: "))

    if jugador1 == jugador2:
        print("Empate")
        print("Ambos pueden elegir una canción")
        karaoke()

    elif (jugador1 == 1 and jugador2 == 3) or \
         (jugador1 == 2 and jugador2 == 1) or \
         (jugador1 == 3 and jugador2 == 2):

        print("Ganó Jugador 1")
        print("Jugador 1 elige la canción")
        karaoke()

    else:
        print("Ganó Jugador 2")
        print("Jugador 2 elige la canción")
        karaoke()


# FUNCIÓN: KARAOKE
def karaoke():

    archivo = open("canciones_Cachipún_Karaoke.txt", "r", encoding="utf-8")

    canciones = archivo.readlines()

    archivo.close()

    print("\n=== KARAOKE ===")

    i = 1
    for linea in canciones:

        datos = linea.strip().split("|")

        print(i, "-", datos[0])

        i = i + 1

    opcion = int(input("\nSeleccione una canción: "))

    linea_elegida = canciones[opcion - 1]

    datos = linea_elegida.strip().split("|")

    webbrowser.open(datos[1])

# INICIO DEL PROGRAMA
cachipun()

# Conceptos utilizados en el proyecto:
# Biblioteca webbrowser
# Funciones: cachipun() y karaoke()
# Variables
# Entrada de datos (input)
# Salida de datos (print)
# Condicionales (if, elif, else)
# Ciclo for
# Listas
# Archivos de texto (.txt)
