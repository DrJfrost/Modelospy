'''
Created on 18/09/2017

@author: Sebastian
'''
from tkinter import *
from Characters import Character
class Warrior(Character.Character):
    def __init__(self):
        print("hola soy un guerrero")
        self.image = "images_characters\Globin.png"
        
        
    #metodo de prueba
    def hable(self):
        return("yo soy guerrero")
    
    
    
    
    