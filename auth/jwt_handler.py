import time
from typing import Dict
from config.config import settings
from jwt import encode, decode


def token_response(token: str):
    return {"access_token": token, "type": "Bearer"}


secret_key = settings.secret_key

algorithm = settings.algorithm


def sign_jwt(email: str) -> Dict[str, str]:
    # Set the expiry time.
    payload = {"email": email, "expires": time.time() + 2400}
    return token_response(encode(payload, secret_key, algorithm=algorithm))


def decode_jwt(token: str) -> dict:
    decoded_token = decode(token.encode(), secret_key, algorithms=[algorithm])
    return decoded_token if decoded_token["expires"] >= time.time() else {}