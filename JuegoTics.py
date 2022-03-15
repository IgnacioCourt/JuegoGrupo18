print("BattleShip")
import numpy as np
from random import choice

terreno=np.array(3,3,0)

a=choice([1,2,3])
b=choice([1,2,3])
c=choice([1,2,3])
d=choice([1,2,3])
while a == c and b==d:
    b=choice([1,2,3])
terreno[a,b]=1
terreno[c,d]=1
print(terreno)