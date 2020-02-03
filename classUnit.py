#!/usr/bin/env python3
import random

class Unit:
    _name = 'Hero'
    _hitpoints = 0
    _att = 0
    _defense = 0
    _chance_att = 0
    _chance_save = 0

    def __init__(self, name, hitpoints, att, defense, chance_att, chance_save):
        if type(hitpoints) != int or type(att) != int or type(defense) != int: 
            raise TypeError
        
        self._hitpoints = hitpoints
        self._att = att 
        self._defense = defense
        self._name = name
        self._chance_att = chance_att
        self._chance_save = chance_save
        self.dead = False
            
    def attack(self, other):
    
        if type(self) != type(other): raise TypeError

        if random.randint(0, 100) <= self._chance_att:
            k_att = 2
        else: k_att = 1 

        if random.randint(0, 100) > other._chance_save:     
            other._defense = other._defense - self._att * k_att
            print(f'{self._name} attack power is {self._att*k_att}')
            if other._defense < 0:
                other._hitpoints = other._hitpoints + other._defense
                other._defense = 0
        
            if other._hitpoints <= 0:
                print(f'Game over {other._name} is dead. {self._name} win!') 
                other.dead = True
                return
            else:
                print(f'Hero {other._name} has {other._hitpoints} hitpoints')  
        else:
            print(f'{self._name}\'s attack was rejected. {other._name} rejected the attack')

    def view(self):
        print(f'{self._name} has helth {self._hitpoints}, power attack is {self._att}, {self._chance_att}% double attack, defense {self._defense}, {self._chance_save}% reject attack.')        
