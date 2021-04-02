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

# a = -1
# print("a="+str(a))
# print("a congru modulo 26 à "+str(Modulo26(a)))
# print("a="+str(a))
