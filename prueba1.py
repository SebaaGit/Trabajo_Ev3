# IMPORTACIONES karaoke  Fiestas ,todo bien
import webbrowser
import os

# FUNCIÓN: KARAOKE (ARCHIVOS + LISTAS + MENÚ)
def karaoke():

# ARCHIVO: lectura del txt
    # Ruta absoluta basada en la ubicación del script
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(carpeta, "canciones.txt")
    
    archivo = open(ruta_archivo, "r", encoding="utf-8")
    canciones = archivo.readlines()
    archivo.close()

# MENÚ (LISTA DE CANCIONES)
    print("\n ELIGE UNA CANCIÓN:\n")

    i = 1
    for linea in canciones:
        datos = linea.strip().split("|")
        print(i, "-", datos[0])
        i += 1

# ENTRADA USUARIO
    opcion = int(input("\nSeleccione una canción: "))

# SELECCIÓN DE CANCIÓN
    linea_elegida = canciones[opcion - 1]
    datos = linea_elegida.strip().split("|")

# ACCIÓN FINAL (ABRIR LINK)
    webbrowser.open(datos[1])

# FUNCIÓN: CACHIPÚN (CONDICIONALES)
def cachipun():

# MENÚ DE JUEGO
    print("\n ELIGE TU JUGADA")
    print("1 = Piedra")
    print("2 = Papel")
    print("3 = Tijera")

# ENTRADA DE JUGADORES
    jugador1 = int(input("Jugador 1: "))
    jugador2 = int(input("Jugador 2: "))

# CONDICIONALES (REGLAS DEL JUEGO)
    if jugador1 == jugador2:
        print("Empate, ambos cantan")
        karaoke()

    elif (jugador1 == 1 and jugador2 == 3) or \
         (jugador1 == 2 and jugador2 == 1) or \
         (jugador1 == 3 and jugador2 == 2):

        print(" Ganó Jugador 1")
        karaoke()

    else:
        print(" Ganó Jugador 2")
        karaoke()
# EJECUCIÓN DEL PROGRAMA
cachipun()

# Importaciones: traen herramientas (webbrowser)
# Archivos: leen canciones.txt
# Listas: guardan canciones
# Ciclo for: muestra menú
# Condicionales: determinan ganador
# Funciones: separan el programa en partes
# Ejecución final: inicia el juego
# El becario juan lismoya