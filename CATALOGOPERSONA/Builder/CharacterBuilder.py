'''
Created on 18/09/2017

@author: Sebastian
'''
from Characters import Character
from Builder.Builder import Builder
from Factories.EpicScepterCreator import EpicScepterCreator
from Factories.LegendaryCaneCreator import LegendaryCaneCreator
from Factories.HeavenlyScepterCreator import HeavenlyScepterCreator
from Factories.DamnBladeCreator import DamnBladeCreator
from Factories.HadesSwordCreator import HadesSwordCreator
from Factories.DemonSwordCreator import DemonSwordCreator
from Factories.DragonSwordCreator import DragonSwordCreator
from Factories.OdinSpearCreator import OdinSpearCreator
from Factories.ExcaliburSwordCreator import ExcaliburSwordCreator
from Factories.MortalDaggerCreator import MortalDaggerCreator
from Factories.VampireSpearCreator import VampireSpearCreator
from Factories.DragonTailCreator import DragonTailCreator

class CharacterBuilder(Builder):
    def __init__(self):
        pass
    def buildCharacter(self, character):
        self.character = character
        
    def buildWeapon(self, weapon):
        #self.weapon = weapon
        self.character.setWeapon(weapon)
        
        
        
    