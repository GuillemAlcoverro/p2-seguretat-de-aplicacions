#!/bin/bash

# 7.1 — Generació de claus RSA amb OpenSSL

# Generar clau privada de 2048 bits
openssl genpkey -algorithm RSA \
    -pkeyopt rsa_keygen_bits:2048 \
    -out claus/privada.pem

# Extreure la clau pública
openssl pkey -in claus/privada.pem \
    -pubout \
    -out claus/publica.pem

# Inspeccionar la clau privada
echo "=== CLAU PRIVADA ==="
openssl pkey -in claus/privada.pem -text -noout

# Inspeccionar la clau pública
echo "=== CLAU PÚBLICA ==="
openssl pkey -pubin \
    -in claus/publica.pem \
    -text -noout