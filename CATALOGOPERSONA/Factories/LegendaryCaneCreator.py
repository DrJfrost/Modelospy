'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.LegendaryCane import LegendaryCane
from Factories.WeaponCreator import WeaponCreator
class LegendaryCaneCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return LegendaryCane()
