from tkinter import *
from EnlistCharacter import EnlistCharacter
import pygame, sys
from pygame.locals import *
from random import randint


class charChooserGUI:
    imageweapon = None
    pygame.mixer.init()
    pygame.mixer.music.load('Musica\musica.mp3')
    pygame.mixer.music.play(-1)

    def __init__(self, master):

        # ***** Parent Window Size ****
        master.minsize(width=1000, height=500)
        master.maxsize(width=1000, height=500)

        label = Label(bg="#3a3a3a")

        # **** Title ****

        title = Label(text="Choose your character", font="times 24 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Images ****

        img1 = PhotoImage(file="images_characters/1.png")
        img2 = PhotoImage(file="images_characters/2.png")
        img3 = PhotoImage(file="images_characters/3.png")
        img4 = PhotoImage(file="images_characters/4.png")

        char1 = Button(label, image=img1, command=lambda: self.chooseWeapon(1), bg="black")
        char1.image = img1
        char1.grid(row=0, padx=10, pady=5)
        char2 = Button(label, image=img2, command=lambda: self.chooseWeapon(2), bg="black")
        char2.image = img2
        char2.grid(row=0, column=1, padx=10, pady=5)
        char3 = Button(label, image=img3, command=lambda: self.chooseWeapon(3), bg="black")
        char3.image = img3
        char3.grid(row=0, column=2, padx=10, pady=5)
        char4 = Button(label, image=img4, command=lambda: self.chooseWeapon(4), bg="black")
        char4.image = img4
        char4.grid(row=0, column=3, padx=10, pady=5)

        # ****** Names *****

        name1 = Label(label, text="Witch", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Demon", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text="Goblin", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name3.grid(row=1, column=2)
        name4 = Label(label, text="Orc", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name4.grid(row=1, column=3)

        # *** Adds the whole content that's on the label ***
        label.pack()

    def chooseWeapon(self, raze):

        root.destroy()
        root2 = Tk()
        root2.title("Weapon Chooser")
        root2.configure(bg="#191919")
        root2.minsize(width=1000, height=600)

        # **** Content ***

        label = Label(bg="#3a3a3a")
        # **** Title ****

        title = Label(text="Choose your weapon", font="times 24 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Images ****
        raze1 = raze

        if raze1 == 1:
            image1 = PhotoImage(file="weapons_witch\EpicScepter.png")
            image2 = PhotoImage(file="weapons_witch\HeavenlyScepter.png")
            image3 = PhotoImage(file="weapons_witch\Scepter.png")
            nameweapon = {1: "Epic Scepter", 2: "Heavenly Scepter", 3: "Scepter"}
            numweapon = {1: 1, 2: 2, 3: 3}
        if raze1 == 2:
            image1 = PhotoImage(file="weapons_demon\HadesSword.png")
            image2 = PhotoImage(file="weapons_demon\DamnBlade.png")
            image3 = PhotoImage(file="weapons_demon\DragonHammer.png")
            nameweapon = {1: "Hades Sword", 2: "Damn Blade", 3: "Dragon Hammer"}
            numweapon = {1: 4, 2: 5, 3: 6}
        if raze1 == 3:
            image1 = PhotoImage(file="weapons_goblin\ExcaliburSword.png")
            image2 = PhotoImage(file="weapons_goblin\Hammer.png")
            image3 = PhotoImage(file="weapons_goblin\OdinSpear.png")
            nameweapon = {1: "Excalibur Sword", 2: "Hammer", 3: "Odin Spear"}
            numweapon = {1: 7, 2: 8, 3: 9}
        if raze1 == 4:
            image1 = PhotoImage(file="weapons_orc\DragonTail.png")
            image2 = PhotoImage(file="weapons_orc\MortalDagger.png")
            image3 = PhotoImage(file="weapons_orc\VampireSpear.png")
            nameweapon = {1: "Dragon Tail", 2: "Mortal Dagger", 3: "Vampire Spear"}
            numweapon = {1: 10, 2: 11, 3: 12}

        char1 = Button(label, image=image1, command=lambda: self.createChar(raze, numweapon[1], nCharVar.get(), root2),
                       bg="black", activebackground="#222222")
        char1.image = image1
        char1.grid(row=0, padx=10, pady=5)
        char2 = Button(label, image=image2, command=lambda: self.createChar(raze, numweapon[2], nCharVar.get(), root2),
                       bg="black", activebackground="#222222")
        char2.image = image2
        char2.grid(row=0, column=1, padx=10, pady=5)
        char3 = Button(label, image=image3, command=lambda: self.createChar(raze, numweapon[3], nCharVar.get(), root2),
                       bg="black", activebackground="#222222")
        char3.image = image3
        char3.grid(row=0, column=2, padx=10, pady=5)

        # ****** Names *****

        name1 = Label(label, text=nameweapon[1], font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text=nameweapon[2], font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text=nameweapon[3], font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name3.grid(row=1, column=2)

        # *** Adds the whole content that's on the label ***
        nCharMsj = Label(label, text="Choose how many characters you want :)", font="times 15 bold italic",
                         fg="#ffca1e", bg="#222222")
        nCharMsj.grid(row=2, column=0, columnspan=2, sticky=E)

        nCharVar = StringVar(label)
        nCharVar.set("1")
        nChar = ["1", "2", "3"]

        nCharMenu = OptionMenu(label, nCharVar, *nChar)
        nCharMenu.config(width=5, font="times 15 bold italic", fg="#ffca1e", bg="#2d2d2d",
                         highlightbackground="#000000", activebackground="#222222")
        nCharMenu.grid(row=2, column=2, pady=30)

        label.pack()

    def createChar(self, raze, weapon, nchar, root2):
        root2.destroy()

        creacion = EnlistCharacter()
        creacion.createWeapon(weapon)
        creacion.createAurora()
        creacion.createCharacter(raze)

        creacion.BuildCharacter()

        personaje1 = None
        personaje12 = None
        personaje13 = None

        if nchar == "1":
            personaje1 = creacion.cloneCharacter()

        if nchar == "2":
            personaje1 = creacion.cloneCharacter()
            personaje12 = creacion.cloneCharacter()
        if nchar == "3":
            personaje1 = creacion.cloneCharacter()
            personaje12 = creacion.cloneCharacter()
            personaje13 = creacion.cloneCharacter()
        imweapon = personaje1.getWeapon().getImageWeapon()
        print(imweapon)
        imchar = personaje1.getImage()
        print(imchar)
        imAurora = personaje1.getAurora()
        print(imAurora)

        class Animation():

            pygame.init()
            ventana = pygame.display.set_mode((1024, 683))
            pygame.display.set_caption("personajes")

            imagen_arma = pygame.image.load(imweapon)

            imagen_personaje = pygame.image.load(imchar)
            imagen_aurora = pygame.image.load(imAurora)

            if raze == 1:
                X = 90
                Y = 310
                posX = 100
                posY = 350
                positX = -15
                positY = 260
            if raze == 2:
                X = 28
                Y = 345
                posX = 150
                posY = 350
                positX = 30
                positY = 260
            if raze == 3:
                X = 140
                Y = 440
                posX = 100
                posY = 350
                positX = 25
                positY = 260
            if raze == 4:
                X = 170
                Y = 310
                posX = 100
                posY = 350
                positX = -15
                positY = 240

            fondo = pygame.image.load("fondo.jpg")
            velocidad = 5
            verde = (0, 255, 0)
            derecha = True
            ventana.blit(fondo, (posX, posY))
            while True:
                ventana.fill(verde)
                ventana.blit(fondo, (0, 0))
                if nchar == "1":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                if nchar == "2":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX + 250, positY))
                    ventana.blit(imagen_personaje, (posX + 250, posY))
                    ventana.blit(imagen_arma, (X + 250, Y))
                if nchar == "3":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX + 250, positY))
                    ventana.blit(imagen_personaje, (posX + 250, posY))
                    ventana.blit(imagen_arma, (X + 250, Y))
                    ventana.blit(imagen_aurora, (positX + 500, positY))
                    ventana.blit(imagen_personaje, (posX + 500, posY))
                    ventana.blit(imagen_arma, (X + 500, Y))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                keys = pygame.key.get_pressed()
                if keys[K_LEFT]:
                    positX -= velocidad
                    X -= velocidad
                    posX -= velocidad
                elif keys[K_RIGHT]:
                    positX += velocidad
                    posX += velocidad
                    X += velocidad
                pygame.display.update()


# *** Defines window ***

root = Tk()
root.title("Character chooser")
root.configure(bg="#191919")

charChooser = charChooserGUI(root)

root.mainloop()
