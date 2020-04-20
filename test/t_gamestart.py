import sys
import numpy as np
sys.path.append('../usecases')
import gamestart as gs
#from ..usecases.gamestart import *

reincarnation,p1,p2,deck = gs.start()

print(reincarnation)
print(p1,p2)
print(deck,len(deck))
