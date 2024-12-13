#!/usr/bin/env python3

import os
import random

"""
Jocs, El Rellotge

En aquest apartat, farem el joc del "Rellotge" amb cartes.

- El joc consisteix en que cada jugador té 12 cartes (48 cartes / 4 jugadors)
- El joc comença amb el comptador a 0
- A cada tirada el jugador posa una carta al centre (sense veure-la, la que té al damunt del seu bloc)
- A cada tirada el jugador compta un número de comptador un més que l'anterior, o 1 si l'anterior era 12
- Si el número del comptador coincideix amb el número de la carta, el jugador agafa totes les cartes del centre (les que s'han tirat abans)
- El joc acaba quan un jugador es queda sense cartes.
"""

# Aquesta funció neteja la pantalla, no la modifiquis
def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

clearScreen()

def genera_cartes():
    """
    Genera una baralla espanyola de 48 cartes.
    
    Retorna:
        cartes (list[list[int, str]]): Una llista amb totes les cartes de la baralla.
    Exemple:
        [[1, 'oros'], [1, 'copes'], [1, 'espases'], [1, 'bastos'], [2, 'oros'], [2, 'copes'], ... ]
    """
    min_num = 1
    max_num = 12
    pals = ["oros", "copes", "espases", "bastos"]
    cartes = []

    for pal in pals:
        for i in range(min_num, max_num + 1):
            carta = [i, pal]
            cartes.append(carta)
    
    return cartes

def barreja_cartes(cartes):
    """
    Barreja una baralla de cartes.
    
    Paràmetres:
        cartes (list[list[int, str]]): Una llista amb les cartes a barrejar.
        
    Retorna:
        cartes_barrejades (list[list[int, str]]): La llista de cartes barrejades.
    """
    cartes_barrejades = cartes.copy()
    random.shuffle(cartes_barrejades)
    return cartes_barrejades

def reparteix_cartes(cartes, nombre_jugadors, cartes_per_jugador):
    """
    Reparteix les cartes entre els jugadors i retorna les cartes restants.
    
    Paràmetres:
        cartes (list[list[int, str]]): La baralla de cartes.
        nombre_jugadors (int): El nombre de jugadors.
        cartes_per_jugador (int): El nombre de cartes per cada jugador.
        
    Retorna:
        cartes_restants (list[list[int, str]]): La baralla restant després de repartir.
        mans_jugadors (list[list[list[int, str]]]): Les cartes de cada jugador.
    """
    cartes_restants = barreja_cartes(cartes)
    mans_jugadors = []

    for num_jugador in range(nombre_jugadors):
        cartes = []
        for num_carta in range(cartes_per_jugador):
            carta_seleccionada = cartes_restants[0]
            cartes_restants.pop(0)
            cartes.append(carta_seleccionada)
        mans_jugadors.append(cartes)

    return cartes_restants, mans_jugadors

def jugada(comptador, numero_jugador, cartes_jugador, cartes_taula):
    """
    Realitza una jugada per al jugador actual i actualitza l'estat del joc.

    El jugador retira la carta superior de la seva mà i la col·loca al centre de la taula. 
    A continuació, es comprova si el valor de la carta coincideix amb el número que indica el comptador. 
    Si coincideix, el jugador recull totes les cartes del centre, incloent-hi la seva pròpia carta jugada. 
    En cas contrari, les cartes es mantenen al centre per a la següent ronda.

    Paràmetres:
        comptador (int): El valor actual del comptador (de 0 a 11), que determina el número a dir.
        numero_jugador (int): La posició del jugador en la llista de jugadors (index).
        cartes_jugador (list[list[int, str]]): Les cartes que el jugador té a la mà.
        cartes_taula (list[list[int, str]]): Les cartes que estan actualment al centre de la taula.

    Retorna:
        tuple: Conté els següents elements:
            - cartes_jugador (list[list[int, str]]): Les cartes restants a la mà del jugador després de la jugada.
            - cartes_taula (list[list[int, str]]): Les cartes actualitzades al centre de la taula.
            - ha_agafat_cartes (bool): Indica si el jugador ha recollit les cartes del centre (True) o no (False).
    """
    comptador = (comptador % 12) + 1
    ultima_carta = cartes_jugador[0]
    cartes_jugador.pop(0)
    cartes_taula.append(ultima_carta)
    ha_agafat_carta = False

    if ultima_carta[0] == comptador:
        cartes_jugador = cartes_jugador + cartes_taula
        cartes_taula.clear()
        ha_agafat_carta = True
    
    resultat = (cartes_jugador, cartes_taula, ha_agafat_carta)
    
    return resultat

def mostra_estat_joc(mans_jugadors):
    """
    Mostra l'estat actual del joc, indicant quantes cartes té cada jugador.

    Paràmetres:
        mans_jugadors (list[list[list[int, str]]]): Les cartes de cada jugador.

    Exemples:
        Jugador 0: 5 cartes, Jugador 1: 1 carta, Jugador 2: 1 carta, Jugador 3: 41 cartes        
        "Jugador 0: 8 cartes, Jugador 1: 3 cartes, Jugador 2: 19 cartes, Jugador 3: 18 cartes"
    """
    for jugador in range(len(mans_jugadors)):
        string = "cartes"
        if len(mans_jugadors[jugador]) == 1:
            string = "carta"
        if jugador == len(mans_jugadors) - 1:
            print(f"Jugador {jugador}: {len(mans_jugadors[jugador])} {string}")
        else:
            print(f"Jugador {jugador}: {len(mans_jugadors[jugador])} {string},", end=" ")

def mainRun():
    """
    Executa el joc del Rellotge.
    
    Aquest mètode implementa la lògica principal del joc, incloent:
    - Inicialització del joc
    - Bucle principal de joc
    - Quan un jugador guanya s'escriu: "\nEl jugador {guanyador} ha guanyat!"
    - Quan un jugador agafa cartes s'escriuen el número de 
      tirades seguides anterior: "\nTirades seguides: {tirades_seguides}"
    - Mostra de l'estat del joc després de cada ronda
    
    Retorna:
        No retorna res, només executa el joc fins que hi ha un guanyador.

    Exemple de sortida:
        Tirades seguides: 2
        Jugador 0: 3 cartes, Jugador 1: 13 cartes, Jugador 2: 22 cartes, Jugador 3: 10 cartes

        Tirades seguides: 3
        Jugador 0: 2 cartes, Jugador 1: 16 cartes, Jugador 2: 21 cartes, Jugador 3: 9 cartes

        El jugador 1 ha guanyat!
    """
    num_jugadors = 4
    num_cartes = 12

    cartes = genera_cartes()
    baralla, cartes_jugadors = reparteix_cartes(cartes, num_jugadors, num_cartes)
    cartes_taula = []
    comptador = 1
    tirades_seguides = 0
    guanyador = -1

    while guanyador == -1:
        tirada_seguida = True

        for num_jugador in range(num_jugadors):
            cartes_jugadors[num_jugador], cartes_taula, ha_agafat = jugada(comptador, num_jugador, cartes_jugadors[num_jugador], cartes_taula)

            if ha_agafat:
                tirada_seguida = False

            if len(cartes_jugadors[num_jugador]) == 0:
                guanyador = num_jugador
                tirada_seguida = False

        tirades_seguides = tirades_seguides + 1
        if not tirada_seguida:
            print(f"Tirades seguides: {tirades_seguides}")
            tirades_seguides = 0

        mostra_estat_joc(cartes_jugadors)
    
    print(f"\nEl jugador {guanyador} ha guanyat!")          

# No canvieu això o no passarà el test
if __name__ == "__main__":
    mainRun()