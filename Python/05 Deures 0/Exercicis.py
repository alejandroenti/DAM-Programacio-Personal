import math

# Conversió de graus Celsius a Fahrenheit
# Fórmula: Fahrenheit = (Celsius * 9/5) + 32
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Conversió de graus Fahrenheit a Celsius
# Fórmula: Celsius = (Fahrenheit - 32) * 5/9
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Calcula l'Índex de Massa Corporal (IMC)
# Fórmula: IMC = pes / (altura ** 2)
def calcular_imc(pes, altura):
    return pes / pow(altura, 2)

# Calcula la hipotenusa d'un triangle rectangle
# Utilitza el teorema de Pitàgores: hipotenusa = sqrt(catet1^2 + catet2^2)
def calcular_hipotenusa(catet1, catet2):
    return math.sqrt(pow(catet1, 2) + pow(catet2, 2))

# Comprova si un nombre és parell
# Per fer-ho, fem nombre % 2 i retornem si el resultat és 0
def es_parell(nombre):
    return nombre % 2 == 0

# Calcula l'àrea d'un cercle donat el radi
# Fórmula: Àrea = π * radi^2
def area_cercle(radi):
    return math.pi * pow(radi, 2)

# Converteix minuts a hores i minuts
# Divideix minuts entre 60 per obtenir les hores i els minuts restants
def minuts_a_hores_minuts(minuts):
    hours = minuts // 60
    mins = minuts % 60
    return hours, mins

# Calcula el perímetre i l'àrea d'un rectangle
# Perímetre = 2 * (llargada + amplada)
# Àrea = llargada * amplada
def perimetre_i_area_rectangle(llargada, amplada):
    perimeter = 2 * (llargada + amplada)
    area = llargada * amplada
    return perimeter, area

# Calcula el preu final després d'un descompte percentual
# Preu final = preu inicial - (preu inicial * descompte_percent / 100)
def preu_final(preu_inicial, descompte_percent):
    return preu_inicial - (preu_inicial * (descompte_percent / 100))

# Calcula l'interès simple
# Fórmula: Interès = capital * (taxa / 100) * temps
def interes_simple(capital, taxa, temps):
    return capital * (taxa / 100) * temps

# Converteix velocitat de km/h a m/s
# Fórmula: m/s = km/h * 1000 / 3600
def kmh_a_ms(velocitat_kmh):
    return velocitat_kmh * 1000 / 3600

# Exercici 1
# Fes un programa amb una variable que tingui el següent text: "La programació és com l'art de resoldre problemes"
# Després manipula aquest text per aconseguir mostrar:
# * La llargada de la frase
# * La subcadena 'art' en majúscules
# * Les lletres inicials de cada paraula concatenades en una cadena
# * La frase completa en majúscules i després en minúscules
# * La frase invertida paraula per paraula
def exercici1():
    string = "La programació és com l'art de resoldre problemes"

    # La llargada de la frase
    length = len(string)
    print(f"La llargada de la frase és: {length}")

    # La subcadena 'art' en majúscules
    char_position = string.find("art")
    sub_string_art = string[char_position:char_position + 3]
    print(f"La subcadena 'art' en majúscules: {sub_string_art}")

    # Les lletres inicials de cada paraula concatenades en una cadena
    sub_string_initial_letters = "".join([word[0] for word in string.split(" ")])
    print(f"Les lletres inicials de cada paraula concatenades en una cadena: {sub_string_initial_letters}")

    # La frase completa en majúscules i després en minúscules
    print(f"La frase completa en majúscules i després en minúscules: \n\t{string.upper()}\n\t{string.lower()}")
    
    # La frase invertida paraula per paraula
    sub_string_reverse = "".join(string.split(" ")[::-1])
    print(f"La frase invertida paraula per paraula: {sub_string_reverse}")

# Exercici 2
# Fes un programa amb una variable que tingui el següent text: "Python és un llenguatge de programació potent i versàtil"
# Després manipula aquest text per aconseguir mostrar:
# * La posició de la paraula 'programació' dins la frase
# * Les paraules 'Python' i 'potent' concatenades en una sola paraula sense espais
# * La subcadena que comprèn des de 'un' fins a 'potent'
# * La frase amb totes les vocals reemplaçades per '*'
# * La frase amb la primera lletra de cada paraula en majúscula

# Fes servir ''.join(['*' if c in vocals else c for c in frase]) per canviar les vocals per '*'

def exercici2():
    string = "Python és un llenguatge de programació potent i versàtil"
    vowels = "aeiouàèéíòóúü"

    # La posició de la paraula 'programació' dins la frase
    char_position = string.find("programació")
    print(f"La posició de la paraula 'programació' dins la frase: {char_position}")

    # Les paraules 'Python' i 'potent' concatenades en una sola paraula sense espais
    sub_string_python = string[string.lower().find("python"):string.lower().find("python") + 6]
    sub_string_potent = string[string.find("potent"):string.find("potent") + 6]
    sub_string_concatenated = sub_string_python + sub_string_potent
    print(f"Les paraules 'Python' i 'potent' concatenades en una sola paraula sense espais: {sub_string_concatenated}")

    # La subcadena que comprèn des de 'un' fins a 'potent'
    sub_string_long = string[string.find("un"): string.find("potent") + 6]
    print(f"La subcadena que comprèn des de 'un' fins a 'potent': {sub_string_long}")

    # La frase amb totes les vocals reemplaçades per '*'
    string_without_vowels = "".join(['*' if letter.lower() in vowels else letter for letter in string])
    print(f"La frase amb totes les vocals reemplaçades per '*': {string_without_vowels}")

    # La frase amb la primera lletra de cada paraula en majúscula
    string_capitalize = string.title()
    print(f"La frase amb la primera lletra de cada paraula en majúscula: {string_capitalize}")

# Exercici 3
# Fes un programa amb una variable que tingui el següent text: "Aprendre a programar és com aprendre un nou idioma"
# Després manipula aquest text per aconseguir mostrar:
# * El nombre de vegades que apareix la paraula 'aprendre'
# * La frase amb la paraula 'idioma' reemplaçada per 'superpoder'
# * Les tres primeres paraules de la frase
# * La frase amb les paraules en ordre invers
# * La frase original però sense espais

def exercici3():
    string = "Aprendre a programar és com aprendre un nou idioma"

    # El nombre de vegades que apareix la paraula 'aprendre'
    learn_count = string.lower().count("aprendre")
    print(f"El nombre de vegades que apareix la paraula 'aprendre': {learn_count}")

    # La frase amb la paraula 'idioma' reemplaçada per 'superpoder'
    language_replace_string = string.replace("idioma", "superpoder")
    print(f"La frase amb la paraula 'idioma' reemplaçada per 'superpoder': {language_replace_string}")

    # Les tres primeres paraules de la frase
    three_words_string = ' '.join(string.split()[:3])
    print(f"Les tres primeres paraules de la frase: {three_words_string}")

    # La frase amb les paraules en ordre invers
    string_reverse = "".join(string.split()[::-1])
    print(f"La frase amb les paraules en ordre invers: {string_reverse}")

    # La frase original però sense espais
    string_without_spaces = string.replace(" ", "")
    print(f"La frase original però sense espais: {string_without_spaces}")  

# Exercici 4
# Fes un programa amb una variable que tingui el següent text: "El coneixement és poder"
# Després manipula aquest text per aconseguir mostrar:
# * La llargada de la frase
# * La paraula 'poder' en majúscules
# * La frase repetida tres vegades amb un espai entre elles
# * La frase amb les vocals eliminades
# * La posició de la primera 'e' i de la darrera 'e' en la frase

def exercici4():
    string = "El coneixement és poder"
    vowels = "aeiouàèéíòóúü"

    # La llargada de la frase
    length = len(string)
    print(f"La llargada de la frase: {length}")

    # La paraula 'poder' en majúscules
    initial_position = string.find("poder")
    final_position = initial_position + len("poder")
    sub_string_power = string[initial_position:final_position].upper()
    print(f"La paraula 'poder' en majúscules: {sub_string_power}")

    # La frase repetida tres vegades amb un espai entre elles
    string_repeated = (string + " ") * 2 + string
    print(f"La frase repetida tres vegades amb un espai entre elles: {string_repeated}")

    # La frase amb les vocals eliminades
    string_without_vowels = "".join([letter for letter in string if letter.lower() not in vowels])
    print(f"La frase amb les vocals eliminades: {string_without_vowels}")

    # La posició de la primera 'e' i de la darrera 'e' en la frase
    first_e_position = string.find("e")
    last_e_position = string.rfind("e")
    print(f"La posició de la primera 'e': {first_e_position}, i de la darrera 'e' en la frase: {last_e_position}")

# Exercici 5
# Fes un programa amb una variable que tingui el següent text: "La pràctica fa el mestre"
# Després manipula aquest text per aconseguir mostrar:
# * La frase amb cada paraula separada per un guió '-'
# * La frase amb l'ordre de les lletres de cada paraula invertit
# * La subcadena des del tercer fins al desè caràcter
# * La frase amb totes les consonants en majúscules i les vocals en minúscules
# * El nombre total de lletres sense comptar els espais

def exercici5():
    string = "La pràctica fa el mestre"
    vowels = "aeiouàèéíòóúü"
    
    # La frase amb cada paraula separada per un guió '-'
    string_hyphen = "-".join(string.split(" "))
    print(f"La frase amb cada paraula separada per un guió '-': {string_hyphen}")

    # La frase amb l'ordre de les lletres de cada paraula invertit
    string_word_reverse = " ".join([word[::-1] for word in string.split(" ")])
    print(f"La frase amb l'ordre de les lletres de cada paraula invertit: {string_word_reverse}")

    # La subcadena des del tercer fins al desè caràcter
    sub_string = string[2:10]
    print(f"La subcadena des del tercer fins al desè caràcter: {sub_string}")

    # La frase amb totes les consonants en majúscules i les vocals en minúscules
    string_upper_cons_lower_vow ="".join([letter.upper() if letter.lower() not in vowels else letter.lower() for letter in string ])
    print(f"La frase amb totes les consonants en majúscules i les vocals en minúscules: {string_upper_cons_lower_vow}")

    # El nombre total de lletres sense comptar els espais
    char_count = len(string.replace(" ", ""))
    print(f"El nombre total de lletres sense comptar els espais: {char_count}")

# Exercici 6
# Fes un programa amb una variable que tingui el següent text: "   En un lugar de la Mancha, de cuyo nombre no quiero acordarme   "
# Després manipula aquest text per aconseguir mostrar:
# * La frase original sense espais al principi ni al final
# * La frase amb un ample total de 80 caràcters, centrada, omplint amb '-'
# * La frase amb un ample total de 80 caràcters, alineada a l'esquerra, omplint amb '*'
# * La frase amb un ample total de 80 caràcters, alineada a la dreta, omplint amb '.'
# * La llargada de la frase original i de la frase després d'aplicar strip()

def exercici6():
    string = "   En un lugar de la Mancha, de cuyo nombre no quiero acordarme   "
    
    # La frase original sense espais al principi ni al final
    stripped_string = string.strip()
    print(f"La frase original sense espais al principi ni al final: {stripped_string}")

    # La frase amb un ample total de 80 caràcters, centrada, omplint amb '-'
    centered_string = stripped_string.center(80, "-")
    print(f"La frase amb un ample total de 80 caràcters, centrada, omplint amb '-': {centered_string}")

    # La frase amb un ample total de 80 caràcters, alineada a l'esquerra, omplint amb '*'
    left_string = stripped_string.ljust(80, "*")
    print(f"La frase amb un ample total de 80 caràcters, alineada a l'esquerra, omplint amb '*': {left_string}")

    # La frase amb un ample total de 80 caràcters, alineada a la dreta, omplint amb '.'
    right_string = stripped_string.rjust(80, ".")
    print(f"La frase amb un ample total de 80 caràcters, alineada a la dreta, omplint amb '.': {right_string}")

    # La llargada de la frase original i de la frase després d'aplicar strip()
    print(f"La llargada de la frase original: {len(string)}, i de la frase després d'aplicar strip(): {len(stripped_string)}")

# Exercici 7
# Fes un programa amb una variable que tingui el següent text: "****Benvinguts al curs de Python****"
# Després manipula aquest text per aconseguir mostrar:
# * La frase original sense els asteriscs del principi i del final
# * La frase sense els asteriscs només del principi
# * La frase sense els asteriscs només del final
# * La frase amb un ample total de 50 caràcters, centrada
# * La frase amb un ample total de 50 caràcters, alineada a la dreta

def exercici7():
    string = "****Benvinguts al curs de Python****"
    
    # La frase original sense els asteriscs del principi i del final
    stripped_string = string.strip("*")
    print(f"La frase original sense els asteriscs del principi i del final: {stripped_string}")

    # La frase sense els asteriscs només del principi
    left_stripped_string = string.lstrip("*")
    print(f"La frase sense els asteriscs només del principi: {left_stripped_string}")

    # La frase sense els asteriscs només del final
    right_stripped_string = string.rstrip("*")
    print(f"La frase sense els asteriscs només del principi: {right_stripped_string}")

    # La frase amb un ample total de 50 caràcters, centrada
    centered_string = string.center(50)
    print(f"La frase amb un ample total de 50 caràcters, centrada: {centered_string}")

    # La frase amb un ample total de 50 caràcters, alineada a la dreta
    right_string = string.rjust(50)
    print(f"La frase amb un ample total de 50 caràcters, alineada a la dreta: {right_string}")

# Exercici 8
# Fes un programa amb una variable que tingui el següent text: "    Python és genial    "
# Després manipula aquest text per aconseguir mostrar:
# * La frase original amb els espais del principi eliminats
# * La frase original amb els espais del final eliminats
# * La frase amb un ample total de 30 caràcters, alineada a l'esquerra, omplint amb '-'
# * La frase amb un ample total de 30 caràcters, alineada a la dreta, omplint amb '+'
# * La frase amb un ample total de 30 caràcters, centrada, omplint amb '*'

def exercici8():
    string = "    Python és genial    "
    
    # La frase original amb els espais del principi eliminats
    left_stripped_string = string.lstrip()
    print(f"La frase original amb els espais del principi eliminats: {left_stripped_string}")

    # La frase original amb els espais del final eliminats
    right_stripped_string = string.rstrip()
    print(f"La frase original amb els espais del final eliminats: {right_stripped_string}")

    # La frase amb un ample total de 30 caràcters, alineada a l'esquerra, omplint amb '-'
    left_string = string.strip().ljust(30, "-")
    print(f"La frase amb un ample total de 30 caràcters, alineada a l'esquerra, omplint amb '-': {left_string}")

    # La frase amb un ample total de 30 caràcters, alineada a la dreta, omplint amb '+'
    right_string = string.strip().rjust(30, "+")
    print(f"La frase amb un ample total de 30 caràcters, alineada a la dreta, omplint amb '+': {right_string}")
    
    # La frase amb un ample total de 30 caràcters, centrada, omplint amb '*'
    centered_string = string.strip().center(30, "*")
    print(f"La frase amb un ample total de 30 caràcters, centrada, omplint amb '*': {centered_string}")

# Exercici 9
# Crea un programa que mostri un menú tipus:
# *********************************Menú Principal*********************************
#             1. Veure perfil                         4. Configuració             
#          2. Canviar contrasenya                         5. Ajuda                
#                3. Sortir                            6. Tancar sessió  
# Sense utilitzar bucles 'for' ni 'while', i fent servir les funcions ljust, center, rjust, etc.
# El programa ha de mostrar el menú amb dues columnes d'opcions una al costat de l'altra.

def exercici9():
    print(f"{"Menú Principal".center(80, "*")}")
    print(f"{"1. Veure Perfil".center(40)}{"4. Configuració".center(40)}")
    print(f"{"2. Canviar contrasenya".center(40)}{"4. Ajuda".center(40)}")
    print(f"{"3. Sortir".center(40)}{"4. Tancar sessió".center(40)}")
