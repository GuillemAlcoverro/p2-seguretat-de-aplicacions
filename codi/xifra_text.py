# 4.2 RSA byte a byte

from genera_claus import genera_claus
from rsa import xifra, desxifra


def xifra_text(text, e, n):
    # Un byte nomes pot pprendre valors de 0 a 255, cal n > 255
    if n <= 255:
        return None
    return [xifra(b, e, n) for b in text.encode("utf-8")]

def desxifra_text(criptograma, d, n):
    dades = bytes(desxifra(c, d, n) for c in criptograma)
    return dades.decode("utf-8")


if __name__ == "__main__":
    print(xifra_text("Hola!", 17, 200))  # Resultat: None

    (n, e), (_, d) = genera_claus(1009, 1013, 65537)
    text = "La criptografia és divertida!"
    criptograma = xifra_text(text, e, n)
    print(criptograma)
    print(desxifra_text(criptograma, d, n))  # Resultat: La criptografia és divertida!