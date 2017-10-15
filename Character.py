'''
Created on 18/09/2017

@author: Sebastian
'''
from copy import deepcopy

class Character():
    weapon=None
    objclone=None
    
    image=None

    
    def clone(self):
        return deepcopy(self)
    
    def __init__(self):
        pass
    def setWeapon(self, weapon):
        self.weapon=weapon
    def getWeapon(self):
        return self.weapon
    
    def getImage(self):
        return self.image
   

    #metodo de prueba
    def hable(self):
        pass
    
    
    
    
