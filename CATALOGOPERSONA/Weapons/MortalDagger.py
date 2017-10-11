'''
Created on 18/09/2017

@author: Sebastian
'''
from tkinter import *
from Weapons.Weapon import Weapon
class MortalDagger(Weapon):
    def __init__(self):
        self.nameweapon="Mortal Dagger"
        self.imageweapon="weapons_orc\MortalDagger.png"
    def showWeapon(self):
        pass