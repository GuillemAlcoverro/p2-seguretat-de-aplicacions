def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print (euclides(1728, 842)) # Resultat: 2