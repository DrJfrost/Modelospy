'''
Created on 18/09/2017

@author: Sebastian
'''
class Director():
    constructor=None
    def __init__(self):
        pass
    def setBuilder(self, constructor):
        self.constructor=constructor
    def getCharacter(self):
        return self.constructor.getCharacter()
    def BuildCharacter(self, character, weapon):
        self.constructor.buildCharacter(character)
        self.constructor.buildWeapon(weapon)