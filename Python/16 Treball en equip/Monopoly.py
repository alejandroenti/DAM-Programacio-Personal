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
def imprimeix_jugades(accions):
    # Imprimimos en el espacio central del tablero 10 líneas de acciones realizadas por los jugadores
    amplada = tauler_mesures["ampla_total"] - (tauler_mesures["ampla_partida"] * 2)
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