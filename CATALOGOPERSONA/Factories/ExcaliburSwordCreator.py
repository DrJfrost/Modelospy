'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.ExcaliburSword import ExcaliburSword
from Factories.WeaponCreator import WeaponCreator
class ExcaliburSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return ExcaliburSword()