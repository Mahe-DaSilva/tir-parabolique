import math
import matplotlib.pyplot as plt # type: ignore

g = 9.81 # Accélération gravitationnelle

def verification(test, donnee=None, h=None):
    try :
        value = float(test)
    except ValueError :
        return None

    if donnee == "v" or donnee == "h" :
            if value > 0 :
                return value
            else : return None

    if donnee == "ang" :
        if h == 0 :
            if value > 0 and value <= 90 :
                return value
            else :
                return None
        elif h > 0 :
            if value >= -90 and value <= 90 :
                return value
            else :
                return None

print()

# Intialisation des valeurs initiales à -1 et 100 pour éviter plus tard les valeurs invalides
v0 = None
h0 = None
ang = None

test_v0 = False
test_h0 = False
test_ang = False

# Récupération des conditions initiales
while test_v0 != True :
    v0_input = input("Vitesse initiale (en m/s, obligatoirement positive) : ")
    v0 = verification(v0_input, "v")
    if v0 == None :
        print("Entrez une vitesse valide.")
    else :
        test_v0 = True

while test_h0 != True :
    h0_input = input("Hauteur initiale (en m, obligatoirement positive) : ")
    h0 = verification(h0_input, "h")
    if h0 == None :
        print("Entrez une hauteur valide.")
    else :
        test_h0 = True

while test_ang != True :
    ang_input = input("Angle du tir (en degrés, 0 < angle < 90 si h==0, -90 < angle < 90 si h > 0) : ")
    ang = verification(ang_input, "ang", h0)
    if ang == None :
        print("Entrez un angle valide.")
    else :
        test_ang = True


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
plt.plot(x,y) # Création des axes
plt.xlabel("portée") # Nom de l'axe des abscisses x
plt.ylabel("hauteur") # Nom de l'axe des ordonnées
plt.title("Trajectoire du tir") # Titre du schéma
plt.grid(True) # Affichage de la grille
plt.gca().set_aspect('equal') # Échelle orthonormée des axes
plt.xlim(-1, portee + 1) # Réglage du cadrage xmin et xmax
plt.ylim(-1, hauteur_max + 1) # Réglage du cadrage ymin et ymax
plt.show() # Affichage de la courbe