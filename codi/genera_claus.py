# 3.1 Un primer exemple / 3.3 Les vostres claus

from euclides import euclides, invers_modular


def es_primer(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def genera_claus(p, q, e):
    if not es_primer(p) or not es_primer(q) or p == q:
        return None
    n = p * q
    phi = (p - 1) * (q - 1)
    if euclides(e, phi) != 1:
        return None
    d = invers_modular(e, phi)
    return (n, e), (n, d)


if __name__ == "__main__":
    # 3.1 Un primer exemple
    p, q = 61, 53
    phi = (p - 1) * (q - 1)
    (n, e), (_, d) = genera_claus(p, q, 17)
    print(n)                            # Resultat: 3233
    print(phi)                          # Resultat: 3120
    print(euclides(e, phi))             # Resultat: 1
    print(d)                            # Resultat: 2753

    # 3.3 Les vostres claus
    (n, e), (_, d) = genera_claus(1009, 1013, 65537)
    print(n, e, d)                      # Resultat: 1022117 65537 832193

    # Els parametres invalids es rebutgen retornant None
    print(genera_claus(1009, 1009, 65537))  # Resultat: None (p = q)
    print(genera_claus(1001, 1013, 65537))  # Resultat: None (1001 no es primer)
    print(genera_claus(1009, 1013, 1000))   # Resultat: None (e no es coprimer)
    print(genera_claus(1009, 1013, 4))      # Resultat: None (e no es coprimer)