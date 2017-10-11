'''
Created on 18/09/2017

@author: Sebastian
'''
from Characters.Warrior import Warrior
from Factories.CharacterCreator import CharacterCreator

class WarriorCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Warrior()