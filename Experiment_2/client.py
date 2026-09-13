import requests
from hashlib import sha256
import hmac
import time

SERVER = "http://127.0.0.1:8000"
SHARED_KEY = b"network_security_lab"


def get_challenge():

    response = requests.get(f"{SERVER}/challenge")

    nonce = response.json()["nonce"]

    return nonce


def create_response(nonce, timestamp):

    message = f"{nonce}:{timestamp}".encode()

    client_response = hmac.new(
        SHARED_KEY,
        message,
        sha256
    ).hexdigest()

    return client_response


def verify_response(nonce, timestamp, client_response):

    result = requests.post(
        f"{SERVER}/verify",
        params={
            "nonce": nonce,
            "response": client_response,
            "timestamp": timestamp
        }
    )

    return result.json()


def normal_authentication():

    nonce = get_challenge()

    timestamp = int(time.time())

    client_response = create_response(
        nonce,
        timestamp
    )

    print("\nServer Nonce : ", nonce)
    print("Client Response : ", client_response)

    result = verify_response(
        nonce,
        timestamp,
        client_response
    )

    print("Authentication : ", result)


def replay_attack():

    nonce = get_challenge()

    timestamp = int(time.time())

    client_response = create_response(
        nonce,
        timestamp
    )

    print("\nServer Nonce : ", nonce)
    print("Client Response : ", client_response)

    # First legitimate request
    result = verify_response(
        nonce,
        timestamp,
        client_response
    )

    print("First Use : ", result)

    # Replay the exact same request
    result = verify_response(
        nonce,
        timestamp,
        client_response
    )

    print("Replay : ", result)


def delayed_response():

    nonce = get_challenge()

    timestamp = int(time.time())

    client_response = create_response(
        nonce,
        timestamp
    )

    print("\nServer Nonce : ", nonce)
    print("Client Response : ", client_response)

    print("Waiting 6 seconds...")

    time.sleep(6)

    result = verify_response(
        nonce,
        timestamp,
        client_response
    )

    print("Delayed Response : ", result)


def menu():

    while True:

        print("\n========================================")
        print(" Challenge-Response Authentication")
        print("========================================")
        print("1. Normal Authentication")
        print("2. Replay Attack")
        print("3. Delayed Response")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice : ")

        if choice == "1":

            normal_authentication()

        elif choice == "2":

            replay_attack()

        elif choice == "3":

            delayed_response()

        elif choice == "4":

            print("Exiting...")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()