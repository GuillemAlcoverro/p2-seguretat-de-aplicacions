# 5 Ataquem el nostre propi RSA

from genera_claus import genera_claus
from xifra_text import xifra_text
from rsa import xifra


def construir_diccionari(e, n):
    """Construeix un diccionari c -> m per a tots els 256 bytes possibles."""
    diccionari = {}
    for m in range(256):
        c = xifra(m, e, n)
        diccionari[c] = m
    return diccionari


def atac_diccionari(criptograma, e, n):
    """Recupera el text xifrat sense la clau privada."""
    diccionari = construir_diccionari(e, n)
    dades = bytes(diccionari[c] for c in criptograma)
    return dades.decode("utf-8")


if __name__ == "__main__":
    (n, e), (_, d) = genera_claus(1009, 1013, 65537)

    # Xifrem un text amb la clau publica
    text_original = "La criptografia és divertida!"
    criptograma = xifra_text(text_original, e, n)
    print("Text original:", text_original)
    print("Criptograma:", criptograma)

    # Recuperem el text SENSE la clau privada, nomes amb la publica
    text_recuperat = atac_diccionari(criptograma, e, n)
    print("Text recuperat:", text_recuperat)
    print("Atac exitós?", text_original == text_recuperat)
