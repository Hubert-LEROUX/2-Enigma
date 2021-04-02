from package.Plugboard import Plugboard
from package.Rotors import Rotors
from package.Reflector import Reflector

ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

class EnigmaMachine():

    def __init__(self, idRot, idRef, pairs=[("A","A"), ("B","B")], rotorsPos=[0,0,0]):
        self.FIRST_PARAMS = {"idRot":idRot, "idRef":idRef, "pairs":pairs, "rotorsPos":rotorsPos}
        self.rotors = Rotors(idRot, rotorsPos)
        self.refl = Reflector(idRef)
        if pairs:
            numericalPairs = []
            for pair in pairs:
                numPair = (ALPHABET.index(pair[0].upper()),ALPHABET.index(pair[1].upper())) # Transforme la pair alphabétique en une pair numérique 
                numericalPairs.append(numPair)
            self.plugBoard = Plugboard(numericalPairs)
        else: self.plugBoard = Plugboard([(0,0)])

    def reset(self):
        self.rotors = Rotors(self.FIRST_PARAMS["idRot"], self.FIRST_PARAMS["rotorsPos"])

    def encryptLetter(self, letter):
        indexLetter = ALPHABET.index(letter)
        indexLetter = self.plugBoard.changeLetter(indexLetter) # On change la lettre selon le plugBoard au départ
        indexLetter = self.rotors.runThrough(indexLetter, dansSensAller=True) # Premier Passage
        indexLetter = self.refl.reflect(indexLetter) # Réflecteur
        indexLetter = self.rotors.runThrough(indexLetter, dansSensAller=False) # Retour
        indexLetter = self.plugBoard.changeLetter(indexLetter) # On change la lettre selon le plugBoard à la fin
        return ALPHABET[indexLetter] # Retourne la lettre encryptée

    def encryptMessage(self, message):
        encryptedMessage = ""
        for caractere in message.upper():
            if caractere in ALPHABET: # Si c'est une lettre
                #* La frappe d'une touche provoquait d'abord une avancée sur les rotors et ensuite seulement une connexion électrique.
                self.rotors.moveRotors() 
                encryptedMessage += self.encryptLetter(caractere)
            else: #Signe de poctuation ou autre
                encryptedMessage += caractere
        return encryptedMessage
    
    def __repr__(self):
        return str(self.rotors) + str(self.plugBoard) + '\n'

# MESSAGE = "HELLO"
# ROTORS = ["II", "IV", "V"]
# REFLECTOR = "UKW B"
# POSITIONS = [2,21,12]
# PAIRS = "AV BS CG DL FU HZ IN KM OW RX"

# # ROTORS = ROTORS[-1::-1]
# # POSITIONS = POSITIONS[-1::-1]

# machine = EnigmaMachine(ROTORS, REFLECTOR, Plugboard.stringToListTuples(PAIRS), POSITIONS)
# encryptedMessage = machine.encryptMessage(MESSAGE)
# print(encryptedMessage)
# machine = EnigmaMachine(ROTORS, REFLECTOR, Plugboard.stringToListTuples(PAIRS), POSITIONS)
# print(MESSAGE)
# print(machine.encryptMessage(encryptedMessage))

