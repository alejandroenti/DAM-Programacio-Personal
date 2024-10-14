import sys
import os

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
    "alt": 7
}
jugadors = {
    "Vermell": {
        "icona": "V",
        "diners": 0,
        "posicio": [],
        "propietats": [],
        "es_preso": False,
        "cartes": []
    },
    "Groc": {
        "icona": "G",
        "diners": 0,
        "posicio": [],
        "propietats": [],
        "es_preso": False,
        "cartes": []
    },
    "Taronja": {
        "icona": "T",
        "diners": 0,
        "posicio": [],
        "propietats": [],
        "es_preso": False,
        "cartes": []
    },
    "Blau": {
        "icona": "B",
        "diners": 0,
        "posicio": [],
        "propietats": [],
        "es_preso": False,
        "cartes": []
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

def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

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

def imprimeix_casella_vertical(nom, cases, hotels, jugadors, fila):
    amplada = casella_mesures["ampla"]
    final_linia = "|"
    separador = f"+{"".ljust(amplada, "-")}+"

    
    string_final = f"{final_linia}"
    if cases > 0:
        amplada -= 1
        final_linia = f"{cases}C"

    string_final += f"{nom.ljust(amplada)}{final_linia}\n"
    amplada = casella_mesures["ampla"]
    final_linia = "|"
    if hotels > 0:
        amplada -= 1
        final_linia = f"{hotels}H"
    string_final += "|"
    if len(jugadors) != 0:
        string_jugadors = ""
        for jugador in jugadors:
            string_jugadors += jugador
        string_final += f"{string_jugadors.ljust(amplada)}"
    else:
        string_final += f"{"".ljust(amplada)}"
    string_final += f"{final_linia}"
    
    if fila != 1:
        string_final += f"\n{separador}"

    print(string_final)

def imprimeix_casella_horizontal(nom, cases, hotels, jugadors, fila):
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
    separador = f"+{"".ljust(amplada, "-")}+"
    if len(jugadors) != 0:
            string_jugadors = ""
            for jugador in jugadors:
                string_jugadors += jugador
            string_jugadors = string_jugadors.ljust(amplada)
    else:
        string_jugadors = "".ljust(amplada)

    if fila == 0:
        string_final = f"{primera_linia}\n{final_linia}{string_jugadors}"
        string_final += final_linia + "\n"
        string_final += f"|{nom.ljust(amplada)}{final_linia}"
    elif fila == tauler_mesures["alt"] - 1:
        string_final = f"{primera_linia}\n{final_linia}{nom.ljust(amplada)}{final_linia}\n"
        string_final += f"|{string_jugadors}{final_linia}"

    print(string_final)

def imprimeix_casella(nom, cases, hotels, jugadors, posicio):
    # Imprimimos por pantalla la casilla 
    # Gestionamos:
    #   - Impresión del nombre
    #   - Impresión del número de casas y hoteles
    #   - Impresión de los jugadores en la casilla
    # Miramos si la casilla debe tener la información en horizontal o en vertical
    if posicio[0] != 0 and posicio[0] != tauler_mesures["alt"] - 1:
        imprimeix_casella_vertical(nom, cases, hotels, jugadors, posicio[0])
    else:
        imprimeix_casella_horizontal(nom, cases, hotels, jugadors, posicio[0])

def imprimeix_fila(fila_caselles):
    # Recibimos una fila del tablero.
    # Iteramos por la fila e imprimimos cada una de las casillas de la fila
    if len(fila_caselles) == 2:
        pass
    else:
        pass

def imprimeix_taula(tauler):
    # Imprimimos del tablero, llamando cada de las fila con los separadores
    pass

def imprimeix_informacio_banca(banca):
    # Imprimimos la información de la banca
    #   Banca:
    #   Diners: 1838734
    pass

def imprimeix_informacio_jugador(jugador):
    # Imprimimos la información de la banca
    #   Jugador Groc:
    #   Carrers: 2834
    #   Diners: 1838734
    #   Especial: (res) "Nombre de las cartas especiales"
    pass

def imprimeix_informacio(banca, jugadors):
    # Gestiona la impresión a la izquierda del tablero
    # ¡MIRAR COMO CAMBIAR LA POSICIÓN DEL PUNTERO DE CONSOLA!
    pass

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

def mou_cursor(x, y):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

clearScreen()
imprimeix_casella("Marina", 1, 2, ["V"], [6, 10])
print(f"+{"".ljust(8, "-")}+")
mou_cursor(11, 0)
imprimeix_casella("Sants", 3, 2, [], [0, 9])
mou_cursor(11, 4)
print(f"+{"".ljust(8, "-")}+")
mou_cursor(0,5)
imprimeix_casella("Gracia", 0, 0, [], [2, 9])
mou_cursor(0, 8)
imprimeix_casella("Gracia", 1, 3, ["V"], [1, 9])
mou_cursor(0, 10)
imprimeix_casella("Marina", 0, 2, [], [0, 9])
print(f"+{"".ljust(8, "-")}+")