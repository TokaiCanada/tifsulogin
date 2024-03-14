from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
# Load the encryption key securely
key = b'CfVbu8IOqCc6L385tVcoZZJEc_FAcn55u9vhbi59hwQ='  # Replace with your encryption key

# Decrypt the email password
def decrypt_password(encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = None
    try:
        decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    except Exception as e:
        print("Error decrypting password:", e)
    return decrypted_password

# Decrypt the encrypted app-specific password
encrypted_app_password = os.getenv('ENCRYPTED_APP_PASSWORD')
if encrypted_app_password:
    app_password = decrypt_password(encrypted_app_password)
    if app_password:
        print("Decrypted App Password:", app_password)
    else:
        print("Failed to decrypt app password.")
else:
    print("ENCRYPTED_APP_PASSWORD environment variable not found.")
