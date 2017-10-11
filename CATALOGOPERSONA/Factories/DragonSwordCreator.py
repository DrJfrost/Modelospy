'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.DragonSword import DragonSword
from Factories.WeaponCreator import WeaponCreator
class DragonSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DragonSword()