# Ús de la intel·ligència artificial

## 1. Per a què l'hem utilitzada

Hem usat l'IA en els programes del lliurament i en la redacció de l'informe per estructurar el codi en els fitxers de `codi/`, depurar-lo, fer-lo més robust a partir de les nostres versions inicials i revisar-ne el disseny. També l'hem utilitzada a l'hora d'anar aclarint dubtes sobre RSA.

## 2. Fragment acceptat

Vam acceptar la sugerència de la última línia de l'anàlisi de les repeticions de `repetitions.py`. Aquesta línia resumeix els criptogrames que es repeteixen.

```python
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
```

D'aquesta manera es veu de cop quins criptogrames es repeteixen i quants cops, la prova empirical que dos bytes iguals sempre produeixen el mateix criptograma.

## 3. Propostes descartades o corregides

- Vam descartar una proposta d'automatitzar les comandes d'OpenSSL en scripts `.sh`. Vam preferir executar-les directament a la terminal, perquè així quedava clar què feia cadascuna, i vam esborrar els scripts.
- La IA va crear de nou la funció `invers_modular` per a l'apartat d'auditoria perquè funcionés, nosaltres vam optar per fer servir la que ja havíem implementat nosaltres.

## 4. Com hem comprovat que el programa funciona

Hem verificat el programa per anada i tornada. Desxifrar amb la clau privada recuperava exactament el text original (`La criptografia és divertida!`) i `xifra` rebutja valors que no compleixen `0 ≤ m < n`. A més, els scripts de les seccions 2 i 3 comproven els valors de l'enunciat (`invers_modular(17, 3120) = 2753`, `65¹⁷ mod 3233 = 2790`, `n = 3233`, `φ(n) = 3120`, `d = 2753`). L'atac per diccionari de l'apartat 5 recupera el text sense la clau privada i a `auditoria_ia.py` cada error es marca com a `INCORRECTE`.
