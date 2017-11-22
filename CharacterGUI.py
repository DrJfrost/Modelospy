from tkinter import *
from EnlistCharacter import EnlistCharacter
import pygame, sys
from pygame.locals import *
from random import randint


class charChooserGUI:
    imageweapon = None

    def __init__(self, master):

        pygame.mixer.init()
        pygame.mixer.music.load('Musica\musica1.wav')
        pygame.mixer.music.play(-1)

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

        char1 = Button(label, image=img1, command=lambda: self.chooseConjurer(master), bg="black")
        char1.image = img1
        char1.grid(row=0, padx=10, pady=5)
        char2 = Button(label, image=img2, command=lambda: self.chooseWeapon(2, master), bg="black")
        char2.image = img2
        char2.grid(row=0, column=1, padx=10, pady=5)
        char3 = Button(label, image=img3, command=lambda: self.chooseWeapon(3, master), bg="black")
        char3.image = img3
        char3.grid(row=0, column=2, padx=10, pady=5)
        char4 = Button(label, image=img4, command=lambda: self.chooseWeapon(4, master), bg="black")
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

    def chooseConjurer(self, root):

        root.destroy()
        root2 = Tk()
        root2.title("Conjurer Chooser")
        root2.configure(bg="#191919")
        root2.minsize(width=660, height=460)

        # *** Main content ***

        label = Label(bg="#3a3a3a")

        #*** Inner content ***

        title = Label(text="Which side do you want to be? D:<", font="times 22 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(40, 0))

        img1 = PhotoImage(file="images_characters/1.png")
        img2 = PhotoImage(file="images_characters/5.png")

        char1 = Button(label, image=img1, command=lambda: self.chooseWeapon(1, root2), bg="black", highlightbackground="#222222")
        char1.image = img1
        char1.grid(row=0, padx=(40,40), pady=10)
        char2 = Button(label, image=img2, command=lambda: self.chooseWeapon(5, root2), bg="black")
        char2.image = img2
        char2.grid(row=0, column=1, padx=(40,40), pady=10)

        # ****** Names *****

        name1 = Label(label, text="Good  Witch", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Evil Witch", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)

        label.pack()

    def chooseWeapon(self, raze, root):

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

        if (raze1 == 1) or (raze1 == 5):
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

        pygame.mixer.music.stop()

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


        class Cursor(pygame.Rect):

            def __init__(self):
                pygame.Rect.__init__(self,0,0,1,1)
            def update(self):
                self.left,self.top=pygame.mouse.get_pos() 
        class Boton(pygame.sprite.Sprite):
            def __init__(self,imagen1,imagen2,x=200,y=200):
                self.imagen_normal=imagen1
                self.imagen_seleccion=imagen2
                self.imagen_actual=self.imagen_normal
                self.rect=self.imagen_actual.get_rect()
                self.rect.left,self.rect.top=(x,y)

            def update(self,pantalla,cursor):
                if cursor.colliderect(self.rect):
                    self.imagen_actual=self.imagen_seleccion
                else: self.imagen_actual=self.imagen_normal

                pantalla.blit(self.imagen_actual,self.rect)


        class Animation():

            pygame.init()
            ventana = pygame.display.set_mode((1024, 683))
            pygame.display.set_caption("personajes")

            atras1=pygame.image.load("boton/button11.png")
            atras2=pygame.image.load("boton/button1.png")

            boton1=Boton(atras1,atras2,0,0)
            cursor1=Cursor()

            imagen_cursor=pygame.image.load("cursor/sword.png")
            pX=0
            pY=0

            imagen_arma = pygame.image.load(imweapon)

            imagen_personaje = pygame.image.load(imchar)
            imagen_aurora = pygame.image.load(imAurora)


            if (raze == 1) or (raze == 5):
                
                X = 90
                Y = 310
                X1 = 340
                Y1 = 310
                X2 = 590
                Y2 = 310
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = -15
                positY = 260
                positX1 = 235
                positY1 = 260
                positX2 = 485
                positY2 = 260
                
            if raze == 2:
                X = 28
                Y = 345
                X1 = 278
                Y1 = 345
                X2 = 528
                Y2 = 345
                posX = 150
                posY = 350
                posX1 = 400
                posY1 = 350
                posX2 = 650
                posY2 = 350
                positX = 30
                positY = 260
                positX1 = 280
                positY1 = 260
                positX2 = 530
                positY2 = 260
            if raze == 3:
                X = 140
                Y = 440
                X1 = 390
                Y1 = 440
                X2 = 640
                Y2 = 440
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = 25
                positY = 260
                positX1 = 275
                positY1 = 260
                positX2 = 525
                positY2 = 260
            if raze == 4:
                X = 170
                Y = 310
                X1 = 420
                Y1 = 310
                X2 = 670
                Y2 = 310
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = -15
                positY = 240
                positX1 = 235
                positY1 = 240
                positX2 = 485
                positY2 = 240

            fondo = pygame.image.load("fondo.jpg")
            velocidad = 5
            verde = (0, 255, 0)
            derecha = True
           
            pygame.mixer.music.load('Musica\musica1.wav')
            pygame.mixer.music.play(-1)
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
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                if nchar == "3":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                    ventana.blit(imagen_aurora, (positX2, positY2))
                    ventana.blit(imagen_personaje, (posX2, posY2))
                    ventana.blit(imagen_arma, (X2, Y2))
                ventana.blit(imagen_cursor, (pX,pY))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cursor1.colliderect(boton1.rect):
                            root = Tk()
                            root.title("Character chooser")
                            root.configure(bg="#191919")

                            charChooser = charChooserGUI(root)
                            pygame.display.quit()
                            pygame.mixer.init()
                            pygame.mixer.music.load('Musica\musica1.wav')
                            pygame.mixer.music.play(-1)
                            root.mainloop() 
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
                if keys [K_a]:
                    positX1 -= velocidad
                    X1 -= velocidad
                    posX1 -= velocidad
                elif keys[K_d]:
                    positX1 += velocidad
                    posX1 += velocidad
                    X1 += velocidad
                if keys [K_j]:
                    positX2 -= velocidad
                    X2 -= velocidad
                    posX2 -= velocidad
                elif keys [K_l]:
                    positX2 += velocidad
                    posX2 += velocidad
                    X2 += velocidad
                if keys[K_SPACE]:
                    personaje1.attack()

                cursor1.update()
                boton1.update(ventana,cursor1)
                pX,pY= pygame.mouse.get_pos()
                pX= pX-80
                pY= pY-90
                pygame.mouse.set_visible(False)
                
                pygame.display.update()



# *** Defines window ***

root = Tk()
root.title("Character chooser")
root.configure(bg="#191919")

charChooser = charChooserGUI(root)

root.mainloop()
