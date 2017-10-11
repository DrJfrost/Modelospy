'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.OdinSpear import OdinSpear
from Factories.WeaponCreator import WeaponCreator
class OdinSpearCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return OdinSpear()