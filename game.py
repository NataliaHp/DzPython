#!/usr/bin/env python3

from classUnit import Unit 
from classGame import Game 

try:
    
    unit1 = Unit('Artur', 100, 10, 50, 45, 28)
    unit1.view()
    unit2 = Unit('Lancelot', 100, 10, 50, 25, 37)
    unit2.view()
    
    game1 = Game(unit1, unit2)
    game1.play()

except TypeError:
    print('Wrong type')
