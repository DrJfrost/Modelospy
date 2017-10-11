'''
Created on 18/09/2017

@author: Sebastian
'''
from Characters.Orc import Orc
from Factories import CharacterCreator
class OrcCreator(CharacterCreator.CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Orc()