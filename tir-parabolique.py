import math
import matplotlib.pyplot as plt # type: ignore

g = 9.81 # Accélération gravitationnelle

def verification(test, donnee=None):
    try :
        value = float(test)
        return value
    except ValueError :
        if donnee == "v" :
            print("Entrez une vitesse valide.")
        elif donnee == "h" :
            print("Entrez une hauteur valide.")
        elif donnee == "ang" :
            print("Entrez un angle valide.")
        else :
            print("Entrez un nombre valide.")
        print()
        return None

print()

# Intialisation des valeurs initiales à -1 et 100 pour éviter plus tard les valeurs invalides
v0 = -1
h0 = -1
ang = 100

# Récupération des conditions initiales
while v0 is None or v0 < 0 :
    v0_input = input("Vitesse initiale (en m/s, obligatoirement positive) : ")
    print()
    v0 = verification(v0_input, "v")

while h0 is None or h0 < 0 :
    h0_input = input("Hauteur initiale (en m, obligatoirement positive) : ")
    print()
    h0 = verification(h0_input, "h")

if h0 == 0 :
    while ang is None or ang > 90 or ang < 0 :
        ang_input = input("Angle du tir (en degrés compris entre 0 et 90 si h==0, peut être négatif si h>0) : ")
        print()
        ang = verification(ang_input, "ang")

else :
    while ang is None or ang > 90 :
        ang_input = input("Angle du tir (en degrés compris entre 0 et 90 si h==0, peut être négatif si h>0) : ")
        print()
        ang = verification(ang_input, "ang")


ang_rad = math.radians(ang) # Convertion de l'angle de degrés à radians

# Valeurs initiales de x et y (coordonnées de départ)
x = [0]
y = [h0] # Hauteur initiale

t = 0.01 # On initialise t=0.01 car la position à t=0 est déjà enregistrée dans les conditions initiales
while y[-1] >= 0 :
    xt = v0 * math.cos(ang_rad) * t
    yt = v0 * math.sin(ang_rad) * t - 1/2*g*t**2 + h0
    x.append(xt)
    y.append(yt)
    t += 0.01

# Résultats
portee = x[-1] # Dernière valeur de x (abscisse finale)
hauteur_max = max(y) # Plus grande valeur de y (ordonnée maximale au sommet de la parabole)

print()
print(f"Portée : {portee:.2f}m, hauteur maximale : {hauteur_max:.2f}m")

# Traçage de la courbe
plt.plot(x,y) # Création desa axes
plt.xlabel("portée") # Nom de l'axe des abscisses x
plt.ylabel("hauteur") # Nom de l'axe des ordonnées
plt.title("Trajectoire du tir") # Titre du schéma
plt.grid(True) # Affichage de la grille
plt.gca().set_aspect('equal') # Échelle orthonormée des axes
plt.xlim(-1, portee + 1) # Réglage du cadrage xmin et xmax
plt.ylim(-1, hauteur_max + 1) # Réglage du cadrage ymin et ymax
plt.show() # Affichage de la courbe