import hashlib
import secrets

secret = secrets.token_hex(32)
secret_hash = hashlib.sha256(secret.encode()).hexdigest()

print(f"secret: {secret}")
print(f"secret_hash: {secret_hash}")
