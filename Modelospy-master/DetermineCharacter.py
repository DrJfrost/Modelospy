'''
Created on 18/09/2017

@author: Sebastian
'''
from CharacterCreator import OrcCreator
from CharacterCreator import ConjurerCreator
from CharacterCreator import DevilCreator
from CharacterCreator import WarriorCreator
class DetermineCharacter():
    def __init__(self):
        pass
    createcharacter=None
    character=None
    def createCharacter(self,number):
        self.createcharacter={1: ConjurerCreator(), 2: DevilCreator(), 3: WarriorCreator(), 4: OrcCreator() }
        self.character=self.createcharacter[number].CreateCharacter()
    def getCharacter(self):
        return self.character
    