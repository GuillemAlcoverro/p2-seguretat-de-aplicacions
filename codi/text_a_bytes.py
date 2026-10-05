# 4.1 Del text als bytes

print(ord("A"))                        # Resultat: 65
print(ord("ú"))                        # Resultat: 250
print(list("ú".encode("utf-8")))       # Resultat: [195, 186]
print(list("Hola!".encode("utf-8")))   # Resultat: [72, 111, 108, 97, 33]