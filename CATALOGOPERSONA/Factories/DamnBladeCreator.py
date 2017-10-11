'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.DamnBlade import DamnBlade
from Factories.WeaponCreator import WeaponCreator
class DamnBladeCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DamnBlade()