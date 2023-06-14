#coding utf-8

"""
"""

from colorama import Fore
from random import randint
from os import system
from time import sleep


def def_taille_map():
    global nb_colonnes,nb_lignes
    nb_lignes = int(input(f'{Fore.RED}> nb de lignes : ')) 
    nb_colonnes = int(input('> nb de colonnes : '))
    
    if nb_colonnes * nb_lignes < 25:
        print(f"{Fore.MAGENTA}>> L'aire minimale de la carte est de 25.Dans ce cas, l'aire est de {nb_lignes * nb_colonnes}")
        def_taille_map()
    
    def_persos()
    créer_carte()



class Joueur:
    def __init__(self):
        self.x = nb_colonnes // 2
        self.y = nb_lignes // 2
        self.x_affiché = 0
        self.y_affiché = 0
        self.sprite = f'{Fore.BLUE}#'
        self.xy = [self.x, self.y]
    
    def haut(self):
        self.y -= 1
        self.y_affiché += 1

    def bas(self):
        self.y += 1
        self.y_affiché -= 1

    def gauche(self):
        self.x -= 1
        self.x_affiché -= 1

    def droite(self):
        self.x += 1
        self.x_affiché += 1



class Sortie:
    def __init__(self):
        self.x = randint(0, nb_colonnes - 1)
        self.y = randint(0, nb_lignes - 1)
        self.sprite = f'{Fore.GREEN}O'
        self.xy = [self.x, self.y]

        while self.xy == [nb_colonnes // 2, nb_lignes // 2]:
            self.x = randint(0,nb_colonnes - 1)
            self.y = randint(0,nb_lignes - 1)
            self.xy = [self.x, self.y]



class Mob:
    def __init__(self):
            self.x = randint(0,nb_colonnes - 1)
            self.y = randint(0,nb_lignes - 1)
            self.xy = [self.x, self.y]
            
            while self.xy == [nb_colonnes // 2, nb_lignes // 2]:
                self.x = randint(0,nb_colonnes - 1)
                self.y = randint(0,nb_lignes - 1)
                self.xy = [self.x, self.y]         
   
            self.sprite = f'{Fore.RED}O'

    def mouvement(self):
        direction = randint(1,4)
        if direction == 1:
            self.y -= 1#haut
        elif direction == 2:
            self.x -= 1#gauche
        elif direction == 3:
            self.y += 1#bas
        elif direction == 4:
            self.x += 1#droite
        
        #si on sort de la map:
        if self.x > x:
            self.x = x
        if self.x < 0:
            self.x = 0
        if self.y > y:
            self.y = y
        if self.y < 0:
            self.y = 0
        self.xy = [self.x, self.y]
        #bah on revient sur le coté            



def def_persos():
    global joueur, sortie, mob1, mob2, mob3
    joueur = Joueur()
    sortie = Sortie()
    mob1 = Mob()
    mob2 = Mob()
    mob3 = Mob()



def créer_carte():
    global x,y
    sprite_affiché = f'{Fore.LIGHTBLACK_EX}*'
    for y in range(nb_lignes):
        for x in range(nb_colonnes):
            
            if joueur.x == x and joueur.y == y:#si on est à l'endroit ou '#' est censé apparaitre
                sprite_affiché = joueur.sprite
            if sortie.x == x and sortie.y == y:#la mm avec la sortie
                sprite_affiché = sortie.sprite
            elif mob1.xy == [x, y] or mob2.xy == [x, y] or mob3.xy == [x, y]:
                sprite_affiché = mob1.sprite
            
            print(sprite_affiché,end=' ')
            sprite_affiché = f'{Fore.LIGHTBLACK_EX}*'
        print(' ')    
    """
    print(f'{Fore.YELLOW}X = {joueur.x_affiché}  Y = {joueur.y_affiché}')
    print(f'{mob1.xy}\n{mob2.xy}\n{mob3.xy}')
    print('------------------------------')
    print(f'{[mob1.x, mob1.y]}\n{[mob2.x, mob2.y]}\n{[mob3.x, mob3.y]}')
    """
    insérer_nom_fonction_ici()    



def insérer_nom_fonction_ici():
    global continuer
    continuer = True
    if [joueur.x, joueur.y] == sortie.xy:
        print(f"{Fore.CYAN}>> Bravo c'est gagné !!!")
    elif [joueur.x, joueur.y] == mob1.xy or [joueur.x, joueur.y] == mob2.xy or  [joueur.x, joueur.y] == mob3.xy:
        print(f"{Fore.CYAN}>> Dommage c'est perdu !")
    else:
        question = input(f'{Fore.RED}> ')     
        while question == 'aide':
            print(f'{Fore.MAGENTA}> controles avec zqsd et taper quitter pour quitter ')
            question = input(f'{Fore.RED}> ')     
        if question == 'quitter':
            print(f'{Fore.MAGENTA}>> au revoir')
            sleep(0.5)
            continuer = False
            Fore.RESET
        elif question == 'q':
            joueur.gauche()
        elif question == 's':
            joueur.bas()
        elif question == 'd':
            joueur.droite()
        elif question == 'z':
            joueur.haut()
        else:
            print(F'{Fore.MAGENTA}>> truc saisi non reconnu')
            sleep(0.5)
        system('cls')
        if continuer is True:
            mob1.mouvement()
            mob2.mouvement()
            mob3.mouvement()
            créer_carte()    



print(f'{Fore.MAGENTA}>> PS:ne pas mettre de majuscule dans les input.Pour toute aide,taper aide')
def_taille_map()
while continuer is True:
    question = input(f'{Fore.RED}>> Nouvelle Partie ? ')
    if 'n' in question:
        print(F'{Fore.MAGENTA}>> Au revoir.')
        Fore.RESET
        continuer = False
    else:
        def_taille_map()

