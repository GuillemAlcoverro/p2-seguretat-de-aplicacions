# 9 Auditoria d'un programa generat per IA

from euclides import invers_modular


def genera_claus(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = invers_modular(e, phi) # la IA no ha creat la funcio invers_modular, l'hem afegida nosaltres
    return (n, e), (n, d)

def xifra_text(text, e, n):
    return [
        pow(ord(c), e, n)
        for c in text
    ]


if __name__ == "__main__":

    print("9.1 Generacio de les claus")

    # p = q
    (n, e), (_, d) = genera_claus(13, 13, 5)
    print("p = q = 13 -> n =", n, " d =", d)
    print("  xifra 7 =", pow(7, e, n), " desxifra =", pow(pow(7, e, n), d, n), "-> INCORRECTE")

    # p no es primer (51 = 3 * 17)
    (n, e), (_, d) = genera_claus(51, 61, 7)
    print("p = 51 (compost) -> n =", n, " d =", d)
    print("  xifra 10 =", pow(10, e, n), " desxifra =", pow(pow(10, e, n), d, n), "-> INCORRECTE")

    # q no es primer (1024 = 2^10)
    (n, e), (_, d) = genera_claus(1009, 1024, 65537)
    print("q = 1024 (compost) -> n =", n, " d =", d)
    print("  xifra 42 =", pow(42, e, n), " desxifra =", pow(pow(42, e, n), d, n), "-> INCORRECTE")

    # e no coprimer amb phi(n)
    print("e = 13, phi = 3120 ->", genera_claus(61, 53, 13), "-> INCORRECTE (d = None)")

    print()
    print("9.2 Xifratge del text")

    # ord(c) vs c.encode("utf-8")
    print("ord('A') =", ord("A"), " utf-8 =", list("A".encode("utf-8")))
    print("ord('ú') =", ord("ú"), " utf-8 =", list("ú".encode("utf-8")), "-> INCORRECTE")
    print("ord('ç') =", ord("ç"), " utf-8 =", list("ç".encode("utf-8")), "-> INCORRECTE")

    # no es comprova m < n
    print("ord('€') =", ord("€"), "> n = 3233, es redueix a", ord("€") % 3233, "-> INCORRECTE")

    # dos lletres iguals
    print("AAAAAAAAAA ->", xifra_text("AAAAAAAAAA", 17, 3233), "-> INCORRECTE")
    print("MISSISSIPPI ->", xifra_text("MISSISSIPPI", 17, 3233), "-> INCORRECTE")

    print()
    print("9.3 Conclusio: SI / NO / NO")
