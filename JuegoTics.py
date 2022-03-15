#BattleShip
#Grupo 18
#Integrantes:
#-Ignacio Court
#-Belen Alamo
#-Fernanda Nicolas

import numpy as np
from random import choice as choice

print("BattleShip")
print("Grupo 18")
print("Integrantes:\n -Ignacio Court\n -Belen Alamo\n -Fernanda Nicolas")

terreno=[[0,0,0],[0,0,0],[0,0,0]]

a=choice([0,1,2])
b=choice([0,1,2])
c=choice([0,1,2])
d=choice([0,1,2])
while a == c and b==d:
    b=choice([0,1,2])
terreno[a][b]=1
terreno[c][d]=1
print(terreno)
jugar=str(input("¿Quieres jugar BattleShip? (responde s si quieres y n si no)\n"))
if jugar == "s":
    print("Exíste un Area maritima en forma de matris de 3x3, en donde se ocultan 2 naves enemigas, intenta destruirlas lanzandoles bombas.\n")
    while np.sum(terreno)>0:
        bomba_fila=int(input("Si las filas van de arriba a abajo y comienzan desde la fila 0 y terminan en la 2. \n ¿En que fila crees que se encuentra alguna de las naves enemigas?\n"))
        bomba_col=int(input("Si las columnas van de izquierda a derecha y comienzan desde la columna 0 y terminan en la 2. \n ¿En que columna crees que se encuentra alguna de las naves enemigas?\n"))
        if terreno[a][b]==terreno[bomba_fila][bomba_col] or terreno[c][d]==terreno[bomba_fila][bomba_col]:
            print("Felicitaciones, has destruido una nave enemiga")
            terreno[bomba_fila][bomba_col]=0
        else:
            print("Lo siento, has errado, intentalo denuevo")
    print("Lo has logrado, has destruido todas las naves enemigas")
elif jugar=="n":
    print("Será para la proxima")
else:
    print("Respuesta no válida")