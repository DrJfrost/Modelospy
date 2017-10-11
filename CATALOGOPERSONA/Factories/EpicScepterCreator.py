'''
Created on 18/09/2017

@author: Sebastian
'''
from Factories.WeaponCreator import WeaponCreator
from Weapons.EpicScepter import EpicScepter

class EpicScepterCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return EpicScepter()
