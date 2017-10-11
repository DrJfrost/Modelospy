'''
Created on 18/09/2017

@author: Sebastian
'''
from Characters.Conjurer import Conjurer
from Factories.CharacterCreator import CharacterCreator
class ConjurerCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Conjurer()
