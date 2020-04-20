#import entities.defcard as dcard
from entities.defcard import Card
from entities.defjobs import Teller
#import entities.defjobs as djobs
import usecases.gamestart as gs
#import . as
#from usecases.gamestart import start
reincarnation, p1, p2, deck = gs.start()

print(reincarnation)
print(deck)
print(p1,p2)

card = Card().set_job(3)
print(card.role)
print(card.power)

job = Teller.telling(Card().set_job(2))
