# Experiment 5: Capture and Analyze a TLS Handshake

## Aim

To capture and analyze an HTTPS/TLS handshake using Wireshark and examine the ClientHello, ServerHello, certificate exchange, cryptographic parameter negotiation, and Finished messages.

---

## Theory

The TLS handshake establishes a secure communication session between a client and server. It negotiates protocol parameters, exchanges key information, authenticates the server using a digital certificate, and derives keys for protected communication.

In TLS 1.3, most handshake messages after the ServerHello are encrypted, so a TLS key log can be used with Wireshark for deeper analysis.

---

## Tools and Technologies

- Wireshark
- Web Browser
- HTTPS
- TLS 1.3
- SSLKEYLOGFILE
- PCAPNG packet capture

---

## Objective

1. Capture HTTPS traffic over TCP port 443.
2. Identify the TLS ClientHello message.
3. Identify the TLS ServerHello message.
4. Analyze parameters offered by the client.
5. Identify parameters selected by the server.
6. Inspect the server certificate.
7. Analyze protected TLS 1.3 handshake messages.
8. Understand the complete TLS handshake flow.

---

## Methodology

### 1. Start Wireshark

Open Wireshark and select the active network interface based on the observed network activity.

### 2. Apply Capture Filter

Use the following capture filter:

```text
tcp port 443
```

This limits the capture to TCP traffic on port 443.

### 3. Generate HTTPS Traffic

Open a fresh private browser window and access the authorized test website:

```text
https://www.wireshark.org/
```

Allow the HTTPS connection to establish.

### 4. Stop and Save the Capture

Stop the capture after the HTTPS session has been established and save it as:

```text
exp5_tls_handshake.pcapng
```

### 5. Filter TLS Traffic

Use the following Wireshark display filter:

```text
tls
```

### 6. Locate ClientHello

Use:

```text
tls.handshake.type == 1
```

Inspect the ClientHello packet for:

- Server Name / SNI
- Supported TLS versions
- Offered cipher suites
- Key-share information

### 7. Locate ServerHello

Use:

```text
tls.handshake.type == 2
```

Inspect the ServerHello packet for:

- Selected TLS version
- Selected cipher suite
- Selected key-share group

### 8. Configure TLS Key Logging

For deeper TLS 1.3 analysis, launch the test browser with `SSLKEYLOGFILE`.

#### Windows

```cmd
@echo off
set SSLKEYLOGFILE=%USERPROFILE%\Desktop\tls-keys.log
start firefox
```

#### Linux

```bash
export SSLKEYLOGFILE=$HOME/Desktop/tls-keys.log
firefox
```

#### macOS

```bash
export SSLKEYLOGFILE=$HOME/Desktop/tls-keys.log
open -a firefox
```

### 9. Configure Wireshark for Decryption

In Wireshark, open:

```text
Edit → Preferences → Protocols → TLS
```

Set the **Pre-Master-Secret log filename** to the absolute path of the generated key-log file.

Recapture a fresh HTTPS session after configuring the key log.

### 10. Analyze Protected Handshake Messages

Use:

```text
tls.handshake.type == 8 ||
tls.handshake.type == 11 ||
tls.handshake.type == 15 ||
tls.handshake.type == 20
```

The message types are:

| Type | Message |
|---|---|
| 8 | EncryptedExtensions |
| 11 | Certificate |
| 15 | CertificateVerify |
| 20 | Finished |

### 11. Inspect the Server Certificate

After successful decryption, locate:

```text
Transport Layer Security
→ Handshake Protocol: Certificate
→ Certificates
→ signedCertificate
```

Record:

- Subject / Common Name
- Issuer
- Subject Alternative Name
- Validity period
- Public-key type
- Certificate chain

---

## Wireshark Filters Used

### Capture Filter

```text
tcp port 443
```

### TLS Display Filter

```text
tls
```

### ClientHello

```text
tls.handshake.type == 1
```

### ServerHello

```text
tls.handshake.type == 2
```

### Certificate

```text
tls.handshake.type == 11
```

### Protected Handshake Messages

```text
tls.handshake.type == 8 ||
tls.handshake.type == 11 ||
tls.handshake.type == 15 ||
tls.handshake.type == 20
```

---

## Results

The HTTPS session was successfully captured and TLS 1.3 ClientHello and ServerHello messages were identified.

### Observed Certificate

The certificate details obtained for the test website were:

| Parameter | Observation |
|---|---|
| Common Name (CN) | `wireshark.org` |
| Issuer | `WE1` |
| Issuer Organization | `Google Trust Services` |
| Issued On | 22 August 2026 |
| Expires On | 20 November 2026 |
| Certificate Type | X.509 |

### TLS Parameters

The following values should be recorded directly from the actual ServerHello packet:

| Parameter | Observation |
|---|---|
| TLS Version | `TLS 1.3` |
| Selected Cipher Suite | `<record from Wireshark>` |
| Key-Share Group | `<record from Wireshark>` |

---

## Discussion

The TLS handshake negotiates the parameters required for secure communication. ClientHello provides the options supported by the client, while ServerHello selects the parameters used by the server.

In TLS 1.3, handshake messages after ServerHello are protected. The server certificate authenticates the server, while CertificateVerify and Finished messages complete the protected handshake.

---

## Improvements

- Use focused `tcp port 443` filtering.
- Record negotiated parameters directly from Wireshark.
- Use `SSLKEYLOGFILE` for TLS 1.3 decryption.
- Inspect certificate details and chain.
- Remove the TLS key-log file after analysis.

---

## TLS Handshake Flow

```text
                    TLS HANDSHAKE

Client                                      Server
  │                                           │
  │ ----------- ClientHello ----------------> │
  │                                           │
  │ <----------- ServerHello ---------------- │
  │                                           │
  │ <-------- EncryptedExtensions ----------- │
  │ <------------- Certificate ------------- │
  │ <---------- CertificateVerify ---------- │
  │ <--------------- Finished -------------- │
  │                                           │
  │ -------------- Finished ---------------> │
  │                                           │
  │ <------ Encrypted Application Data ----> │
  │                                           │
```

---

## Output

The experiment produced the following evidence:

1. ClientHello packet
2. ServerHello packet
3. Negotiated TLS parameters
4. Server certificate details
5. Decrypted TLS handshake messages, where key logging was enabled
6. Saved packet capture:

```text
exp5_tls_handshake.pcapng
```

### Important Screenshots

The following screenshots should be included in the lab record:

- ClientHello with expanded handshake fields
- ServerHello with selected parameters
- Certificate details
- Decrypted Certificate / CertificateVerify / Finished messages

---

## Safety and Notes

- Capture only authorized traffic.
- Do not use personal accounts during the experiment.
- Use a fresh private browser session.
- Treat the TLS key-log file as sensitive because it can contain session secrets.
- Delete or securely remove the test key-log file after completing the experiment.

---

## Conclusion

The TLS handshake was successfully captured and analyzed using Wireshark. The experiment demonstrated how ClientHello and ServerHello negotiate TLS parameters, how certificates provide server authentication, and how TLS 1.3 protects subsequent handshake and application data.
