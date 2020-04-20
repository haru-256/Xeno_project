import numpy as np
import random
import usecases.draw as dw

def start():
    all_cards = np.array([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10])
    #シャッフル
    random.shuffle(all_cards)
    #山札と転生札の生成
    reincarnation,deck = dw.drawing(all_cards)
    p1_1,deck = dw.drawing(deck)
    p2_1,deck = dw.drawing(deck)
    return reincarnation,p1_1,p2_1,deck
