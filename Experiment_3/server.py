from fastapi import FastAPI
import secrets
import hmac
import hashlib
from time import time

app = FastAPI()

SHARED_KEY = b"network_security_lab"
MAX_AGE_SECONDS = 5

stored_nonce = set()


@app.get("/")
def home():
    return "This is The Challenge Simulation"


@app.get("/challenge", status_code=201)
def challenge():
    
    nonce = secrets.token_hex(16)

    stored_nonce.add(nonce)

    return {"nonce": nonce}


@app.post("/verify")
def verify(nonce: str, response: str, timestamp: int):

    if nonce not in stored_nonce:
        return {
            "authenticated" : False,
            "message" : "Replay Detected : Nonce already used"
        }


    current_time = int(time())

    if abs(current_time - timestamp) > 5:
        stored_nonce.remove(nonce)
        return {
            "authenticated" : False,
            "message" : "Time Expired!"
        }

    message = f"{nonce}:{timestamp}".encode()

    expected = hmac.new(SHARED_KEY, message, sha256).hexdigest()


    if hmac.compare_digest(response, expected):
        stored_nonce.remove(nonce)
        return {
            "authenticated" : True,
            "message" : "Authentication successful"
        }
    else:
        return {
            "authenticated" : False,
            "message" : "Authentication failed"
        }
