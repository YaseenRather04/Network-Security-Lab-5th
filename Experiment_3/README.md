# Challenge-Response Authentication

FastAPI-based implementation of challenge-response authentication with replay attack detection and timestamp validation.

## Features

- Secure nonce generation
- HMAC-SHA256 authentication
- Timestamp-based freshness check
- Replay attack detection
- Interactive client menu

## Run

Install dependencies:

```bash
pip install fastapi uvicorn requests
# Challenge-Response Authentication

Start the server:
  uvicorn server:app --reload
In another terminal:
  python client.py
Tests
  The client menu provides:
  1. Normal Authentication
  2. Replay Attack
  3. Delayed Response
  4. Exit
```

