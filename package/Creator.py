import random

#! Constantes
ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def creationRotor():
    copieAlpha = ALPHABET [:]
    random.shuffle(copieAlpha)
    return convertAlphaRotorToNumRotor(copieAlpha)

def convertAlphaRotorToNumRotor(alphaRotor):
    numRotor = []
    for letter in alphaRotor: # Pour chaque lettre du rouage
        #* il faut trouver le décalage (positif) existant entre la lettre d'entrée et la lettre de sortie (les nombres sont plus simples à manipuler)
        indexLettreDansWring = alphaRotor.index(letter)
        indexLettreDansAlphabet = ALPHABET.index(letter)
        decalage = indexLettreDansAlphabet - indexLettreDansWring # On obtient alors le décage ente chaque entrée sortie au niveau du toror
        numRotor.append(decalage) # On l'ajoute à notre nouveau wring numérique
    return numRotor

def convertAlphaReflToNumRefl(alphaRefl):
    numRefl = []
    for letter in alphaRefl:
        index = ALPHABET.index(letter)
        numRefl.append(index)
    return numRefl

print(creationRotor())