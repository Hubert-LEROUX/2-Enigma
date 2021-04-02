#? Documentation 
# UKW A 	EJMZALYXVBWFCRQUONTSPIKHGD 		
# UKW B 	YRUHQSLDPXNGOKMIEBFZCWVJAT 	2. November 1937 	
# UKW C 	FVPJIAOYEDRZXWGCTKUQSBNMHL 	1940/41 	
# [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]
# [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
# [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

#! Constantes
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

class Reflector():
    def __init__(self, idReflector):
        # Mise en place du réflecteur selon les modèles
        if idReflector == "UKW A": self.refl = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]
        elif idReflector == "UKW B": self.refl = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
        elif idReflector == "UKW C": self.refl = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]
        elif idReflector == "UKW BRUNO": self.refl = [4, 13, 10, 16, 0, 20, 24, 22, 9, 8, 2, 14, 15, 1, 11, 12, 3, 23, 25, 21, 5, 19, 7, 17, 6, 18]
        elif idReflector == "UKW CASAR": self.refl = [17, 3, 14, 1, 9, 13, 19, 10, 21, 4, 7, 12, 11, 5, 2, 22, 25, 0, 23, 6, 24, 8, 15, 18, 20, 16]
        else: raise ValueError("There isn't any reflector called "+idReflector+" !") #! Renvoie une exception si les paramètres sont invalides


    def reflect(self, input):
        input = mod26(input)
        output = self.refl[input]
        return output
