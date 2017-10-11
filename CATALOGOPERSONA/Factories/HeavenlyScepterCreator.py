'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.HeavenlyScepter import HeavenlyScepter
from Factories.WeaponCreator import WeaponCreator
class HeavenlyScepterCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return HeavenlyScepter()