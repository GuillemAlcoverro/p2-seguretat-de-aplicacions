# 4.3 Què passa amb les repeticions?

from collections import Counter
from genera_claus import genera_claus
from xifra_text import xifra_text


if __name__ == "__main__":
    (n, e), _ = genera_claus(1009, 1013, 65537)

    for text in ["AAAAAAAAAA", "MISSISSIPPI", "ABRACADABRA", "AABBAABBAABB"]:
        criptograma = xifra_text(text, e, n)
        print(text)                                             # Text en clar
        print(criptograma)                                      # Criptograma
        print({k: v for k, v in Counter(criptograma).items() if v > 1})  # Criptogrames repeticits