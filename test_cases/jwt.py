import jwt

token = input()

payload = jwt.decode(
    token,
    options={"verify_signature": False}
)