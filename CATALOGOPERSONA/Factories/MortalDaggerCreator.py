'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.MortalDagger import MortalDagger
from Factories.WeaponCreator import WeaponCreator
class MortalDaggerCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return MortalDagger()