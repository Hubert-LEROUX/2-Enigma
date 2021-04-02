# Enigma Program

# ? https://en.wikipedia.org/wiki/Enigma_rotor_details --> Détails officiels sur tous les rotors !
# ? https://de.wikipedia.org/wiki/Enigma-Walzen en allemand c plus complet

# I 	EKMFLGDQVZNTOWYHXUSPAIBRCJ 	1930 	Enigma I
# II 	AJDKSIRUXBLHWTMCQGZNPYFVOE 	1930 	Enigma I
# III 	BDFHJLCPRTXVZNYEIWGAKMUSQO 	1930 	Enigma I
# IV 	ESOVPZJAYQUIRHXLNFTGKDCMWB 	15. Dezember 1938 	M3 (Heer)
# V 	VZBRGITYUPSDNHLXAWMJQOFECK 	15. Dezember 1938 	M3 (Heer)
# VI 	JPGVOUMFYQBENHZRDKASXLICTW 	1939 	M3 und M4
# VII 	NZJHGRCXMYSWBOUFAIVLPEKQDT 	1939 	M3 und M4
# VIII 	FKQHTLXOCBJSPDZRAMEWNIUYGV 	1939 	M3 und M4 

# TODO C'est peut-être cela qui gêne, les rotors ne sont entraînés qu'à un certain moment
#? https://www.instagram.com/p/BDYwoLeEq3m/?utm_source=ig_embed&utm_campaign=loading
# Rotor 	Positions 	Effet
# I 	Q 	la transition Q vers R provoque l'avancée du rotor suivant
# II 	E 	la transition E vers F provoque l'avancée du rotor suivant
# III 	V 	la transition V vers W provoque l'avancée du rotor suivant
# IV 	J 	la transition J vers K provoque l'avancée du rotor suivant
# V 	Z 	la transition Z vers A provoque l'avancée du rotor suivant
# VI, VII et VIII 	Z et M 	une transition Z vers A, ou M vers N, provoque l'avancée du rotor suivant 

#! CONSTANTES
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def mod26(input):
    """
    Returne le nombre d'entrée modulo 26
    """
    # Pour forcer l'input à être positif
    while input < 0 :
        input += 26
    # pour forcer l'input à être compris entre 0 et 26
    input = input % 26
    return input

class Rotor(): 
    """
    Un rotor de la machine
    """

    def __init__(self, idRotor, rotorPosition):
        self.id = idRotor # On enregistre le type de rotor
        self.position = 0 # Initialisé à 0
        # Fixation des wring pour Enigma I
        if idRotor == "I": self.wring = [4, 9, 10, 2, 7, 1, -3, 9, 13, 16, 3, 8, 2, 9, 10, -8, 7, 3, 0, -4, -20, -13, -21, -6, -22, -16]
        elif idRotor == "II": self.wring = [0, 8, 1, 7, 14, 3, 11, 13, 15, -8, 1, -4, 10, 6, -2, -13, 0, -11, 7, -6, -5, 3, -17, -2, -10, -21]
        elif idRotor == "III": self.wring = [1, 2, 3, 4, 5, 6, -4, 8, 9, 10, 13, 10, 13, 0, 10, -11, -8, 5, -12, -19, -10, -9, -2, -5, -8, -11]
        elif idRotor == "IV": self.wring = [4, 17, 12, 18, 11, 20, 3, -7, 16, 7, 10, -3, 5, -6, 9, -4, -3, -12, 1, -13, -10, -18, -20, -11, -2, -24]
        elif idRotor == "V": self.wring = [21, 24, -1, 14, 2, 3, 13, 17, 12, 6, 8, -8, 1, -6, -3, 8, -16, 5, -6, -10, -4, -7, -17, -19, -22, -15]
        elif idRotor == "VI": self.wring = [9, 14, 4, 18, 10, 15, 6, -2, 16, 7, -9, -7, 1, -6, 11, 2, -13, -7, -18, -1, 3, -10, -14, -21, -5, -3]
        elif idRotor == "VII": self.wring = [13, 24, 7, 4, 2, 12, -4, 16, 4, 15, 8, 11, -11, 1, 6, -10, -16, -9, 3, -8, -5, -17, -12, -7, -21, -6]
        elif idRotor == "VIII": self.wring = [5, 9, 14, 4, 15, 6, 17, 7, -6, -8, -1, 7, 3, -10, 11, 2, -16, -5, -14, 3, -7, -13, -2, 1, -18, -4]
        
        # Enigma M4
        elif idRotor == "BETA": self.wring = [11, 3, 22, 6, 17, -3, 7, 1, 15, 13, 5, -10, 4, -1, -11, 2, 3, -17, -8, 6, -14, -16, -2, -16, -10, -7]
        elif idRotor == "GAMMA": self.wring = [5, 17, 12, 7, -4, 8, 14, -3, 9, -2, 2, -10, 7, -5, 10, -13, 6, -6, -2, -4, 5, 2, -1, -17, -15, -22]

        else: raise ValueError("There isn't any rotor called "+idRotor+" !") #! Renvoie une exception si les paramètres sont invalides

        self.turn(rotorPosition)# On avance le rotor à sa position
        self.lastPosition = 0 # Position antécédente de celle actuelle

    def vientDeBouger(self):
        if self.lastPosition == self.position: return False # Il ne vient pas de bouger
        else: return True
        

    def runThrough(self, input, dansSensAller = True):
        """
        Ressort la lettre sortnant du rotor en fonction de l'entrée
        Input est un nombre congru modulo 26 à la lettre qu'il représente
        """
        input = mod26(input)
        if dansSensAller: return mod26(input + self.wring[input]) # Passage dans le bon sens
        # en sens inverse
        # Il faut chercher la lettre, qui, encryptée dans le bon sens donne notre lettre
        for l in range(0,26): # In teste donc toutes les lettres
            if mod26(l + self.wring[l]) == input: # On a trouvé la lettre
                return l # On la renvoie
        return None


    def turn(self, dec=1):
        """
        Tourne le rouage
        dec --> de combien faut-il tourner
        """
        self.position = mod26(self.position+dec) # On incrémente la position tout en apliquant le modulo 26
        self.wring = self.wring[-dec:] + self.wring[:-dec] # On d"place wring
        return self

    def crochetEntraineAvanceeRotorSuivant(self):
        """
        Détermine suivant le rotor si l'appuie d'une touche va entraîner le rotor
        """
        if self.id == "I" and self.position == ALPHABET.index("Q") : return True
        elif self.id == "II" and self.position == ALPHABET.index("E") : return True
        elif self.id == "III" and self.position == ALPHABET.index("V") : return True
        elif self.id == "IV" and self.position == ALPHABET.index("J") : return True
        elif self.id == "V" and self.position == ALPHABET.index("Z") : return True
        elif self.id in ("VI","VII", "VIII")  and (self.position == ALPHABET.index("M") or self.position == ALPHABET.index("Z")) : return True
        return False
    
    def __repr__(self):
        """
        Renvoie une représentation du rotor
        """
        return "ID\t"+self.id+"\nPOSITION\t"+str(self.position)+"\nWRING\t"+str(self.wring)


class Rotors():
    def __init__(self, idRotors, rotorPositions=[0,0,0]):
        self.rotor1 = Rotor(idRotors[0], rotorPositions[0])
        self.rotor2 = Rotor(idRotors[1], rotorPositions[1])
        self.rotor3 = Rotor(idRotors[2], rotorPositions[2])

    def moveRotors(self):
        # On sauvegarde les dernières positions
        self.rotor1.lastPosition = self.rotor1.position
        self.rotor2.lastPosition = self.rotor2.position
        self.rotor3.lastPosition = self.rotor3.position

        self.rotor1.turn() # Le premier rotor tourne à chaque fois
        
        # Mécanisme d'avancée sans crochets
        if self.rotor1.position == 0 : # C'est à dire que le premier rotor vient de faire un tour compler
            self.rotor2.turn() # Le second rotor suivant est entraîne
            if self.rotor2.position == 0 : # C'est à dire que le deuxième rotor vient de faire un tour compler
                self.rotor3.turn() # Le second rotor suivant est entraîne
        else : # Autre moyen (crochets)
            if self.rotor1.crochetEntraineAvanceeRotorSuivant(): # Le rotor 1 entraîne le suivant
                self.rotor2.turn()
            #  On met if car l'un n'emp^che pas l'autre
            if self.rotor2.crochetEntraineAvanceeRotorSuivant() and self.rotor2.vientDeBouger(): # Le rotor 2 entraîne le suivant
                self.rotor2.turn()
                self.rotor3.turn()

    def runThrough(self, input, dansSensAller=True):
        """
        Effectue un passage complet des 3 rotors
        """
        output = 0
        if dansSensAller:
            output = self.rotor1.runThrough(input)
            output = self.rotor2.runThrough(output)
            output = self.rotor3.runThrough(output)
        else:
            output = self.rotor3.runThrough(input, False)
            output = self.rotor2.runThrough(output, False)
            output = self.rotor1.runThrough(output, False)
        return output

        

    def __repr__(self):
        return "=========== ROTOR 1 ===========\n" + str(self.rotor1) + "\n\n=========== ROTOR 2 ===========\n" + str(self.rotor2) + "\n\n=========== ROTOR 3 ===========\n" + str(self.rotor3) + "\n\n"

        

# mesRotors = Rotors(["I", "II", "III"], [0,0,0])
# print(mesRotors)
# monRotor = Rotor("I", 0)
# for letter in range(0,26):
#     print(ALPHABET[monRotor.runThrough(letter)],end="")
# print(ALPHABET[monRotor.runThrough(monRotor.runThrough(0), dansSensAller=False)])




