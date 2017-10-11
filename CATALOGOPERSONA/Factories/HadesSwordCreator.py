'''
Created on 18/09/2017

@author: Sebastian
'''
from Weapons.HadesSword import HadesSword
from Factories.WeaponCreator import WeaponCreator
class HadesSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return HadesSword()