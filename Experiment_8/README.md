# Experiment 8 — OpenPGP Email in Thunderbird (Yaseen)

## Aim

Demonstrate two-way email protection with OpenPGP in Thunderbird: encrypt messages for the recipient and use digital signatures that the recipient can verify.

## Participants and recorded keys

| Role | Email / display name | OpenPGP key ID |
|---|---|---|
| Yaseen | `2024a7r002@mietjammu.in` | `0xE1A46926C6F12BD0` |
| Correspondent | `2024a7r056@mietjammu.in` (Adaya Misra) | `0x7DCBCEDB5EA19ECA` |

## Exchange visualization

```text
Yaseen                                              Adaya Misra
(private key: E1A46926C6F12BD0)                    (private key: 7DCBCEDB5EA19ECA)
       |                                                     |
       | 1. Exchange public keys and confirm key identity    |
       |<--------------------------------------------------->|
       |                                                     |
       | 2. Sign with Yaseen's key; encrypt to Adaya         |
       |---------------------------------------------------->|
       |                    decrypt + verify                 |
       |                                                     |
       | 3. Sign with Adaya's key; encrypt to Yaseen         |
       |<----------------------------------------------------|
       |                    decrypt + verify                 |
```

## Procedure

1. In Thunderbird, create or select the OpenPGP key pair for the account and share its public key with the correspondent.
2. Import the correspondent's public key. Confirm its fingerprint through a trusted channel before relying on it; a key ID alone does not establish identity.
3. Compose an email to the correspondent and enable **Encrypt** and **Digitally Sign**. Send it.
4. The correspondent opens the email, decrypts it with their private key, and checks the signature against Yaseen's public key.
5. The correspondent sends a reply with encryption and signing enabled. Yaseen opens it and checks the decryption and signature status in Thunderbird's OpenPGP/message-security details.

## Observed results

| Direction | Encryption/decryption | Signature status | Key IDs recorded |
|---|---|---|---|
| Yaseen → Adaya Misra | Successful | Valid | Sender `0xE1A46926C6F12BD0`; correspondent `0x7DCBCEDB5EA19ECA` |
| Adaya Misra → Yaseen | Successful | Valid | Sender `0x7DCBCEDB5EA19ECA`; recipient `0xE1A46926C6F12BD0` |

The conversation's screenshot review reports successful encryption and decryption and valid signatures in both directions. No message text, timestamps, cipher, or full fingerprints are recorded here.

## Security interpretation

- **Confidentiality:** successful encryption and decryption show that the exchanged messages were protected for their intended recipients and could be opened by the corresponding private-key holders.
- **Integrity and origin authentication:** a valid signature means Thunderbird verified the signed content against the signer's public key and found no signature mismatch. The sender's real-world identity still depends on checking that public key's fingerprint with the intended person.
- **Limit:** key IDs identify keys but are not substitutes for fingerprint verification. The available observations do not specify a cipher, fingerprint value, or trust-check method.

## Evidence checklist

- [ ] Screenshot of Yaseen → correspondent message security showing encrypted status and valid signature.
- [ ] Screenshot of correspondent → Yaseen message security showing encrypted status and valid signature.
- [ ] Screenshot or record showing Yaseen's key ID `0xE1A46926C6F12BD0`.
- [ ] Screenshot or record showing correspondent key ID `0x7DCBCEDB5EA19ECA`.
- [ ] If required by the lab, evidence of fingerprint comparison; no fingerprint value is reproduced in the available observations.

## Conclusion

The observed two-way Thunderbird exchange completed successfully: both sides decrypted the received email and both signatures were reported valid. This demonstrates OpenPGP email encryption and signature checking for the recorded accounts and keys.
