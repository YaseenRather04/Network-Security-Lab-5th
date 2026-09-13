# Experiment 2: SHA-256 Data Integrity

## Aim

To generate SHA-256 hash values for text and files and simulate file tampering to observe changes in the hash.

## Methodology

1. Accept text or a file as input.
2. Generate its SHA-256 hash using Python's `hashlib`.
3. Read file contents using UTF-8 encoding.
4. Read file bytes in binary mode for file hashing.
5. Simulate tampering by modifying an existing word or appending text.
6. Generate the new hash after modification.
7. Compare the original and modified hash values to identify changes.

## Implementation

The program contains the following functions:

- `hash_text()` - Generates SHA-256 hash for user-provided text.
- `read_file()` - Reads and returns the contents of a text file.
- `hash_file()` - Generates SHA-256 hash for a file.
- `tampering_simulation()` - Modifies the file and generates its new hash.

## Features

- Hash typed text
- Hash files
- Display file contents
- Replace an existing word
- Append text to a file
- Generate a new hash after modification
- Handles missing files using exception handling
- Menu-driven interface

## Results

| Operation | Result |
|-----------|--------|
| Text hashing | SHA-256 hash generated |
| File hashing | SHA-256 hash generated |
| Word modification | File modified and new hash generated |
| Text append | File modified and new hash generated |

A modified file produces a different SHA-256 hash from its original content.

## Discussion

SHA-256 generates a fixed 256-bit digest represented by 64 hexadecimal characters. A change in the input changes the resulting digest, allowing modifications to be detected.

Hashing provides integrity checking but does not encrypt or hide the original data.

## Improvements

- Added hashing for both text and files.
- Added interactive tampering simulation.
- Added two tampering methods: word replacement and text appending.
- Added file content display before and after modification.
- Added file-not-found exception handling.
- Added a menu-driven interface for all operations.
