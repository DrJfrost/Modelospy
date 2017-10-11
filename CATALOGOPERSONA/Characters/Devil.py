'''
Created on 18/09/2017

@author: Sebastian
'''
from tkinter import *
from Characters import Character
class Devil(Character.Character):
    
    def __init__(self):
        print("hola soy un demonio")
        self.image = "images_characters\Demon.png"
        

    #metodo de prueba
    def hable(self):
        return("yo soy demonio")
    
    

    