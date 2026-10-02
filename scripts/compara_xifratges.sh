#!/bin/bash

# 7.3 — El mateix missatge dues vegades

# Xifrar el mateix missatge dues vegades
openssl pkeyutl -encrypt \
    -pubin \
    -inkey claus/publica.pem \
    -in missatges/missatge.txt \
    -out criptogrames/missatge1.enc \
    -pkeyopt rsa_padding_mode:pkcs1

openssl pkeyutl -encrypt \
    -pubin \
    -inkey claus/publica.pem \
    -in missatges/missatge.txt \
    -out criptogrames/missatge2.enc \
    -pkeyopt rsa_padding_mode:pkcs1

# Comparar els dos criptogrames
echo "=== SHA256 dels criptogrames ==="
sha256sum criptogrames/missatge1.enc criptogrames/missatge2.enc

echo ""
echo "=== Comparació directa ==="
if cmp -s criptogrames/missatge1.enc criptogrames/missatge2.enc; then
    echo "Els criptogrames són IGUALS"
else
    echo "Els criptogrames són DIFERENTS"
fi
