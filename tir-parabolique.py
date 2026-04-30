import math
import matplotlib.pyplot as plt # type: ignore

g = 9.81 # Accélération gravitationnelle

def verification(test, donnee=None, h=None):
    try :
        value = float(test)
    except ValueError :
        return None

    if donnee == "v" or donnee == "h" :
            if value >= 0 :
                return value
            else : 
                return None

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

def demander_valeur(val_init, h = None):
    val = None
    while val is None :
        inp = input(msg[val_init]['msg_inp'])
        val = verification(inp, msg[val_init]['type'], h)
        if val is None :
            print(msg[val_init]['msg_err'])
    return val

# Définition des messages d'input, des messages d'erreurs et types associés aux valeur initiales
msg = {
    "v0" : {'msg_inp' : "Vitesse initiale (en m/s, obligatoirement positive) : ", 'msg_err' : "Entrez une vitesse valide.", 'type' : 'v'},
    "h0" : {'msg_inp' : "Hauteur initiale (en m, obligatoirement positive) : ", 'msg_err' : "Entrez une hauteur valide.", 'type' : 'h'},
    "ang" : {'msg_inp' : "Angle du tir (en degrés, 0 < angle < 90 si h==0, -90 < angle < 90 si h > 0) : ", 'msg_err' : "Entrez un angle valide.", 'type' : 'ang'}
}

# Récupération des conditions initiales
v0 = demander_valeur("v0")
h0 = demander_valeur("h0")
ang = demander_valeur("ang", h0)


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
plt.xlim(-2, portee + 2) # Réglage du cadrage xmin et xmax
plt.ylim(-2, hauteur_max*1.3) # Réglage du cadrage ymin et ymax
plt.show() # Affichage de la courbe