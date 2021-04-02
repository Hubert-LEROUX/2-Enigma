ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

class Plugboard():
    def __init__(self, pairs):
        # Les pairs sont représentés par une liste de tuple
        self.pairs = pairs
    
    def changeLetter(self, letterNumber):
        letterNumber = mod26(letterNumber)
        for pair in self.pairs: # On regarde toutes les pairs
            if letterNumber in pair: # Si une des pairs contient le numéro en question
                return pair[(pair.index(letterNumber)+1)%2]
        return letterNumber

    def __repr__(self):
        """
        Renvoie une chaîne de caractère représentant l'objet
        """
        represenation = "====== PLUGBOARD ======\n"
        for pair in self.pairs:
            represenation += str(ALPHABET[pair[0]])+str(ALPHABET[pair[1]])+" "
        return represenation

    @staticmethod
    def stringToListTuples(stringPairs):
        """
        Elle permet de saisir plus feacilement les pairs
        :param: stringPairs est une chaîne de caractère avec les pères représentées comme ceci : "AB DE GL JH"
        :return: une liste de tuple où chaque tuple correspond à une paire
        """
        listeTuplePairs = []
        for pair in stringPairs.upper().split(" "):
            listeTuplePairs.append((pair[0],pair[1])) # On ajoute la pair à celle connue
        return listeTuplePairs

# myPlug = Plugboard([(0,5),(1,6), (2,7), (3,8), (4, 9)])
# print(myPlug)

