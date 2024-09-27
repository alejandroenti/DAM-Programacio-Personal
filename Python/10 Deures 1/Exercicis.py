#!/usr/bin/env python3
import os
import random

def clearScreen():
    if os.name == 'nt':  # Si estàs en Windows
        os.system('cls')
    else:  # Si estàs en Linux o macOS
        os.system('clear')
clearScreen()

# Fes un programa que permeti a l'usuari introduir números i operacions. 
# El programa suma aquests números i mostra la suma 
# acumulada després de cada entrada. Si l'usuari escriu "sortir", 
# el programa acaba i mostra la suma final.
def suma_infinit():
    stop_demanding_numbers = False
    total_sum = 0

    while not stop_demanding_numbers:
        user_num = input("Introdueix el següent número a sumar [SORTIR per acabar]: ")

        if user_num.lower() == "sortir":
            stop_demanding_numbers = True
            print("Sortint...")
            print(f"La suma final és: {total_sum}")
            continue

        try:
            total_sum += float(user_num)
            print(f"La suma de tots els números introduits és {total_sum}")
        except Exception:
            print("S'han d'introduir números o la paraula SORTIR")

# Escull un número aleatori entre 1 i 25, després fes que el programa multipliqui 
# aquest número per 2 repetidament, mostrant el resultat a cada iteració. 
# El bucle acaba quan el resultat supera 100. 
# Finalment retorna el número d'iteracions que han fet falta.
def multiplica_fins_100():
    num = random.randint(1, 25)
    stop_multiply = False
    multiply_times = 0

    print(f"El número inicial és: {num}")

    while not stop_multiply:
        num *= 2
        multiply_times += 1
        print(f"Resultat actual: {num}")

        if num >= 100:
            stop_multiply = True

    print(f"'Han fet falta {multiply_times} iteracions per superar 100.")
    return multiply_times

# Fes un programa que mostri el següent menú
# Menú:
# 1 Saludar
# 2 Presentar
# 3 Vacilar
# 0 Sortir
# L'usuari ha de poder escriure el número o la opció (ignorant les majúscules)
# La opció 1 escriu "Hola colega"
# La opció 2 escriu "Sóc un programa molón"
# La opció 3 escriu "Pfff" o "De què vas?" de manera aleatòria
# La opció 0 surt del programa
def gestionar_menu():
    exit = False

    while not exit:
        print("""
Menú:
1 Saludar
2 Presentar
3 Vacilar
0 Sortir
        """)

        opt = input("Introdueix una opció: ")
        print()

        if opt == "0" or opt.lower() == "sortir":
            exit = True
            print("Sortint del programa...")
        elif opt == "1" or opt.lower() == "saludar":
            print("Hola colega")
        elif opt == "2" or opt.lower() == "presentar":
            print("Sóc un programa molón")
        elif opt == "3" or opt.lower() == "vacilar":
            phrase = random.randint(1,2)
            print("Pfff")
            if phrase == 1:
                print("De què vas?")
                
        else:
            print("Opció no vàlida, torna-ho a provar.")

# Fes un programa que a partir de dos numeros aleatoris 
# entre 1 i 5 els ordena de major a menor i escriu 
# (X guions pel primer número, separats d'un espai) 
# tantes vegades com el segon número
def guions_ordenats():
    min_num_random = random.randint(1,5)
    max_num_random = random.randint(1,5)
    string = ""

    if min_num_random > max_num_random:
        tmp = min_num_random
        min_num_random = max_num_random
        max_num_random = tmp
    
    for i in range(max_num_random):
        for j in range(min_num_random):
            string += "-"
        string += " "

    print(f"{string}")

# Fes un programa que esculli una operació a l'atzar 
# (suma, resta, multiplicació i divisió). 
# Esculli dos números entre 1 i 10 a l'atzar i aleshores 
# apliqui la operació sobre el primer número 
# les vegades indicades pel segon número.
# Si la operació és dividir i el divisor és 0, ha de dir:
# No es pot dividir per 0
def operacio_aleatoria():
    oprs = ["suma", "resta", "multiplicacio", "divisio"]
    opr = random.choice(oprs)
    random_num_1 = random.randint(0,10)
    random_num_2 = random.randint(0,10)
    result = random_num_1

    print(f"Operació: {opr}, Número inicial: {random_num_1}, Vegades: {random_num_2}")

    if opr == 'suma':
        for i in range(random_num_2):
            result += random_num_1
    elif opr == 'resta':
        for i in range(random_num_2):
            result -= random_num_1
    elif opr == 'multiplicacio':
        for i in range(random_num_2):
            result *= random_num_1
    elif opr == 'divisio':
        if random_num_1 == 0:
            print("No es pot dividir per 0.")
        else:
            for i in range(random_num_2):
                    result /= random_num_1
    
    print(f"El resultat final és: {result}")
