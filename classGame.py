#!/usr/bin/env python3

class Game:
    
    def __init__(self, unit1, unit2):
        self.unit1 = unit1
        self.unit2 = unit2

    def play(self):
        answer = input('Do you want attack? Answer Y or N:')
        while answer != 'N':
            if answer == 'Y':

                self.unit1.attack(self.unit2) 
                if self.unit2.dead:
                    return

                self.unit2.attack(self.unit1)
                if self.unit1.dead:
                    return

                self.unit1.view()
                self.unit2.view()

            answer = input('Do you want attack again? Answer Y or N:') 