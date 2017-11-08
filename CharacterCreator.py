'''
Created on 18/09/2017

@author: Sebastian
'''
from Character import Conjurer
from Character import Devil
from Character import Orc
from Character import Warrior
from Character import Adapter

class CharacterCreator():
    def __init__(self):
        pass
    def factorymethod(self):
        pass
    def CreateCharacter(self):
        return self.factorymethod()
    
class ConjurerCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        x = Conjurer()
        evilConjurer=Adapter(x)
        return evilConjurer
    
class DevilCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Devil()
    
class OrcCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Orc()
    
class WarriorCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Warrior()