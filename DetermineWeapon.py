'''
Created on 18/09/2017

@author: Sebastian
'''
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
class DetermineWeapon():
    def __init__(self):
        pass
    createweapon=None
    weapon=None
    def createWeapon(self, number):
        self.createweapon={1: EpicScepterCreator(), 2: HeavenlyScepterCreator(), 3: LegendaryCaneCreator(), 4: HadesSwordCreator(),
                   5: DamnBladeCreator(), 6: DemonSwordCreator(), 7: ExcaliburSwordCreator(), 8: DragonSwordCreator(),
                   9: OdinSpearCreator(), 10: DragonTailCreator(), 11: MortalDaggerCreator(), 12: VampireSpearCreator() }
        self.weapon = self.createweapon[number].CreateWeapon()
        print(str(self.weapon))
    def getWeapon(self):
        return self.weapon
    
    
    
    