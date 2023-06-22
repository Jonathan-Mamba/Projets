#coding utf-8

"""

"""

from colorama import Fore
from random import randint
from os import system
from time import sleep
from keyboard import is_pressed,press,release

temporaire = lambda:print(f"{Fore.LIGHTYELLOW_EX}> Placeholder pcq j'ai trop la flemme là.")

def def_taille_map():
    global nb_colonnes,nb_lignes,nombre_vies
    nb_lignes = int(input(f'{Fore.RED}> nb de lignes : ')) 
    nb_colonnes = int(input('> nb de colonnes : '))
    nombre_vies = 3

    if nb_colonnes * nb_lignes < 25:
        print(f"{Fore.MAGENTA}>> L'aire minimale de la carte est de 25.Dans ce cas, l'aire est de {nb_lignes * nb_colonnes}")
        def_taille_map()
    
    def_persos()
    créer_carte()



class Joueur:
    sprite = f'{Fore.BLUE}#'
    def __init__(self):
        self.x = nb_colonnes // 2
        self.y = nb_lignes // 2
        self.x_affiché = 0
        self.y_affiché = 0
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
    sprite = f'{Fore.GREEN}O'
    def __init__(self):
        self.x = randint(0, nb_colonnes - 1)
        self.y = randint(0, nb_lignes - 1)
        self.xy = [self.x, self.y]

        while self.xy == [nb_colonnes // 2, nb_lignes // 2]:
            self.x = randint(0,nb_colonnes - 1)
            self.y = randint(0,nb_lignes - 1)
            self.xy = [self.x, self.y]



class Mob:
    sprite = f'{Fore.RED}O'
    def __init__(self):
            self.x = randint(0,nb_colonnes - 1)
            self.y = randint(0,nb_lignes - 1)
            self.xy = [self.x, self.y]
            
            while self.xy == [nb_colonnes // 2, nb_lignes // 2]:
                self.x = randint(0,nb_colonnes - 1)
                self.y = randint(0,nb_lignes - 1)
                self.xy = [self.x, self.y]         
   
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
        if self.x > x:#si on est a droite
            self.x = x
        if self.x < 0:#si on est à gauche
            self.x = 0
        if self.y > y:#si on est en bas
            self.y = y
        if self.y < 0:#si on est en haut
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
                sprite_affiché = Joueur.sprite
            if sortie.x == x and sortie.y == y:#la mm avec la sortie
                sprite_affiché = Sortie.sprite
            elif mob1.xy == [x, y] or mob2.xy == [x, y] or mob3.xy == [x, y]:#si j'ai mis un elif ici c'est pour éviter qu'il affiche le mob au lieu de la sortie
                sprite_affiché = Mob.sprite
            
            print(sprite_affiché,end=' ')
            sprite_affiché = f'{Fore.LIGHTBLACK_EX}*'
        print(' ')    
    
    """
    print(f'{mob1.xy}\n{mob2.xy}\n{mob3.xy}')
    print('------------------------------')
    print(f'{[mob1.x, mob1.y]}\n{[mob2.x, mob2.y]}\n{[mob3.x, mob3.y]}')
    """
    insérer_nom_fonction_ici()    



def insérer_nom_fonction_ici():
    global continuer
    continuer = True
    if [joueur.x, joueur.y] == sortie.xy:#si le joueur a gagné:
        print(f"{Fore.CYAN}>> Bravo c'est gagné !!!")
    
    elif [joueur.x, joueur.y] == mob1.xy or [joueur.x, joueur.y] == mob2.xy or [joueur.x, joueur.y] == mob3.xy:#sinon,si il a perdu:
        print(f"{Fore.CYAN}>> Dommage c'est perdu !")
    else:#si il a ni gagné ni perdu  
        while True:
            if is_pressed('space'):
                print(f'{Fore.MAGENTA}> controles avec zqsd et taper la touche "retour/backspace" pour quitter ')   
                sleep(0.5)

            elif is_pressed('backspace'):
                print(f'{Fore.MAGENTA}>> au revoir')
                sleep(0.5)
                continuer = False
                Fore.RESET
                break
            
            elif is_pressed('q'):
                joueur.gauche()
                sleep(0.5)
                break
            
            elif is_pressed('s'):
                joueur.bas()
                sleep(0.5)
                break
            
            elif is_pressed('d'):
                joueur.droite()
                sleep(0.5)
                break
            
            elif is_pressed('z'):
                joueur.haut()
                sleep(0.5)
                break
            
        if continuer is True:
            system('cls')   
            mob1.mouvement()
            mob2.mouvement()
            mob3.mouvement()
            créer_carte()    



def effacer_touches():#enft quand on finit il prend toutes les touches préssées et les met dans les input.Donc j'ai fait ca pour tout vider 
    press('enter')
    input(f'{Fore.BLACK} ')
    release('enter')
    system('cls')
    créer_carte()



def début_combat():#PAS ENCORE FINI
    global nombre_vies
    temporaire()
    nombre_vies -= 1


print(f"{Fore.MAGENTA}>> PS:ne pas mettre de majuscule dans les input.Pour toute aide,taper sur la touche Espace(n'appuie pas sur Entrée aussi).")
def_taille_map()
while continuer is True:
    effacer_touches()
    
    question = input(f'{Fore.RED}>> Nouvelle Partie ? ')
    if 'n' in question:
        print(F'{Fore.MAGENTA}>> Au revoir.')
        Fore.RESET
        continuer = False
    else:
        def_taille_map()

