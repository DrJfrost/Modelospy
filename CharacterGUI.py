from tkinter import *


class charChooserGUI:

    def __init__(self, master):

        # ***** Parent Window Size ****
        master.minsize(width=1000, height=500)
        master.maxsize(width=1000, height=500)

        label = Label(bg="#3a3a3a")

        # **** Title ****

        title = Label(text="Choose your character", font="times 24 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Images ****

        img1 = PhotoImage(file="1.png")
        img2 = PhotoImage(file="2.png")
        img3 = PhotoImage(file="3.png")
        img4 = PhotoImage(file="4.png")

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
        root2.minsize(width=1000, height=500)

        # **** Content ***

        label = Label(bg="#3a3a3a")
        # **** Title ****

        title = Label(text="Choose your character", font="times 24 bold italic", fg="#ffca1e", bg="#3a3a3a")
        title.pack(pady=(50, 0))

        # ***** Images ****

        default = PhotoImage(file="default.png")

        char1 = Button(label, image=default, command=lambda: self.createChar(raze, 1), bg="black")
        char1.image = default
        char1.grid(row=0, padx=10, pady=5)
        char2 = Button(label, image=default, command=lambda: self.createChar(raze, 2), bg="black")
        char2.image = default
        char2.grid(row=0, column=1, padx=10, pady=5)
        char3 = Button(label, image=default, command=lambda: self.createChar(raze, 3), bg="black")
        char3.image = default
        char3.grid(row=0, column=2, padx=10, pady=5)
        char4 = Button(label, image=default, command=lambda: self.createChar(raze, 4), bg="black")
        char4.image = default
        char4.grid(row=0, column=3, padx=10, pady=5)

        # ****** Names *****

        name1 = Label(label, text="raza.getWeapon(1)", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="raza.getWeapon(2)", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name2.grid(row=1, column=1)
        name3 = Label(label, text="raza.getWeapon(3)", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name3.grid(row=1, column=2)
        name4 = Label(label, text="raza.getWeapon(4)", font="times 10 bold italic", fg="#ffca1e", bg="#3a3a3a")
        name4.grid(row=1, column=3)

        # *** Adds the whole content that's on the label ***

        label.pack()

    def createChar(self, raze, weapon):

        print("this would create raze number "+str(raze)+" with the weapon "+str(weapon))


# *** Defines window ***

root = Tk()
root.title("Character chooser")
root.configure(bg="#191919")

charChooser = charChooserGUI(root)

root.mainloop()
