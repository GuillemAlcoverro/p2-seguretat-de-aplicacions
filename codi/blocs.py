# 6 Blocs de bytes

from genera_claus import genera_claus


def bytes_a_enter(bloc):
    """Converteix un bloc de bytes a un enter (base 256, big-endian)."""
    return int.from_bytes(bloc, byteorder="big")


def enter_a_bytes(m, k):
    """Converteix un enter a un bloc de k bytes (big-endian)."""
    return m.to_bytes(k, byteorder="big")


def max_bytes_per_bloc(n):
    """Calcula el maxim k tal que 256^k < n."""
    k = 0
    while 256 ** (k + 1) < n:
        k += 1
    return k


if __name__ == "__main__":
    # 6.1 Experiment: "Hola" com a enter
    bloc = b"Hola"
    m = bytes_a_enter(bloc)
    print("'Hola' com a enter:", m)
    print("Recuperat:", enter_a_bytes(m, 4))

    # 6.2 Quants bytes caben?

    # Clau petita de l'exemple de classe (p=61, q=53 -> n=3233)
    n_petit = 3233
    k_petit = max_bytes_per_bloc(n_petit)
    print(f"\nn = {n_petit} (clau petita)")
    print(f"  Maxim bytes per bloc: k = {k_petit}")
    print(f"  256^{k_petit} = {256**k_petit} < {n_petit} < {256**(k_petit+1)} = 256^{k_petit+1}")

    # Clau propia (p=1009, q=1013 -> n=1022117)
    (n_propi, _, ), _ = genera_claus(1009, 1013, 65537)
    k_propi = max_bytes_per_bloc(n_propi)
    print(f"\nn = {n_propi} (clau propia)")
    print(f"  Maxim bytes per bloc: k = {k_propi}")
    print(f"  256^{k_propi} = {256**k_propi} < {n_propi} < {256**(k_propi+1)} = 256^{k_propi+1}")

    # Clau de 2048 bits (n te aproximadament 2048 bits)
    n_2048_bits = 2 ** 2048
    k_2048 = max_bytes_per_bloc(n_2048_bits)
    print(f"\nn ~ 2^2048 (clau de 2048 bits)")
    print(f"  Maxim bytes per bloc: k = {k_2048}")
    print(f"  Es a dir, {k_2048} bytes = {k_2048 * 8} bits")
