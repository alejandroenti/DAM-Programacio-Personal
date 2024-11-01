#!/usr/bin/env python3

import os
import platform
import random

"""
Jocs, Daus (amb llistes)

Aquest joc consisteix en:

- Es tiren dos daus cada torn, si la suma és parell, se sumen els punts del dau major i i si són imparells, es resten els del dau menor.

- Es tiren 50 vegades cadascun els daus i el que major puntuació treu, guanya.

- Si guanya l'usuari, s'afegeix el jugador i la seva puntuació al ranking.

- El ranking haurà d’estar ordenat.

- Al final de cada partida, caldrà resetejar el nom de l'usuari.

En aquesta versió el ranking es guarda en una llista d'aquest estil:

[["pepe",150],["Juan",100],["Pablo",50]]

"""

# Aquesta funció neteja la pantalla, no la modifiquis
def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

clearScreen()

def afegir_jugador(ranking, nom_jugador, nova_puntuacio):
    """
    Afegeix un nou jugador al rànquing o actualitza la seva puntuació si és més alta que l'actual.

    Paràmetres:
        ranking (list[list]): Llista que conté el rànquing de jugadors, on cada element és una llista amb el nom del jugador i la seva puntuació.
        nom_jugador (str): Nom del jugador que s'afegirà o actualitzarà al rànquing.
        nova_puntuacio (int): Puntuació del jugador.

    Retorna:
        list[list]: Retorna el rànquing actualitzat.

    Comportament:
        - Comprova si el jugador ja és al rànquing.
        - Si hi és, actualitza la seva puntuació només si la `nova_puntuacio` és més alta que l'actual.
        - Si no hi és, l'afegim amb la `nova_puntuacio`.

    Exemples:
        ranking = [["pepe", 150], ["Juan", 100]]
        afegir_jugador(ranking, "Pablo", 50)
        ranking serà [["pepe", 150], ["Juan", 100], ["Pablo", 50]]

        afegir_jugador(ranking, "Juan", 120)
        ranking serà [["pepe", 150], ["Juan", 120], ["Pablo", 50]]
    """
    for jugador in ranking:
        if jugador[0] == nom_jugador:
            if jugador[1] < nova_puntuacio:
                jugador[1] = nova_puntuacio
            return ranking
    
    ranking.append([nom_jugador, nova_puntuacio])

    return ranking

def escollir_jugador(ranking):
    """
    Permet a l'usuari escollir un jugador existent del rànquing.

    Paràmetres:
        ranking (list[list]): Llista que conté el rànquing de jugadors, on cada element és una llista amb el nom del jugador i la seva puntuació.

    Retorna:
        str: Retorna el nom del jugador escollit.

    Comportament:
        - Mostra una llista amb els noms dels jugadors disponibles.
        - L'usuari pot escollir un jugador introduint el número corresponent o escrivint el nom del jugador.
        - La funció no surt fins que es selecciona un jugador vàlid.
        - Retorna el nom del jugador seleccionat.

    Exemples:
        ranking = [["pepe", 150], ["Juan", 100]]
        escollir_jugador(ranking)
        "pepe" si l'usuari selecciona la primera opció o escriu "pepe".
    """
    if not ranking:
        print("No hi ha jugadors disponibles.")
        return None

    while True:
        # Mostrem la llista de jugadors
        for i, jugador in enumerate(ranking):
            print(f"{i + 1}) {jugador[0]}")

        # Demanem al jugador que esculli
        eleccio = input("\nEscull un jugador (número o nom): ").strip()

        # Comprovem si l'usuari ha introduït un número
        if eleccio.isdigit():
            index = int(eleccio) - 1
            if 0 <= index < len(ranking):
                return ranking[index][0]
            else:
                print("Número no vàlid, torna-ho a intentar.")

        # Comprovem si l'usuari ha introduït un nom vàlid
        else:
            for jugador in ranking:
                if jugador[0].lower() == eleccio.lower():
                    return jugador[0]

            print("Nom no vàlid, torna-ho a intentar.")

def mostrar_puntuacions(ranking):
    """
    Mostra les puntuacions actuals del rànquing de jugadors de manera ordenada.

    Paràmetres:
        ranking (list[list]): Llista que conté el rànquing de jugadors, on cada element és una llista amb el nom del jugador i la seva puntuació.

    Retorna:
        None: Aquesta funció no retorna res.

    Comportament:
        - Ordena el rànquing segons les puntuacions de manera descendent.
        - Mostra el rànquing amb els noms dels jugadors i les seves puntuacions en format tabular.

    Exemples:
        ranking = [["pepe", 150], ["Juan", 100], ["Pablo", 50]]
        mostrar_puntuacions(ranking)
        Sortida:
        ················ Ranking ················
        NOM                                 PUNTS
        *****************************************
        pepe                                  150
        Juan                                  100
        Pablo                                  50
    """
    ranking_ordenat = sorted(ranking, key=lambda jugador: jugador[1], reverse=True)

    print(f"{" Ranking ".center(41, "·")}")
    print(f"{"NOM".ljust(21)}{"PUNTS".rjust(20)}")
    print(f"{"".ljust(41, "*")}")
    for jugador in ranking_ordenat:
        print(f"{f"{jugador[0]}".ljust(21)}{f"{jugador[1]}".rjust(20)}")

def jugar(jugador):
    """
    Simula una partida entre el jugador i l'ordinador. Es tiren dos daus cada torn, 50 vegades.

    Paràmetres:
        jugador (str): Nom del jugador participant a la partida.

    Retorna:
        None: Aquesta funció no retorna res.

    Comportament:
        - Es tiren dos daus per torn, durant 50 torns per al jugador i l'ordinador.
        - Si la suma dels daus és parell, s'afegeixen els punts del dau major.
        - Si la suma dels daus és imparell, es resten els punts del dau menor.
        - El jugador o l'ordinador amb més punts després de 50 tirades guanya.
        - Al final, es mostra qui ha guanyat i amb quina puntuació.
    """
    primer_dau = None
    segon_dau = None

    puntuacio_jugador = 0
    puntuacio_ordinador = 0

    for torn in range(50):
        primer_dau = random.randint(1, 6)
        segon_dau = random.randint(1, 6)

        if (primer_dau + segon_dau) % 2 == 0:
            puntuacio_jugador += max(primer_dau, segon_dau)
        else:
            puntuacio_jugador -= min(primer_dau, segon_dau)
        
        primer_dau = random.randint(1, 6)
        segon_dau = random.randint(1, 6)

        if (primer_dau + segon_dau) % 2 == 0:
            puntuacio_ordinador += max(primer_dau, segon_dau)
        else:
            puntuacio_ordinador -= min(primer_dau, segon_dau)
    
    if puntuacio_jugador > puntuacio_ordinador:
        print(f"Ha guanyat el jugador \"{jugador}\"")
        return puntuacio_jugador
    else:
        print("Ha guanyat l'ordinador")
        return -1

def mainRun():
    """
    Mostra un menú principal per gestionar el joc de daus i permet interactuar amb les opcions del joc.

    Paràmetres:
        None: Aquesta funció no té paràmetres.

    Retorna:
        None: Aquesta funció no retorna res.

    Comportament:
        - Mostra les opcions disponibles: iniciar una nova partida, afegir un nou jugador, escollir un jugador, jugar, mostrar puntuacions o sortir del joc.
        - Si no hi ha jugadors al rànquing, l'opció d'escollir jugador no està disponible.
        - Si no s'ha escollit un jugador, l'opció de jugar no està disponible.
        - Es poden escollir les opcions del menú per número [0, 1, 2, 3, 4]
        - Es poden escollir les opcions del menú per text ['afegir', 'escollir', 'jugar', 'puntuacions', 'ranking', 'sortir']

    Textos:
        "\nEscull una opció: ": Per escollir la opció del menú
        "\nIntrodueix el nom del nou jugador: "
        "\nNo hi ha jugadors al rànquing. Afegiu-ne un primer."
        "\nNo s'ha escollit cap jugador."
        "Opció no vàlida."

    Exemples:
        1) Afegir jugador
        X) Escollir jugador
        X) Jugar ()
        4) Mostrar puntuacions
        0) Sortir

        1) Afegir jugador
        2) Escollir jugador
        3) Jugar (Pedrito)
        4) Mostrar puntuacions
        0) Sortir
    """
    ranking = []
    nom_jugador = None

    while True:
        print("""
1) Afegir jugador
2) Escollir jugador
3) Jugar (Pedrito)
4) Mostrar puntuacions
0) Sortir
        """)
        opcio = input("Escull una opció: ")

        if opcio == 0:
            break
        elif opcio == 1:
            nom = input("Introdueix el nom del nou jugador: ")
            afegir_jugador(ranking, nom, 0)
        elif opcio == 2:
            escollir_jugador(ranking)
        elif opcio == 3:
            if nom_jugador:
                jugar()
            else:
                print("No s'ha escollit cap jugador.")
        elif opcio == 4:
            if len(ranking) > 0:
                mostrar_puntuacions(ranking)
            else:
                print("No hi ha jugadors al rànquing. Afegiu-ne un primer.")
        else:
            print("Opció no vàlida.")

# No canvieu això o no passarà el test
if __name__ == "__main__":
    mainRun()