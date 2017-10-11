'''
Created on 18/09/2017

@author: Sebastian
'''
from tkinter import *
from Characters import Character
class Orc(Character.Character):
    def __init__(self):
        print("hola soy un orco")
        self.image = "images_characters\orc.png"
       
        
    #metodo de prueba
    def hable(self):
        return("yo soy orco")
    
    
    
    