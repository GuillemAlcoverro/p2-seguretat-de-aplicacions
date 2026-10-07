def euclides(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def euclides_extens(a, b):
    if b == 0:
        return a, 1, 0
    d, x, y = euclides_extens(b, a % b)
    return d, y, x - (a // b) * y

def invers_modular(a, n):
    d, x, _ = euclides_extens(a, n)
    if d != 1:
        return None
    return x % n

if __name__ == "__main__":
    print (euclides(1728, 842)) # Resultat: 2
    print (euclides(240, 46)) # Resultat: 2
    print (euclides_extens(1728, 842)) # Resultat: (2, 134, -275)
    print(invers_modular(17, 3120)) # Resultat: 2753