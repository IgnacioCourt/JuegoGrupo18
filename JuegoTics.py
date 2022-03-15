print("BattleShip")
import numpy as np
from random import choice as choice

terreno=[[0,0,0],[0,0,0],[0,0,0]]

a=choice([0,1,2])
b=choice([0,1,2])
c=choice([0,1,2])
d=choice([0,1,2])
while a == c and b==d:
    b=choice([0,1,2])
terreno[a,b]=1
terreno[c,d]=1
print(terreno)