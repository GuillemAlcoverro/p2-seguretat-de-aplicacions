def exponenciacio_modular_rapida(a, b, n):
    resultat = 1 % n
    base = a % n
    while b > 0:
        if b % 2 == 1:
            resultat = (resultat * base) % n
        base = (base * base) % n
        b //= 2
    return resultat


if __name__ == "__main__":
    print(exponenciacio_modular_rapida(65, 17, 3233)) # Resultat: 2790