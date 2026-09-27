# Experiment 4 — X.509 Self-Signed Digital Certificate

**COM-511 Network Security Lab**

## Aim

Generate an RSA private key and a self-signed X.509 certificate using OpenSSL, inspect its fields, verify it with and without an explicit trust anchor, and confirm the certificate's public key matches the private key.

## Background

An X.509 certificate binds a public key to an identity (the **subject**) and is signed by an **issuer**. In a normal PKI, a separate trusted Certificate Authority (CA) signs the certificate, and a relying party trusts it because it trusts that CA. In a **self-signed** certificate, the subject and issuer are the same entity — there is no independent third party vouching for the identity. The signature still proves internal consistency (the certificate hasn't been tampered with and really does pair with this key), but it proves nothing about whether the identity should be trusted. That decision is made separately by whoever is relying on the certificate.

## Lab Steps

### 1. Setup
```bash
openssl version
mkdir x509_lab
cd x509_lab
```
Confirms OpenSSL is installed and creates a clean working folder.

### 2. Generate the RSA private key
```bash
openssl genpkey -algorithm RSA -out private.key -pkeyopt rsa_keygen_bits:2048
openssl pkey -in private.key -check -noout
chmod 600 private.key
```
Creates a 2048-bit RSA key pair, validates it (`Key is valid`), and restricts file permissions since `private.key` must never be shared.

### 3. Create the self-signed certificate
```bash
openssl req -new -x509 -sha256 \
 -key private.key -out certificate.crt -days 365 \
 -subj "/C=IN/ST=Jammu/L=Jammu/O=MIET/OU=CSE/CN=localhost" \
 -addext "subjectAltName=DNS:localhost,IP:127.0.0.1" \
 -addext "basicConstraints=critical,CA:FALSE" \
 -addext "keyUsage=critical,digitalSignature,keyEncipherment" \
 -addext "extendedKeyUsage=serverAuth"
```
Builds a certificate around the public key, valid for 365 days, and signs it with the same private key (self-signed). Extensions restrict what the certificate may be used for.

### 4. Inspect the certificate
```bash
openssl x509 -in certificate.crt -text -noout
openssl x509 -in certificate.crt -noout -subject -issuer -dates -serial
openssl x509 -in certificate.crt -noout -ext subjectAltName,basicConstraints,keyUsage,extendedKeyUsage
openssl x509 -in certificate.crt -noout -fingerprint -sha256
```
Reveals subject, issuer, validity period, public key info, extensions, and signature. **Subject and Issuer are identical** — the signature of a self-signed certificate.

### 5. Verify — untrusted vs. explicitly trusted
```bash
openssl verify certificate.crt
# → error 18: self-signed certificate (fails by default)

openssl verify -CAfile certificate.crt certificate.crt
# → certificate.crt: OK (passes once explicitly trusted)
```
This is the core result of the lab: the certificate fails verification against the default trust store, but passes once the command is explicitly told to treat it as its own trust anchor. **This does not make the certificate publicly trusted** — it only reflects the local trust decision made for that one command.

### 6. Confirm the private key and certificate match
```bash
openssl pkey -in private.key -pubout -outform DER 2>/dev/null | openssl dgst -sha256
openssl x509 -in certificate.crt -pubkey -noout | openssl pkey -pubin -outform DER 2>/dev/null | openssl dgst -sha256
```
Both commands derive a public key by a different path and hash it. Identical SHA-256 digests prove the certificate really does carry the public key paired with `private.key`.

### Optional: PEM ↔ DER encoding
```bash
openssl x509 -in certificate.crt -outform DER -out certificate.der
openssl x509 -in certificate.der -inform DER -noout -subject -issuer
```
Converts between the text-based PEM encoding and the binary DER encoding of the same certificate.

## Files Produced

| File | Type | Purpose | Handling |
|---|---|---|---|
| `private.key` | Private | Signs/decrypts | Never share |
| `certificate.crt` | Public | Identity + public key + signature | Safe to distribute |
| `certificate.der` | Public | Binary encoding of the same certificate | Safe to distribute |

