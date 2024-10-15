import sys
import os
from colorama import just_fix_windows_console # Paquete para que la terminal de Windows entienda los caràcteres ANSI y podamos mover el cursor a la posición que deseemos 

just_fix_windows_console()

MIN_DINERS_BANCA = 500000

tauler = {}
banca = 0
casella_mesures = {
    "alt": 2,
    "ampla": 8
}

tauler_mesures = {
    "ampla_total": 64,
    "ampla_partida": 10,
    "files": 7,
    "columnes": 7
}

jugadors = {
    "Vermell": {
        "nom": "Vermell",
        "icona": "V",
        "diners": 0,
        "posicio": [],
        "propietats": [],
        "es_preso": False,
        "cartes": []
    },
    "Groc": {
        "nom": "Groc",
        "icona": "G",
        "diners": 0,
        "posicio": [],
        "propietats": ["Gracia", "Pl Cat"],
        "es_preso": False,
        "cartes": []
    },
    "Taronja": {
        "nom": "Taronja",
        "icona": "T",
        "diners": 0,
        "posicio": [],
        "propietats": ["Aribau"],
        "es_preso": False,
        "cartes": []
    },
    "Blau": {
        "nom": "Blau",
        "icona": "B",
        "diners": 0,
        "posicio": [],
        "propietats": [],
        "es_preso": False,
        "cartes": ["Sortir preso"]
    }
}

caselles = {
    "Lauria": {
        "nom_acortat": "Lauria",
        "lloguer_casa": 10,
        "lloguer_hotel": 15,
        "preu_terreny": 50,
        "comprar_casa": 300,
        "comprar_hotel": 250
    },
}

posicions_caselles_files = [1, 5, 8, 11, 14, 17, 19]
posicions_caselles_columnes = [0, 10, 19, 28, 37, 45, 55]
posicions_separadors = [[0, 4], [0, 22]]
posicions_informacio = [[66, 1], [66, 4], [66, 9], [66, 14], [66, 19]]
posicio_estat = [5, 11]

def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def mou_cursor(x, y):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def afegir_diners_banca():
    # Añadimos dinero a la banca cuando esta no disponga de suficiente dinero (1.000.000€)
    pass

def gestiona_diners_banca():
    # Miramos la cantidad de dinero de la banca, si es menor a 5000.000€, llamaremos a afegir_diners_banca()
    pass

def ordre_tirada(jugadors):
    # Mezaclamos el diccionario de jugadores para que tengan un orden aleatorio
    pass

def primer_pagament(jugadors):
    # Añadimos a todos los jugadores 2000€ en sus cuentas
    pass

def crea_casella(nom, nom_acortat, jugadors, posicio, es_especial, opcions_especials, preu_casa, preu_hotel):
    # Genera una estructura de casilla
    casella = {
        "nom": f"{nom}",
        "acortado": f"{nom_acortat}",
        "cases": 0,
        "hotels": 0,
        "jugadores": f"{jugadors}",
        "posicio": posicio,
        "es_especial": es_especial,
        "opcions_especials": opcions_especials,
        "preu_casa": preu_casa,
        "preu_hotel": preu_hotel,
        "propietari": ""
    }
    
    # Añadimos la casilla generada al tablero
    tauler[nom] = casella

def imprimeix_separador():
    amplada = casella_mesures["ampla"]
    print(f"+{"".ljust(amplada, "-")}+{"".ljust(amplada, "-")}+{"".ljust(amplada, "-")}+{"".ljust(amplada, "-")}+{"".ljust(amplada, "-")}+{"".ljust(amplada, "-")}+{"".ljust(amplada, "-")}+")

def imprimeix_casella_vertical(nom, cases, hotels, jugadors, posicio):
    amplada = casella_mesures["ampla"]
    final_linia = "|"
    separador = f"+{"".ljust(amplada, "-")}+"

    string_final = f"{final_linia}"
    if cases > 0:
        amplada -= 1
        final_linia = f"{cases}C"

    string_final += f"{nom.ljust(amplada)}{final_linia}"
    mou_cursor(posicio[1], posicio[0])
    print(string_final)

    amplada = casella_mesures["ampla"]
    final_linia = "|"
    if hotels > 0:
        amplada -= 1
        final_linia = f"{hotels}H"
    string_final = "|"
    if len(jugadors) != 0:
        string_jugadors = ""
        for jugador in jugadors:
            string_jugadors += jugador
        string_final += f"{string_jugadors.ljust(amplada)}"
    else:
        string_final += f"{"".ljust(amplada)}"
    string_final += f"{final_linia}"
    mou_cursor(posicio[1], posicio[0] + 1)
    print(string_final)
    
    if posicio[0] != 17:
        string_final = f"{separador}"
        mou_cursor(posicio[1], posicio[0] + 2)
        print(string_final)

def imprimeix_casella_horizontal(nom, cases, hotels, jugadors, posicio):
    primera_linia = "+"
    if cases > 0:
        primera_linia += f"{"".ljust(4, "-")}{cases}C"
    else:
        primera_linia += f"".ljust(6, "-")

    if hotels > 0:
        primera_linia += f"{hotels}H+"
    else:
        primera_linia += f"".ljust(2, "-") + "+"
    
    amplada = casella_mesures["ampla"]
    final_linia = "|"
    if len(jugadors) != 0:
            string_jugadors = ""
            for jugador in jugadors:
                string_jugadors += jugador
            string_jugadors = string_jugadors.ljust(amplada)
    else:
        string_jugadors = "".ljust(amplada)

    if posicio[0] == 19:
        mou_cursor(posicio[1], posicio[0])
        print(primera_linia)

        mou_cursor(posicio[1], posicio[0] + 1)
        print(f"{final_linia}{string_jugadors}{final_linia}")

        mou_cursor(posicio[1], posicio[0] + 2)
        print(f"{final_linia}{nom.ljust(amplada)}{final_linia}")

    elif posicio[0] == 1:
        mou_cursor(posicio[1], posicio[0])
        print(primera_linia)

        mou_cursor(posicio[1], posicio[0] + 1)
        print(f"{final_linia}{nom.ljust(amplada)}{final_linia}")

        mou_cursor(posicio[1], posicio[0] + 2)
        print(f"{final_linia}{string_jugadors}{final_linia}")


def imprimeix_casella(nom, cases, hotels, jugadors, posicio):
    # Imprimimos por pantalla la casilla 
    # Gestionamos:
    #   - Impresión del nombre
    #   - Impresión del número de casas y hoteles
    #   - Impresión de los jugadores en la casilla
    # Miramos si la casilla debe tener la información en horizontal o en vertical
    if posicio[0] != 1 and posicio[0] != 19:
        imprimeix_casella_vertical(nom, cases, hotels, jugadors, posicio)
    else:
        imprimeix_casella_horizontal(nom, cases, hotels, jugadors, posicio)

def imprimeix_fila(fila_caselles):
    # Recibimos una fila del tablero.
    # Iteramos por la fila e imprimimos cada una de las casillas de la fila
    for casella in fila_caselles:
            imprimeix_casella(casella["nom_acortat"], casella["cases"], casella["hotels"], casella["jugadors"], casella["posicio"])

def imprimeix_taula(tauler):
    # Imprimimos del tablero, llamando cada de las fila con los separadores
    for index in posicions_caselles_files:
        fila = list(filter(lambda casella: casella["posicio"][0] == index, tauler))
        imprimeix_fila(fila)
    
    mou_cursor(posicions_separadors[0][0], posicions_separadors[0][1])
    imprimeix_separador()
    mou_cursor(posicions_separadors[1][0], posicions_separadors[1][1])
    imprimeix_separador()

def imprimeix_informacio_banca(banca):
    # Imprimimos la información de la banca
    #   Banca:
    #   Diners: 1838734
    mou_cursor(posicions_informacio[0][0], posicions_informacio[0][1])
    print("Banca: ")
    mou_cursor(posicions_informacio[0][0], posicions_informacio[0][1] + 1)
    print(f"Diners: {banca}")

def imprimeix_informacio_jugador(index, jugador):
    # Imprimimos la información de la banca
    #   Jugador Groc:
    #   Carrers: 2834
    #   Diners: 1838734
    #   Especial: (res) "Nombre de las cartas especiales"
    mou_cursor(posicions_informacio[index][0], posicions_informacio[index][1])
    print(f"Jugador {jugador["nom"]}: ")

    mou_cursor(posicions_informacio[index][0], posicions_informacio[index][1] + 1)
    print(f"Carrers: ", end="")
    longitud = len(jugador["propietats"])
    if longitud != 0:
        for index_, propietat in enumerate(jugador["propietats"]):
            print(f"{propietat}", end="")
            if index_ != longitud - 1:
                print(", ", end="")

    else:
        print("(res)")

    mou_cursor(posicions_informacio[index][0], posicions_informacio[index][1] + 2)
    print(f"Diners: {jugador["diners"]} ")

    mou_cursor(posicions_informacio[index][0], posicions_informacio[index][1] + 3)
    print(f"Especial: ", end="")
    longitud = len(jugador["cartes"])
    if longitud != 0:
        for index_, carta in enumerate(jugador["cartes"]):
            print(f"{carta}", end="")
            if index_ != longitud - 1:
                print(", ", end="")
    else:
        print("(res)")  

def imprimeix_informacio(banca, jugadors):
    # Gestiona la impresión a la izquierda del tablero
    # ¡MIRAR COMO CAMBIAR LA POSICIÓN DEL PUNTERO DE CONSOLA!
    imprimeix_informacio_banca(banca)

    for index, jugador in enumerate(jugadors.values()):
        imprimeix_informacio_jugador(index + 1, jugador)

def mira_propietari(casella_propietari, jugador):
    # Devuelva si el jugador es el propietario de la casilla o no
    pass

def cobra_casella(casella, jugador):
    # Miramos si la casilla tiene propietario:
    #   - En caso de no tener, no hacemos nada y continuamos
    #   - En caso de tener, deberemos reviasar su propietario:
    #       - Si es suya, no hacemos nada
    #       - Si es de otro jugador, deberemos hacerle pagar su valor en casas/hoteles
    pass

def imprimeix_jugades(accions):
    # Imprimimos en el espacio central del tablero 10 líneas de acciones realizadas por los jugadores
    amplada = tauler_mesures["ampla_total"] - (tauler_mesures["ampla_partida"] * 2)
    pass

def opcio_es_truc(opcio):
    # Miramos si tiene alguna opción de los trucos ('anar a')
    pass

def gestiona_truc(opcio):
    # Revismos que el truco se válido
    # Aplicamos el truco
    # Añadimos acción a la lista
    pass

def gestiona_accio_usuari():
    # Pedimos al usuario una acción
    # - Gestionamos trucos
    # Deberemos revisar en que posición se encuentra
    #   - En caso de que solo pueda 'passar', imprimiremos información y pasaremos de turno
    # Mostrar las acciones que puede realizar
    # Preguntar hasta optener opción válida
    # Gestionar opción y realizar acción correspondiente
    # Añadir dentro de acciones, que se deberán imprimir al acabar su turno
    pass

clearScreen()
caselles = [
    {
        "nom_acortat": "Gracia",
        "cases": 2,
        "hotels": 0,
        "jugadors": ["V"],
        "posicio": [19, 10]
    },
    {
        "nom_acortat": "Marina",
        "cases": 1,
        "hotels": 1,
        "jugadors": [],
        "posicio": [19, 0]
    },
    {
        "nom_acortat": "Aribau",
        "cases": 0,
        "hotels": 2,
        "jugadors": ["VGB"],
        "posicio": [17, 0]
    },
    {
        "nom_acortat": "Mallorca",
        "cases": 0,
        "hotels": 0,
        "jugadors": ["B"],
        "posicio": [5, 0]
    },
    {
        "nom_acortat": "Arago",
        "cases": 1,
        "hotels": 1,
        "jugadors": ["T"],
        "posicio": [1, 0]
    },
    {
        "nom_acortat": "Pl Cat",
        "cases": 4,
        "hotels": 2,
        "jugadors": ["TB"],
        "posicio": [1, 55]
    },
    {
        "nom_acortat": "Sants",
        "cases": 2,
        "hotels": 0,
        "jugadors": [""],
        "posicio": [5, 55]
    },
]

clearScreen()
imprimeix_taula(caselles)
imprimeix_informacio(banca, jugadors)
mou_cursor(0, 25)