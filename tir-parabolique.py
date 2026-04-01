import math
import matplotlib.pyplot as plt # type: ignore

g = 9.81 # Accélération gravitationnelle

print()

# Récupération des conditions initiales
v0 = float(input("Vitesse initiale (en m/s) : "))
h0 = float(input("Hauteur initiale (en m) : "))
ang = float(input("Angle du tir (en degrés) : "))

ang_rad = math.radians(ang) # Convertion de l'angle de degrés à radians

# Valeurs initiales de x et y (coordonnées de départ)
x = [0]
y = [h0] # Hauteur initiale

t = 0.01
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