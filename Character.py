'''
Created on 18/09/2017

@author: Sebastian
'''
from copy import deepcopy

class Character():
    weapon=None
    objclone=None
    
    image=None
    aurora= None
    auroraNum=None

    
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
    def setAurora(self, aurora):
        self.auroraNum=aurora
        if (aurora==0):
            self.aurora="aurora/Aurora.png"

        if (aurora==1):
            self.aurora="aurora/Aurora1.png"

        if (aurora==2):
            self.aurora="aurora/Aurora2.png"

        if (aurora==3):
            self.aurora="aurora/Aurora3.png"

    def getAurora(self):
        return self.aurora
    def getAuroraNum(self):
        return self.auroraNum

   

    #metodo de prueba
    def hable(self):
        pass
    
    
class Conjurer(Character):
    def __init__(self):
        print("hola soy un mago")
        self.image = "images_characters/Witch.png"
    
    
    #metodo de prueba
    def hable(self):
        return("yo soy mago")
    
    
class Devil(Character):
    
    def __init__(self):
        print("hola soy un demonio")
        self.image = "images_characters\Demon.png"
        

    #metodo de prueba
    def hable(self):
        return("yo soy demonio")
    
    
class Orc(Character):
    def __init__(self):
        print("hola soy un orco")
        self.image = "images_characters\orc.png"
       
        
    #metodo de prueba
    def hable(self):
        return("yo soy orco")
    
    
class Warrior(Character):
    def __init__(self):
        print("hola soy un guerrero")
        self.image = "images_characters\Globin.png"
        
        
    #metodo de prueba
    def hable(self):
        return("yo soy guerrero")
    
    
    
