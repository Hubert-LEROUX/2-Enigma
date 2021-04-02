from tkinter import Tk, Canvas, StringVar, OptionMenu, IntVar, Entry, Button, Text, END
from EnigmaMachine import EnigmaMachine
from package.Plugboard import Plugboard

#! Constantes
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
RAYON_VOYANT = 30
DISTANCE_ENTRE_VOYANT = 3*RAYON_VOYANT
BG_FOND = "#5A2E00"
BG_COLOR_INACTIF = "#FFFFFF"
BG_COLOR_ACTIF = "#FFFF00"
OUTLINE_COLOR_INACTIF = "#000000"
WIDTH_OUTLINE_VOYANT = 5
FONT_VOYANT = ('Helvetica', 36, 'bold')
FONT_LABELS = ('Helvetica', 36, 'bold')
IS_ENCIPHERING = False

PARAMS = {"RotorIDs":["I", "II", "III"], "ReflectorID":"UKW A", "RotorPositions":[0,0,0], "Pairs":"AA"}


listeRotorIds = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "BETA", "GAMMA")
listeReflectorIds = ("UKW A", "UKW B", "UKW C", "UKW BRUNO", "UKW CASAR")
listeRotorPositions = tuple(range(26))

def begin(event=None):
    global IS_ENCIPHERING
    IS_ENCIPHERING = True

def stop(event=None):
    global IS_ENCIPHERING
    IS_ENCIPHERING = False

def toggle_fullscreen(event=None):
    fen.attributes("-fullscreen", True)
    

def end_fullscreen(event=None):
    fen.attributes("-fullscreen", False)
    fen.state("zoomed")

class Voyant():
    """
    Classe d'un voyant
    """

    listeVoyants = []

    def __init__(self, x, y, letter, canvas):
        # Récupère l'emplacement du voyant et la lettre qu'il affiche
        self.x = x
        self.y = y
        self.letter = letter
        self.cercle = canvas.create_oval(x-RAYON_VOYANT, y-RAYON_VOYANT, x+RAYON_VOYANT, y+RAYON_VOYANT, fill=BG_COLOR_INACTIF, outline=OUTLINE_COLOR_INACTIF, width=WIDTH_OUTLINE_VOYANT)
        self.label = canvas.create_text(x,y,fill=OUTLINE_COLOR_INACTIF, text=letter.upper(), font=FONT_VOYANT)
        Voyant.listeVoyants.append(self)

    def activate(self):
        """
        Active un voyant
        """
        fond.itemconfigure(self.cercle, fill=BG_COLOR_ACTIF)

    def desactivate(self):
        """
        Desactive le voyant
        """
        fond.itemconfigure(self.cercle, fill=BG_COLOR_INACTIF)

    @staticmethod
    def desactivate_all():
        """
        Fonction statique desactivant tous les voyants
        """
        for voyant in Voyant.listeVoyants:
            voyant.desactivate()
        
def setEnigmaMachine():
    global machine
    machine = EnigmaMachine([rotorId1.get(), rotorId2.get(), rotorId3.get()], reflectorId.get(),
     Plugboard.stringToListTuples( entryPairs.get() ), [rotorPosition1.get(), rotorPosition2.get(), rotorPosition3.get()])
    texteTraduit.delete(1.0,END)
    texteInput.delete(1.0,END)
    # SAVING NEW PARAMS
    PARAMS["RotorIDs"] = [rotorId1.get(), rotorId2.get(), rotorId3.get()]
    PARAMS["RotorPositions"] = [rotorPosition1.get(), rotorPosition2.get(), rotorPosition3.get()]
    PARAMS["ReflectorID"] = reflectorId.get()
    PARAMS["Pairs"] = entryPairs.get()

def resetEnigmaMachine():
    """
    Reset la machine à partir des anciens paramètres
    """
    global machine
    machine = EnigmaMachine(PARAMS["RotorIDs"], PARAMS["ReflectorID"],
     Plugboard.stringToListTuples( PARAMS["Pairs"] ), PARAMS["RotorPositions"])
    texteTraduit.delete(1.0,END)
    texteInput.delete(1.0,END)
    rotorPosition1.set(PARAMS["RotorPositions"][0])
    rotorPosition2.set(PARAMS["RotorPositions"][1])
    rotorPosition3.set(PARAMS["RotorPositions"][2])

def keyPressed(event): #Lorsqu'une touche est pressée
    global rotorPosition1, rotorPosition2, rotorPosition3
    if IS_ENCIPHERING: #Si on est en train de décoder
        l = event.keysym.upper()
        if l in ALPHABET:
            # texteInput.insert("end", l) #On insère la lettre au texte d'entrée
            Voyant.desactivate_all() #On desactive tous les voyant
            encryptedLetter = machine.encryptMessage(l) # On encrypte la lettre saisie
            voyant = eval("voyant"+str(encryptedLetter)) # On trouve le voyant correspondant à la lettre cryptée
            texteTraduit.insert("end", encryptedLetter) #On isère la lettre traduite au texte
            voyant.activate() #On allume le voyant
        rotorPosition1.set(machine.rotors.rotor1.position)
        rotorPosition2.set(machine.rotors.rotor2.position)
        rotorPosition3.set(machine.rotors.rotor3.position)



fen = Tk() # Création d'un objet fenêtre
fen.title("Enigma Machine")
fen.resizable(True, True) # Cette fenêtre peut être redimensionner
fen.iconbitmap("res/icon.ico") # Set icon

#* Full Screen
pad = 0
# .fengeometry("{0}x{1}+0+0".format(fen.winfo_screenwidth()-pad, fen.winfo_screenheight()-pad))
# fen.attributes("-fullscreen", True) #On commence en full screnn
fen.state("zoomed")
fen.bind("<F11>", toggle_fullscreen) # Se mettre en full screen
fen.bind("<Escape>", end_fullscreen) # Enlever le full screen

#Canvas
fond = Canvas(fen, background=BG_FOND, width=fen.winfo_width(), height=fen.winfo_height())
fond.place(x=0,y=0)

#* =================== Création des 26 voyants ===================
FIRST_X_ROW = 300
Y_FIRST_ROW = 400
Y_SECOND_ROW = 500
Y_THIRD_ROW = 600
voyantA = Voyant(FIRST_X_ROW+0*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "A", fond)
voyantZ = Voyant(FIRST_X_ROW+1*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "Z", fond)
voyantE = Voyant(FIRST_X_ROW+2*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "E", fond)
voyantR = Voyant(FIRST_X_ROW+3*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "R", fond)
voyantT = Voyant(FIRST_X_ROW+4*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "T", fond)
voyantY = Voyant(FIRST_X_ROW+5*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "Y", fond)
voyantU = Voyant(FIRST_X_ROW+6*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "U", fond)
voyantI = Voyant(FIRST_X_ROW+7*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "I", fond)
voyantO = Voyant(FIRST_X_ROW+8*DISTANCE_ENTRE_VOYANT,Y_FIRST_ROW, "O", fond)
voyantP = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+0*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "P", fond)
voyantQ = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+1*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "Q", fond)
voyantS = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+2*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "S", fond)
voyantD = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+3*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "D", fond)
voyantF = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+4*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "F", fond)
voyantG = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+5*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "G", fond)
voyantH = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+6*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "H", fond)
voyantJ = Voyant(FIRST_X_ROW+DISTANCE_ENTRE_VOYANT/2+7*DISTANCE_ENTRE_VOYANT,Y_SECOND_ROW, "J", fond)
voyantK = Voyant(FIRST_X_ROW+0*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "K", fond)
voyantL = Voyant(FIRST_X_ROW+1*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "L", fond)
voyantM = Voyant(FIRST_X_ROW+2*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "M", fond)
voyantW = Voyant(FIRST_X_ROW+3*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "W", fond)
voyantX = Voyant(FIRST_X_ROW+4*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "X", fond)
voyantC = Voyant(FIRST_X_ROW+5*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "C", fond)
voyantV = Voyant(FIRST_X_ROW+6*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "V", fond)
voyantB = Voyant(FIRST_X_ROW+7*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "B", fond)
voyantN = Voyant(FIRST_X_ROW+8*DISTANCE_ENTRE_VOYANT,Y_THIRD_ROW, "N", fond)

#* ======================= Réglages ========================
# RotorIDs
rotorId1 = StringVar()
rotorId2 = StringVar()
rotorId3 = StringVar()
rotorId1.set(listeRotorIds[0])
rotorId2.set(listeRotorIds[1])
rotorId3.set(listeRotorIds[2])
omRotorId1 = OptionMenu(fen, rotorId1, *listeRotorIds)
omRotorId2 = OptionMenu(fen, rotorId2, *listeRotorIds)
omRotorId3 = OptionMenu(fen, rotorId3, *listeRotorIds)
# RotorPositions
rotorPosition1 = IntVar()
rotorPosition2 = IntVar()
rotorPosition3 = IntVar()
rotorPosition1.set(listeRotorPositions[0])
rotorPosition2.set(listeRotorPositions[0])
rotorPosition3.set(listeRotorPositions[0])
omRotorPosition1 = OptionMenu(fen, rotorPosition1, *listeRotorPositions)
omRotorPosition2 = OptionMenu(fen, rotorPosition2, *listeRotorPositions)
omRotorPosition3 = OptionMenu(fen, rotorPosition3, *listeRotorPositions)
# ReflectoID
reflectorId = StringVar()
reflectorId.set(listeReflectorIds[0])
omRelflectorId = OptionMenu(fen, reflectorId, *listeReflectorIds)

fond.create_text(150, 165, text="Rotor ID", font=FONT_LABELS)
fond.create_text(150, 215, text="Position", font=FONT_LABELS)
fond.create_text(150, 265, text="Pairs", font=FONT_LABELS)
for i in range(3):
    fond.create_text(350+i*100, 80, text=str(i+1), font=FONT_LABELS)
    # Rotor ID OM
    omRotorId = eval("omRotorId"+str(i+1))
    omRotorId.place(x=330+i*100, y=150)
    # RotorPosition OM
    omRotorPosition = eval("omRotorPosition"+str(i+1))
    omRotorPosition.place(x=330+i*100, y=200)

entryPairs = Entry(fen, width=19, font=("Helvetica", 18, "bold"))
entryPairs.place(x=330, y=255)
entryPairs.insert(0,"AA")


fond.create_text(850, 165, text="Reflector ID", font=FONT_LABELS)
omRelflectorId.place(x=1000,y=150)

# SET BUTTON
setButton = Button(fen, text="SET", font=("Helvetica", 15, "bold"), command=setEnigmaMachine)
setButton.place(x=800,y=220)

# RESET BUTTON
resetButton = Button(fen, text="RESET", font=("Helvetica", 15, "bold"), command=resetEnigmaMachine)
resetButton.place(x=795,y=270)

# TEXTE INPUT
texteInput = Text(fen, bg="white", height=50, width=30)
texteInput.place(x=0, y=300)

# TEXTE TRADUIT
texteTraduit = Text(fen, bg="white", height=100, width=34)
texteTraduit.place(x=1100, y=5)

# Création de la machine
machine = EnigmaMachine([rotorId1.get(), rotorId2.get(), rotorId3.get()], reflectorId.get(), [("A", "A")],
 [rotorPosition1.get(),rotorPosition2.get(),rotorPosition3.get()])

fen.bind("<F1>", begin) # Commence
fen.bind("<F2>", stop) # Arrêt



fen.bind("<Key>", keyPressed)

fen.mainloop()