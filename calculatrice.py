#coding utf-8

"""
ptn c long par contre
ptdr 95% du code c'est des fonctions et le reste c'est une boucle et des variables 
cd desktop/fichiers python
python calculatrice.py
"""
from math import sqrt,pi
garder_resultat = False#permet de "skip" toute la partie de n1 quand on garde le resultat
calcul = False #permet d'éviter de meler la calculatrice et les fonctions
stockage_resultat = 0# sert pour le "garder le résultat" ->stocke le résultat
continuer = True#sert a continuer d'utiliser la calculatrice sans la remettre(non utilisé)


def commandes():
    print('cette calculatrice est composée de deux parties:')
    print("1)la calculatrice de base qui permet d'additioner(+),soustraire(-),multiplier(*),faire des divisions décimales(/) ou euclidiennes(//) et calculer des puissances(**)")
    print("2)les calculs spécifiques qu'il faut taper à la place de 1er nombre.pour l'instant il y a:")
    print(' -aire cercle(A)\n -périmetre cercle(B)\n -pythagore(C)\n -produit en croix(D)\n -moyenne(E)\n -volume sphère(F)\n -fibonacci(G)\n -nombre premier(H)\n -racine carré(I)\n -multiples(J)\n -diviseurs(K)\n -conversion décimal -> binaire(binaire)')  
    print("PS:pour arrêter d'ajouter des nombres dans la moyanne il suffit de rien taper")

temporaire = lambda:print("placeholder pcq j'ai trop la flemmme la")

def aire_cercle():#(de 24 à 120) toutes les fonctions sur les calculs spécifiques 
    global stockage_resultat
    rayon = float(input('>rayon ? ')) 
    rayon = rayon ** 2 * pi
    r2 = round(rayon, 2)
    if rayon != r2:
        print(f'> {rayon} ≈ {r2}')
    else:
        print('>>',rayon)
    stockage_resultat += r2

def Pcercle():
    global stockage_resultat
    rayon = float(input('>rayon? '))
    rayon *= 2 * pi
    print('>',rayon)
    r2 = round(rayon, 2)
    if rayon != r2:
        print(f'> {rayon} ≈ {r2}')
    else:
        print(f'> {rayon}')
    stockage_resultat += r2

def pythagore():
    global stockage_resultat
    v1 = float(input('côté 1? '))
    v2 = float(input('côté 2? '))
    v3 = (v1 * v1) + (v2 * v2)
    v3 = sqrt(v3)
    v1 = round(v3, 2)
    if v1 != v3:
        print(f'> {v3} ≈ {v1}')
    else:
        print(f'> {v3}')    
    stockage_resultat += v1

def pCroix():
    global stockage_resultat
    v1 = float(input("> "))
    v2 = float(input("> "))
    v3 = float(input("> "))
    v4 = v1 * v2 / v3
    round(v4, 2)
    print(f'>> {v4}')
    stockage_resultat += v4

def moyenne():
    global stockage_resultat
    somme_termes,nb_termes = 0,0
    while True:
        try:
            terme = int(input('> '))
            somme_termes += terme
            nb_termes += 1
        except:
            break
    moyenne = somme_termes / nb_termes
    arrondi = round(moyenne,2)
    if moyenne == arrondi:
        print(f'> {arrondi}')
    else:
        print(f'> {arrondi} ≈ {moyenne}')
    stockage_resultat += arrondi

def vSphere():
    global stockage_resultat
    v1 = float(input('> rayon: '))
    v2 = 4 * pi * (v1**3) / 3
    v3 = round(v2, 2)
    print(f'> volume = {v2} ≈ {v3}')
    stockage_resultat += v3

def fibonacci():
    global stockage_resultat
    n = int(input('entrez un nombre:')) 
    while n < 2:
        print('nombre non valide')
        n = int(input('entrez un nombre:')) 
    u0 = 0
    u1 = 1
    print('>>',u0)
    print('>>',u1)
    for nb in range(n - 1):
        u = u0 + u1
        print('>',u)
        u0 = u1
        u1 = u
    stockage_resultat += u

def n1er():
    global stockage_resultat
    n = int(input('>entrez un nombre:')) 
    while n < 2:
        print('>nombre non valide')
        n = int(input('>entrez un nombre:')) 
    for n3 in range(2,n // 2):
        if (n % n3) == 0:
            nb1 = False
            break
    if nb1 == 1:
        print('> ce nombre est un nombre premier')    
    elif nb1 == 0:
        print("> ce nombre n'est pas un nombre premier")
    stockage_resultat += n

def rcarre():
    global stockage_resultat
    n1 = sqrt(float(input('> ')))
    n2 = round(n1,2)
    if n1 == n2:
        print(f'>> {n1}')
    else:
        print(f'>> {n1} ≈ {n2}')
    stockage_resultat += n2

def multiples():
        try:
            n1 = round(float(input('> ')),2)
            n2 = int(input('>nb max: '))
        except:
            print('>> met que des nombres srx') 
        else:
            for n3 in range(1,n2 + 1):
                print(f'{n1} x {n3} = {n1 * n3}')

def diviseurs():
    while True:
        try:
            n1 = int(input('> '))
            print('>',end=' ')
            for i in range(1,n1):
                if n1 % i == 0:
                    print(f' {i} ',end=';')
            print(' ')
            break
        except:
            print('> met un nombre imbécile')

def binaire():
    nb_décimal,nb_binaire = int(input('> ')),[]
    while nb_décimal != 0:
        nb_binaire.append(nb_décimal % 2)
        nb_décimal //= 2
    nb_binaire.reverse()            
    print('>',end=' ')
    if nb_binaire == []:#donc à 0
        nb_binaire = ['0']
    for i in nb_binaire:
        print(i,end=' ')
    print(' ')       
    
def calculatrice():
    global stockage_resultat#}relie la partie hors fonction et interne a celle-ci
    global calcul           #}
    calcul = False#sinon si on faisait calculatrice puis fonctions bah calcul restait à true et il demandait n2
    if garder_resultat == False:#garder_resultat = false que quand on répond non a l'input garder le résultat
        n1 = input("> ")
        while n1 == "commandes":#(de 117 à 140)sert à détecter quel calcul faire
            commandes()
            n1 = input("> ")
        if "aire cercle" in n1 or n1 == 'A':
            aire_cercle()
        elif "périmetre cercle" in n1 or n1 == 'B':
            Pcercle()    
        elif 'pythagore' in n1 or n1 == 'C':
            pythagore()
        elif "produit en croix" in n1 or n1 == 'D':
            pCroix()
        elif 'moyenne' in n1 or n1 == 'E':
            moyenne()
        elif 'volume sphère' in n1 or n1 == 'F':
            vSphere()
        elif 'fibonacci' in n1 or n1 == 'G':
            fibonacci()
        elif 'nombre premier' in n1 or n1 == 'H':
            n1er()
        elif 'racine carré' in n1 or n1 == 'I':
            rcarre()
        elif 'multiples' in n1 or n1 == 'J':
            multiples()
        elif 'diviseurs' in n1 or n1 == 'K':
            diviseurs()    
        elif 'binaire' in n1 or n1 == 'L':
            binaire()
        else:
            try:
                n1 = float(n1)
                calcul = True#si calcul = False,la partie avec n2 se déclencherait mm avec les calculs spécifiques
            except ValueError:
                print('> met un nombre imbécile')
                calcul = False
    else:
        n1 = stockage_resultat
        calcul = True#j'écris ce commentaire il est 21:03 et je viens de sortir d'une heure au moins de réflexion apres 8 heures de cours donc la flemme d'expliquer
    
    if calcul == True:    
        signe = input(">> ")
        try:
            n2 = float(input("> "))
        except ValueError:
            print('>> met un nombre srx')
        else:    
            if "+" in signe:#(de 80 à 94)bah permet de calculer quoi...
                resultat = n1 + n2
                print('>',n1,"+",n2,"=",resultat)
            elif "-" in signe:
                resultat = n1 - n2
                print('>',n1,"-",n2,"=",resultat)
            elif signe == '*':
                resultat = n1 * n2
                print('>',n1,"*",n2,"=",resultat)
            elif signe == '/':
                if n2 == 0:
                    print('la division par 0 est impossible')
                else:
                    resultat = n1 / n2
                    print('>',n1,"/",n2,"=",resultat)
            elif signe == '**':
                resultat = n1 ** n2
                print('>',n1,"**",n2,"=",resultat)
            elif signe == '//':
                if n2 == 0:
                    print('la division par 0 est impossible')
                else:    
                    resultat = n1 // n2
                    reste = n1 % n2
                    print('>',n1,"//",n2,"=",resultat,'reste =',reste)
            else:
                print("l'opérateur est incorrect")
            stockage_resultat += resultat
    
    if garder_resultat == True and calcul == False:#donc si on skipe tout(arrive seulement si on garde le résultat après avoir utilisé une fonction)
        print(">> bah y'a pas de résultat la ptdr")

#petit rappel,tout ce que tu as lu jusqu'a maintenant c'est que des fonctions et des variables
print("Calculatrice:pour toute aide taper 'commandes'\nPS:ne pas mettre de majuscule dans les input ")
calculatrice()
#bon je vais résumer mais la boucle permet a la fin de chaque opération de demander si on veut continuer ou pas et si on veut garder le résultat
while True :
    question_calcul = input(">> continuer ? ")
    if 'non' in question_calcul:#si on veut arrêter quoi 
        print('>> au revoir') 
        break             
    else:#si on continue:
        question_resultat = input('>> garder le résultat ? ')# 1)on demande si on garde le résultat
        if 'oui' in question_resultat:
            garder_resultat = True# 2)si oui on skip la partie avec n1
        else:
            garder_resultat = False
        calculatrice() #3)et on "éxécute" la calculatrice
         