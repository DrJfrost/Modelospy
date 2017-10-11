'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.DragonTail import DragonTail
from Factories.WeaponCreator import WeaponCreator
class DragonTailCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DragonTail()