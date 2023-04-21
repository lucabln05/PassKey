#pyotp

import pyotp

# generate the 2fa number for the key
def generate_key(key: str) -> str:
    totp = pyotp.TOTP(key)
    return totp.now()

