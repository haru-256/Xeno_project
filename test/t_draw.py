import sys
sys.path.append('../usecases')
import draw as dw
#from ..usecases.draw import *
import numpy as np

rand = np.random.randint(0,10,10)
drawed, rand_after = dw.drawing(rand)

print(rand,len(rand))
print(drawed)
print(rand_after,len(rand_after))
