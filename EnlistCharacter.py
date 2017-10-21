'''
Created on 18/09/2017

@author: Sebastian
'''

from DetermineCharacter import DetermineCharacter
from DetermineWeapon import DetermineWeapon
from Director import Director
from Builder import CharacterBuilder
import Character
import Weapon


class EnlistCharacter():
    personajesclonados=None
    
    determinarpersonaje=None
    determinararma=None
    constructorpersonaje=None
    armarpersonaje=None
    def __init__(self):
        self.determinarpersonaje=DetermineCharacter()
        self.determinararma=DetermineWeapon()
        self.constructorpersonaje=CharacterBuilder()
        self.armarpersonaje=Director()
    def createWeapon(self,number2):
        self.determinararma.createWeapon(number2)
    def createCharacter(self,number): 
        self.determinarpersonaje.createCharacter(number)  
    def BuildCharacter(self):
        self.armarpersonaje.setBuilder(self.constructorpersonaje)
        self.armarpersonaje.BuildCharacter(self.determinarpersonaje.getCharacter(),self.determinararma.getWeapon())
    def cloneCharacter(self):
        self.personajesclonados=self.armarpersonaje.getCharacter()
        return self.personajesclonados.clone()
    
    











