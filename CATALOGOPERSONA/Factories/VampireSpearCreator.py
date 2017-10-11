'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.VampireSpear import VampireSpear
from Factories.WeaponCreator import WeaponCreator
class VampireSpearCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return VampireSpear()