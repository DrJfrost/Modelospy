'''
Created on 18/09/2017

@author: Sebastian
'''
from Characters.Devil import Devil
from Factories.CharacterCreator import CharacterCreator
class DevilCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Devil()