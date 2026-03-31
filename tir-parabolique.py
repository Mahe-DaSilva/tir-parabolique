import math
import matplotlib.pyplot as plt # type: ignore

g = 9.81

v0 = float(input("Vitesse initiale (en m/s) : "))
ang = float(input("Angle du tir (en degrés) : "))

ang_rad = math.radians(ang)

x = [0]
y = [0]

t = 0.01
while y[-1] >= 0 :
    xt = v0 * math.cos(ang_rad) * t
    yt = v0 * math.sin(ang_rad) * t - 1/2*g*t**2
    x.append(xt)
    y.append(yt)
    t += 0.01

portee = x[-1]
hauteur_max = max(y)

print(f"Portée : {portee:.2f}m, hauteur maximale : {hauteur_max:.2f}m")

plt.plot(x,y)
plt.xlabel("portée")
plt.ylabel("hauteur")
plt.title("Trajectoire du tir")
plt.grid(True)
plt.gca().set_aspect('equal')
plt.xlim(-1, 50)
plt.ylim(-1, 50)
plt.show()