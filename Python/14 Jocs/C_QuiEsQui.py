#!/usr/bin/env python3

import os
import platform
import random

"""
Jocs, Qui és qui

- El joc consisteix en que cada jugador escull un personatge a l'atzar

- Cada jugador té un tauler amb els personatges

- Cada jugador ha d'endevinar el personatge de l'altre jugador

- Els jugadors es van provant caselles del rival fins que endevinen el personatge

- Qui endevina el personatge de l'altre jugador primer, guanya

"""

# Aquesta funció neteja la pantalla, no la modifiquis
def clearScreen():
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def genera_noms():
    """
        Genera i barreja una llista de noms aleatòriament fent servir 'shuffle'

    Retorna:
        list[str]: Una llista de 12 noms barrejats aleatòriament.

    Comportament:
        - Genera una llista amb els noms: ['Phillip', 'Susan', 'Herman', 'Anne', 'Claire', 'Richard', 'Tom', 'Max', 'Sam', 'Anita', 'Joe', 'Maria'].
        - Barreja els noms de manera aleatòria.
        - Retorna la llista barrejada.

    Exemples:
        genera_noms()
          # ['Tom', 'Maria', 'Anita', 'Phillip', ...]  (la llista ordenada aleatòriament)

    """
    noms = ['Phillip', 'Susan', 'Herman', 'Anne', 'Claire', 'Richard', 'Tom', 'Max', 'Sam', 'Anita', 'Joe', 'Maria']
    random.shuffle(noms)
    return noms

def escull_carta():
    """
        Selecciona l'últim nom d'una baralla generada de noms.

    Retorna:
        str: El nom que ocupa l'última posició de la baralla aleatòria.

    Comportament:
        - Genera una baralla amb la funció `genera_noms()`.
        - Retorna l'últim nom d'aquesta baralla.

    Exemples:
        escull_carta()
          # 'Maria'  (últim nom en la baralla generada)
    """
    noms = genera_noms()
    return noms[-1]

def genera_tauler():
    """
        Genera un tauler de joc 3x4 amb noms barrejats.

    Retorna:
        list[list[str]]: Un array 3x4 amb els noms barrejats.

    Comportament:
        - Genera una llista de noms amb la funció `genera_noms()`.
        - Crea una llista de llistes (3 files per 4 columnes) que representen el tauler del joc.
        - Els noms estan barrejats de manera aleatòria.

    Exemples:
        genera_tauler()
          # [['Phillip', 'Susan', 'Herman', 'Anne'],
             ['Claire', 'Richard', 'Tom', 'Max'],
             ['Sam', 'Anita', 'Joe', 'Maria']]  (noms aleatoris)
    """
    noms = genera_noms()
    tauler = []
    for i in range(3):
        columna = []
        for j in range(4):
            nom = random.choice(noms)
            columna.append(nom)
            noms.remove(nom)
        tauler.append(columna)
    
    return tauler

def genera_partida():
    """
        Genera els elements inicials d'una partida de "Qui és qui".
        El personatge de l'usuari i el del jugador s'escullent independentment
        un de l'altre.

    Retorna:
        list: Una llista amb quatre elements:
            1) El personatge seleccionat per l'usuari.
            2) El personatge seleccionat per l'ordinador.
            3) El tauler de l'usuari (3x4).
            4) El tauler de l'ordinador (3x4).

    Comportament:
        - Utilitza la funció `escull_carta()` per seleccionar el personatge de l'usuari i el de l'ordinador.
        - Genera els taulers de l'usuari i de l'ordinador amb la funció `genera_tauler()`.
        - Retorna els quatre elements en una llista.

    Exemples:
        genera_partida()
          # ['Maria', 'Tom', [['Phillip', 'Susan', 'Herman', 'Anne'], ...], [['Claire', 'Richard', 'Tom', 'Max'], ...]]
    """
    usuari = escull_carta()
    ordinador = escull_carta()
    tauler_usuari = genera_tauler()
    tauler_ordinador = genera_tauler()
    
    resultat = [usuari, ordinador, tauler_usuari, tauler_ordinador]
    return resultat

def escriu_nom():
    """
        Demana a l'usuari que introdueixi un nom vàlid.

        Retorna:
            str: El nom introduït per l'usuari sense números.

        Comportament:
            - Mostra el missatge "Escriu el teu nom: " i demana a l'usuari que introdueixi un nom.
            - No permet noms que continguin números.
            - Torna a demanar el nom si aquest és invàlid.
            - Mostra un missatge d'error si el nom conté números.
            - Retorna el nom vàlid quan l'usuari l'introdueix correctament.
            - Si el nom no és vàlid mostra els següent missatge i torna a "Escriu el teu nom..."
                "Error: El nom no pot contenir números. Torna a provar."

        Exemples:
            escriu_nom()
              # 'Albert' (si l'usuari introdueix un nom vàlid)
    """
    while True:
        nom_introudit = input("Escriu el teu nom: ")
        if nom_introudit.isalpha() or nom_introudit == "" or " " in nom_introudit:
            return nom_introudit
        else:
            print("Error: El nom no pot contenir números. Torna a provar.")


def selecciona_oponent():
    """
        Permet a l'usuari escollir un oponent d'una llista de noms.

    Retorna:
        str: El nom de l'oponent seleccionat per l'usuari.

    Comportament:
        - Mostra una llista d'oponents possibles: ['Romulus', 'Tarpeia', 'Horatius', 'Cloelia', 'Brutus', 'Lucretia'].
        - Demana a l'usuari que seleccioni un nom de la llista.
        - Si l'usuari introdueix un nom incorrecte, es neteja la pantalla 
          i es mostra un missatge d'error: "Error! Selecciona un oponent vàlid."
        - Repeteix el procés fins que l'usuari introdueix un nom vàlid.

    Exemples:
        selecciona_oponent()
          # 'Brutus' (si l'usuari selecciona un nom vàlid de la llista)
    """
    oponents = ['Romulus', 'Tarpeia', 'Horatius', 'Cloelia', 'Brutus', 'Lucretia']

    while True:
        for i in range(len(oponents)):
            if i == len(oponents) - 1:
                print(oponents[i])
            else:
                print(oponents[i], end=", ")
        oponent = input("Selecciona un nom de la llista: ")

        if oponent not in oponents:
            clearScreen()
            print("Error! Selecciona un oponent vàlid.")
        else:
            clearScreen()
            return oponent

def dibuixa_tauler_secret(tauler, descoberts):
    """
        Dibuixa el tauler secret de l'oponent. 
        La funció no retorna res, només dibuixa el tauler.

    Paràmetres:
        tauler (list[list[str]]): El tauler de l'oponent.
        descoberts (set): Un conjunt de tuples que representen les posicions ja descobertes.

    Retorna:
        None: La funció només dibuixa el tauler secret a la consola.

    Comportament:
        - Mostra el tauler de l'oponent amb les posicions descobertes indicades per 'X' i les no descobertes per '?'.
        - Les posicions s'indiquen amb lletres (files) i números (columnes).

    Exemples:
        tauler = [['Phillip', 'Susan', 'Herman', 'Anne'], ['Claire', 'Richard', 'Tom', 'Max'], ['Sam', 'Anita', 'Joe', 'Maria']]
        descoberts = {(0, 0), (1, 1)}
        
        dibuixa_tauler_secret(tauler, descoberts)
          # Mostra el tauler a la consola així:
          #  0 1 2 3
          # A X ? ? ?
          # B ? X ? ?
          # C ? ? ? ?
    """
    nums = ["0", "1", "2", "3"]
    lletres = ["A", "B", "C"]
    print(" ", end="")
    for num in range(len(nums)):
        print(f" {num}", end="")
    print()

    for fila in range(3):
        print(f"{lletres[fila]}", end="")
        for columna in range(4):
            simbol = "?"
            if (fila, columna) in descoberts:
                simbol = "X"
            print(f" {simbol}", end="")
        print()


def fila_columna(posicio):
    """
    Converteix una posició en format text (per exemple, "A0") en coordenades de fila i columna.

    Paràmetres:
        posicio (str): La posició en format text (per exemple, "A0").

    Retorna:
        tuple[int, int] | int: Una tupla (fila, columna) si la posició és vàlida, o -1 si no és vàlida.

    Comportament:
        - Verifica que la posició tingui exactament 2 caràcters.
        - Converteix la lletra de la fila (A, B, C) en un número (0, 1, 2).
        - Converteix el número de la columna (0-3) en l'índex corresponent.
        - Retorna les coordenades de la posició o -1 si la posició no és vàlida.
        - Gestiona errors per a entrades no vàlides (per exemple, lletres en lloc de números per a la columna).

    Exemples:
        fila_columna("A0") -> (0, 0)
        fila_columna("B2") -> (1, 2)
        fila_columna("C3") -> (2, 3)
        fila_columna("D0") -> -1 (fila no vàlida)
        fila_columna("A4") -> -1 (columna no vàlida)
        fila_columna("AA") -> -1 (columna no numèrica)
        fila_columna("") -> -1 (entrada buida)
    """
    files = {'A': 0, 'B': 1, 'C': 2}
    pos = (-1, -1)

    if len(posicio) != 2:
        return -1
    

    if posicio[0].isnumeric() or not posicio[1].isnumeric():
        return -1
    
    if posicio[0].upper() not in files.keys():
        return -1

    fila = files[posicio[0].upper()]
    columna = int(posicio[1])

    if columna < 0 or columna > 3:
        return -1
    
    pos = (fila, columna)
    return pos

def posicio_valida(posicio, descoberts):
    """
        Comprova si una posició és vàlida i no ha estat descoberta.

    Paràmetres:
        posicio (str): La posició en format text (per exemple, "A0").
        descoberts (set): Un conjunt de tuples que representen les posicions ja descobertes.

    Retorna:
        bool: True si la posició és vàlida i no ha estat descoberta, False altrament.

    Comportament:
        - Comprova si la posició és vàlida (format correcte i dins dels límits del tauler).
        - Comprova si la posició no ha estat descoberta prèviament.

    Exemples:
        descoberts = {(0, 0), (1, 1)}
        posicio_valida("A0", descoberts)
          # False (la posició ja ha estat descoberta)
    """
    pos = fila_columna(posicio)

    if pos in descoberts or pos == -1:
        return False
    
    return True

def jugada_usuari(tauler_oponent, descoberts):
    """
        Permet a l'usuari realitzar una jugada en el tauler de l'oponent.

    Paràmetres:
        tauler_oponent (list[list[str]]): El tauler de l'oponent.
        descoberts (set): Un conjunt de tuples que representen les posicions ja descobertes.

    Retorna:
        str: El nom del personatge en la posició seleccionada.

    Comportament:
        - Dibuixa el tauler secret de l'oponent.
        - Demana a l'usuari que introdueixi una posició.
        - Comprova si la posició és vàlida.
        - Si és vàlida, descobreix el personatge i retorna el seu nom.
        - Si no és vàlida escriu el següent text i torna a demanar la posició.
          "Posició no vàlida. Torna a provar."

    Exemples:
        descoberts = {(0, 0)}
        tauler_oponent = [['Phillip', 'Susan', 'Herman', 'Anne'], ...]
        
        jugada_usuari(tauler_oponent, descoberts)
          # Demana la posició a descobrir
    """
    while True:
        dibuixa_tauler_secret(tauler_oponent, descoberts)
        posicio = input("Introdueix una posicio: ")

        if posicio_valida(posicio, descoberts):
            fila, columna = fila_columna(posicio)
            descoberts.add((fila, columna))
            return tauler_oponent[fila][columna] 
        else:
            print("Posició no vàlida. Torna a provar.")

def jugada_oponent(tauler_usuari, descoberts):
    """
        Realitza la jugada de l'ordinador en el tauler de l'usuari.

    Paràmetres:
        tauler_usuari (list[list[str]]): El tauler de l'usuari.
        descoberts (set): Un conjunt de tuples que representen les posicions ja descobertes per l'ordinador.

    Retorna:
        str: El nom del personatge en la posició seleccionada.

    Comportament:
        - L'ordinador selecciona aleatòriament una posició en el tauler de l'usuari.
        - Comprova si la posició és vàlida (no descoberta).
        - Si és vàlida, descobreix el personatge i retorna el seu nom.
        - Si no és vàlida, repeteix el procés fins trobar una posició vàlida.

    Exemples:
        descoberts = set()
        tauler_usuari = [['Phillip', 'Susan', 'Herman', 'Anne'], ...]
        
        jugada_oponent(tauler_usuari, descoberts)
          # Retorna el personatge seleccionat per l'ordinador.
    """
    while True:
        fila = random.randint(0, 3)
        columna = random.randint(0, 4)

        if (fila, columna) not in descoberts:
            descoberts.add((fila, columna))
            return tauler_usuari[fila][columna]

def esborra_del_tauler(tauler, nom):
    """
        Esborra un personatge del tauler.

    Paràmetres:
        tauler (list[list[str]]): El tauler on es vol esborrar el personatge.
        nom (str): El nom del personatge que es vol esborrar.

    Retorna:
        None: La funció només modifica el tauler.

    Comportament:
        - Busca el personatge en el tauler.
        - Substitueix el nom per una cadena buida ("") si el troba.

    Exemples:
        tauler = [['Phillip', 'Susan', 'Herman', 'Anne'], ...]
        esborra_del_tauler(tauler, 'Phillip')
          # El tauler tindrà la posició de 'Phillip' buida.
    """
    for fila in tauler:
        for columna in range(len(fila)):
            if fila[columna] == nom:
                fila[columna] = ""

def joc_del_qui_es_qui():
    """
    Inicia i controla el joc de "Qui és qui".

    Comportament:
        - Genera una partida amb `genera_partida()`.
        - Alterna torns entre el jugador i l'ordinador fins que un d'ells encerta el personatge de l'altre.
        - Declara el guanyador quan s'encerta el personatge i escriu: 
          "Has guanyat!" o bé "L'ordinador ha guanyat!"
        - Després de guanyar, demana a l'usuari si vol tornar a jugar o tornar al menú.
          "Vols tornar a jugar (j) o tornar al menú (m)? "
        - Si l'usuari no escriu (j) o (m):
          "Opció no vàlida. Si us plau, escriu 'j' per jugar de nou o 'm' per tornar al menú."

    Exemples:
        joc_del_qui_es_qui()
            # Comença el joc i alterna els torns fins que hi ha un guanyador.
    """
    al_menu = False

    while not al_menu:
        usuari, ordinador, tauler_usuari, tauler_ordinador = genera_partida()
        usuari_descobert = []
        ordinador_descobert = []

        while True:
            nom = jugada_usuari(tauler_ordinador, usuari_descobert)
            if nom == ordinador:
                print("Has guanyat!")
                break
            else:
                esborra_del_tauler(tauler_ordinador, nom)

            nom = jugada_oponent(tauler_usuari, ordinador_descobert)
            if nom == usuari:
                print("L'ordinador ha guanyat!")
                break
            else:
                esborra_del_tauler(tauler_usuari, nom)
        
        while True:
            opcio = input("Vols tornar a jugar (j) o tornar al menú (m)? ").lower()
            if opcio == "j":
                break
            elif opcio == "m":
                al_menu = True
                break
            else:
                print("Opció no vàlida. Si us plau, escriu 'j' per jugar de nou o 'm' per tornar al menú.")
    
def mainRun():
    """
        Mostra el menú principal del joc "Qui és qui?".

    Comportament:
        - Mostra un menú amb les opcions: escollir nom, escollir oponent, jugar o sortir.
        - Si no s'ha seleccionat un nom o oponent, mostra un missatge d'error.
        - Després de jugar, retorna al menú.

    Exemples:
        mostra_menu()
            Qui és qui?
            1) Escull el teu nom
            2) Escull el nom de l'oponent
            3) Juga
            0) Sortir
            Escull una opció:
    """
    nom = None
    oponent = None
    
    while True:
        clearScreen()
        print("""
Qui és qui?
1) Escull el teu nom
2) Escull el nom de l'oponent
3) Juga
0) Sortir
        """)
        opcio = int(input("Escull una opció: "))

        if opcio == 1:
            nom = escriu_nom()
        elif opcio == 2:
            oponent = selecciona_oponent()
        elif opcio == 3:
            if nom and oponent:
                joc_del_qui_es_qui()
            else:
                print("Error! Has d'escollir el nom i l'oponent abans de jugar.")
        elif opcio == 0:
            break
        else:
            print("Opció no vàlida.")

# No canvieu això o no passarà el test
if __name__ == "__main__":
    mainRun()