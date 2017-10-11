'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.DemonSword import DemonSword
from Factories.WeaponCreator import WeaponCreator
class DemonSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DemonSword()