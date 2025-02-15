import jwt
import datetime

def generate_token(user_id: int, secret: str, algorithm: str, expires_delta: int) -> str:
    payload = {
        "user_id": user_id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_delta)
    }
    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token

def verify_token(token: str, secret: str, algorithms: list):
    try:
        payload = jwt.decode(token, secret, algorithms=algorithms)
        return payload
    except jwt.ExpiredSignatureError:
        print("Token Expired")
    except jwt.InvalidTokenError:
        print("Token Invalid")
    return None