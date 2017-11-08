'''
Created on 18/09/2017

@author: Sebastian
'''

class Weapon():
    nameweapon=None
    imageweapon=None
    def getNameWeapon(self):
        return self.nameweapon
    
    def __init__(self):
        pass
    def showWeapon(self):
        pass
    def getImageWeapon(self):
        return self.imageweapon
    

class VampireSpear(Weapon):
    def __init__(self):
        self.nameweapon="Vampire Spear"
        self.imageweapon="weapons_orc\VampireSpear.png"
    def showWeapon(self):
        pass
    
    
class OdinSpear(Weapon):
    def __init__(self):
        self.nameweapon="Odin Spear"
        self.imageweapon="weapons_goblin\OdinSpear.png"
    def showWeapon(self):
        pass
    
    
class MortalDagger(Weapon):
    def __init__(self):
        self.nameweapon="Mortal Dagger"
        self.imageweapon="weapons_orc\MortalDagger.png"
    def showWeapon(self):
        pass
    
class LegendaryCane(Weapon):
    def __init__(self):
        self.nameweapon="Legendary Cane"
        self.imageweapon="weapons_witch\Scepter.png"
    def showWeapon(self):
        pass
    
class HeavenlyScepter(Weapon):
    def __init__(self):
        self.nameweapon="Heavenly Scepter"
        self.imageweapon="weapons_witch\HeavenlyScepter.png"
    def showWeapon(self):
        pass
    
class HadesSword(Weapon):
    def __init__(self):
        self.nameweapon="Hades Sword"
        self.imageweapon="weapons_demon\HadesSword.png"
    def showWeapon(self):
        pass

class ExcaliburSword(Weapon):
    def __init__(self):
        self.nameweapon="Excalibur Sword"
        self.imageweapon="weapons_goblin\ExcaliburSword.png"
    def showWeapon(self):
        pass
    
class EpicScepter(Weapon):
    def __init__(self):
        self.nameweapon = "Epic Scepter"
        self.imageweapon = "weapons_witch\EpicScepter.png"
    def showWeapon(self):
        pass
    
class DragonTail(Weapon):
    def __init__(self):
        self.nameweapon="Dragon Tail"
        self.imageweapon="weapons_orc\DragonTail.png"
    def showWeapon(self):
        pass
    
class DragonSword(Weapon):
    def __init__(self):
        self.nameweapon="Dragon Sword"
        self.imageweapon="weapons_goblin\Hammer.png"
        
    def showWeapon(self):
        pass
    
class DemonSword(Weapon):
    def __init__(self):
        self.nameweapon="Demon Sword"
        self.imageweapon="weapons_demon\DragonHammer.png"
        
    def showWeapon(self):
        pass
    
class DamnBlade(Weapon):
    def __init__(self):
        self.nameweapon="Damn Blade"
        self.imageweapon="weapons_demon\DamnBlade.png"
        
    def showWeapon(self):
        pass