import numpy as np
import random

def drawing(deck):
    onecard = deck[0]
    deck = np.delete(deck,0)
    return onecard,deck
