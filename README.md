# Pràctica 2: RSA — de les matemàtiques a una implementació real
**Grup:** Guillem Alcoverro, Nil Molinero

## Requisits

- Python 3.10 o superior.
- No calen dependències externes; tots els scripts fan servir únicament la biblioteca estàndard de Python (durant les fases 2–6 no s'ha utilitzat cap biblioteca criptogràfica, i la multipotència modular `pow(a, b, n)` només s'ha fet servir per a l'auditoria de l'apartat 9).
- OpenSSL 3.x per als apartats 7 (comparació amb una biblioteca real) i 8 (comunicació Alice–Bob).
- Terminal amb `bash` (o equivalent) per a les comandes d'OpenSSL.

---

## Estructura del projecte

```
.
├── README.md                        # Aquest fitxer
├── IA.md                            # Ús de la intel·ligència artificial
├── informe.pdf                      # Informe de la pràctica
├── claus/                           # Claus PEM de l'experiment Alice–Bob (apartat 8)
│   ├── privada_bob.pem              # La nostra clau privada (mai s'intercanvia)
│   ├── publica_bob.pem              # La nostra clau pública (lliurada a l'altra parella)
│   └── publica_alice.pem            # Clau pública de l'altra parella (rebuda)
├── criptogrames/                    # Resultats de l'intercanvi Alice–Bob
│   ├── missatge_alice.enc           # Missatge rebut d'Alice, xifrat amb la nostra clau pública
│   ├── missatge_recuperat_alice.txt # Missatge d'Alice desxifrat amb la nostra clau privada
│   ├── frase_original_bob.txt       # Missatge nostre per a Alice, en clar
│   └── text_xifrat_per_alice.enc    # El mateix missatge xifrat amb la clau pública d'Alice
└── codi/
    ├── euclides.py                  # MCD, Euclides estès i invers modular (apartat 2)
    ├── exponenciacio.py             # Exponenciació modular ràpida (apartat 2.4)
    ├── genera_claus.py              # Generació i validació de claus RSA (apartat 3)
    ├── rsa.py                       # Xifratge i desxifratge d'enters (apartat 3.2)
    ├── text_a_bytes.py              # Del text a bytes UTF-8 (apartat 4.1)
    ├── xifra_text.py                # Xifratge byte a byte (apartat 4.2)
    ├── repetitions.py               # Anàlisi de repeticions en el criptograma (apartat 4.3)
    ├── atac.py                      # Atac per diccionari dels 256 bytes (apartat 5)
    ├── blocs.py                     # Vàries bytes com un únic enter (apartat 6)
    └── auditoria_ia.py              # Auditoria del programa generat per IA (apartat 9)
```

Els scripts s'importen entre si (`genera_claus` importa `euclides`, `xifra_text` importa `rsa`, etc.), per això **s'han d'executar des del directori `codi/`**:

```bash
cd codi
python3 euclides.py
```

---

## Com executar els programes

### 1. `euclides.py` — Eines matemàtiques (apartat 2)

Implementa l'algorisme d'Euclides (`euclides`), l'algorisme estès (`euclides_extens`, que retorna els coeficients de Bézout) i l'invers modular (`invers_modular`, que retorna `None` quan no existeix).

```bash
python3 euclides.py
```

Comprovacions:

```python
euclides(1728, 842)        # 2
euclides_extens(1728, 842) # (2, 134, -275)
invers_modular(17, 3120)   # 2753
```

---

### 2. `exponenciacio.py` — Exponenciació modular ràpida (apartat 2.4)

Calcula `aᵉ mod n` escrivint `e` en binari i amb quadrats successius, sense calcular mai `aᵉ` i reduint mòdul `n` després de cada multiplicació (nombre de multiplicacions proporcional al nombre de bits de l'exponent).

```bash
python3 exponenciacio.py
```

Comprovació:

```python
exponenciacio_modular_rapida(65, 17, 3233)  # 2790
```

Els resultats es poden contrastar amb `pow(a, e, n)`.

---

### 3. `genera_claus.py` — Generació de claus RSA (apartats 3.1 i 3.3)

Calcula `n = pq`, `φ(n) = (p−1)(q−1)`, comprova que `mcd(e, φ(n)) = 1` i obté `d = e⁻¹ mod φ(n)`. Retorna `((n, e), (n, d))`.

```bash
python3 genera_claus.py
```

Comprovacions:

```python
genera_claus(61, 53, 17)      # n = 3233, φ(n) = 3120, d = 2753
genera_claus(1009, 1013, 65537)  # n = 1022117, e = 65537, d = 832193  (la nostra clau)
```

Rebuigs (retorna `None`):

| Cas                             | Exemple provat        |
| ------------------------------- | --------------------- |
| `p = q`                         | `genera_claus(1009, 1009, 65537)` |
| `p` o `q` no primer             | `genera_claus(1001, 1013, 65537)` |
| `e` no coprimer amb `φ(n)`      | `genera_claus(1009, 1013, 4)`     |

---

### 4. `rsa.py` — Xifratge i desxifratge d'enters (apartat 3.2)

`xifra(m, e, n)` i `desxifra(c, d, n)`, només amb la funció d'exponenciació modular pròpia. `xifra` rebutja valors fora de l'interval `0 ≤ m < n`.

```bash
python3 rsa.py
```

```python
xifra(65, 17, 3233)   # 2790
desxifra(2790, 2753, 3233)  # 65
xifra(3233, 17, 3233) # None  (cal m < n)
```

---

### 5. `text_a_bytes.py` — Del text als bytes (apartat 4.1)

Comprovació de la diferència entre el codi Unicode d'un caràcter (`ord`) i la seva representació en UTF-8.

```bash
python3 text_a_bytes.py
```

Sortida:

```
65                  # ord("A")
250                 # ord("ú")
[195, 186]          # "ú".encode("utf-8") → 2 bytes
[72, 111, 108, 97, 33]  # "Hola!".encode("utf-8")
```

---

### 6. `xifra_text.py` — RSA byte a byte (apartat 4.2)

Converteix el text a UTF-8, xifra cada byte independentment amb `xifra`, i el desxifra reconstruint els bytes i el text originals. Comprova que `n > 255` (un byte va de 0 a 255 i RSA exigeix `m < n`).

```bash
python3 xifra_text.py
```

```python
xifra_text("Hola!", 17, 200)                     # None  (n = 200 ≤ 255)
xifra_text("La criptografia és divertida!", e, n) # llista d'enters xifrats
desxifra_text(criptograma, d, n)                  # "La criptografia és divertida!"
```

---

### 7. `repetitions.py` — Anàlisi de les repeticions (apartat 4.3)

Xifra textos amb repeticions i mostra quins criptogrames es repeteixen: dos bytes iguals sempre produeixen el mateix criptograma, de manera que les repeticions del text en clar es veuen en clar.

```bash
python3 repetitions.py
```

Sortida (clau `p = 1009, q = 1013`):

```
AAAAAAAAAA
[341568, 341568, ... ]   →  {341568: 10}
MISSISSIPPI
[428438, 368745, 520249, 520249, ...]  →  {368745: 4, 520249: 4, 238996: 2}
```

---

### 8. `atac.py` — Atac per diccionari dels 256 bytes (apartat 5)

Construeix el diccionari `c → m` calculant `mᵉ mod n` per a `m = 0, …, 255` **només amb la clau pública** i recupera el text xifrat sense factoritzar `n` ni calcular `d`.

```bash
python3 atac.py
```

Sortida:

```
Text original: La criptografia és divertida!
Criptograma: [167785, 745232, 651066, ...]
Text recuperat: La criptografia és divertida!
Atac exitós? True
```

---

### 9. `blocs.py` — Blocs de bytes com un únic enter (apartat 6)

Converteix un bloc de bytes a un enter (base 256, big-endian) i viceversa, i calcula el màxim `k` tal que `256ᵏ < n`.

```bash
python3 blocs.py
```

Sortida:

```
'Hola' com a enter: 1215261793
Recuperat: b'Hola'

n = 3233 (clau petita)      → k = 1 byte
n = 1022117 (la nostra clau) → k = 2 bytes
n ≈ 2^2048 (clau OpenSSL)   → k = 255 bytes = 2040 bits
```

---

### 10. `auditoria_ia.py` — Auditoria del programa generat per IA (apartat 9)

Reproduïx el codi proposat per la IA i construeix casos concrets que mostren els seus errors: `p = q`, `p` o `q` compostos, `e` no coprimer amb `φ(n)`, `ord(c)` en lloc de UTF-8, absència de la comprovació `m < n` i visibilitat de les repeticions.

```bash
python3 auditoria_ia.py
```

Sortida (resum):

```
9.1 Generacio de les claus
p = q = 13 -> n = 169  d = 29
  xifra 7 = 76  desxifra = 33 -> INCORRECTE
p = 51 (compost) -> n = 3111 ... -> INCORRECTE
q = 1024 (compost) -> n = 1033216 ... -> INCORRECTE
e = 13, phi = 3120 -> ((3233, 13), (3233, None)) -> INCORRECTE (d = None)

9.2 Xifratge del text
ord('A') = 65  utf-8 = [65]
ord('ú') = 250  utf-8 = [195, 186] -> INCORRECTE
ord('ç') = 231  utf-8 = [195, 167] -> INCORRECTE
ord('€') = 8364 > n = 3233, es redueix a 1898 -> INCORRECTE
AAAAAAAAAA -> [2790, 2790, ...] -> INCORRECTE
MISSISSIPPI -> [3123, 1486, 2680, ...] -> INCORRECTE

9.3 Conclusio: SI / NO / NO
```