# 3.2 Xifratge i desxifratge d'enters

from exponenciacio import exponenciacio_modular_rapida


def xifra(m, e, n):
    if not 0 <= m < n:
        return None
    return exponenciacio_modular_rapida(m, e, n)

def desxifra(c, d, n):
    return exponenciacio_modular_rapida(c, d, n)


if __name__ == "__main__":
    # Claus de l'apartat 3.1
    n, e, d = 3233, 17, 2753
    c = xifra(65, e, n)
    print(c)                            # Resultat: 2790
    print(desxifra(c, d, n))            # Resultat: 65
    print(xifra(n, e, n))               # Resultat: None (m = n, cal m < n)