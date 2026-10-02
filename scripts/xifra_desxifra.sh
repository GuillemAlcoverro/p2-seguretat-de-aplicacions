#!/bin/bash

# 7.2 — Xifratge i desxifratge amb OpenSSL

# Xifrar amb la clau pública (amb padding PKCS#1)
openssl pkeyutl -encrypt \
    -pubin \
    -inkey claus/publica.pem \
    -in missatges/missatge.txt \
    -out criptogrames/missatge.enc \
    -pkeyopt rsa_padding_mode:pkcs1

echo "Missatge xifrat guardat a criptogrames/missatge.enc"

# Desxifrar amb la clau privada
openssl pkeyutl -decrypt \
    -inkey claus/privada.pem \
    -in criptogrames/missatge.enc \
    -out missatges/recuperat.txt \
    -pkeyopt rsa_padding_mode:pkcs1

echo "Missatge recuperat:"
cat missatges/recuperat.txt
