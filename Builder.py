'''
Created on 18/09/2017

@author: Sebastian
'''
class Builder():
    character=None
    weapon=None
    def __init__(self):
        pass
    def buildCharacter(self):
        pass
    def buildWeapon(self):
        pass
    def getCharacter(self):
        return self.character
    
    
class CharacterBuilder(Builder):
    def __init__(self):
        pass
    def buildCharacter(self, character):
        self.character = character
        
    def buildWeapon(self, weapon):
        #self.weapon = weapon
        self.character.setWeapon(weapon)