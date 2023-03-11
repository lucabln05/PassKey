import sys
from crypto.otp import *



import random

def first_time_encrypt(database_content, password) -> str:
    try:
        random_salt = str(random.randint(10**15, (10**16)-1))
        print("""

        SAFE-Salt = """ + random_salt + """
        SAFE-Password = """ + password + """

        """)
        print("Please safe your key and email. You will need it to decrypt your database. IF YOU CAN'T DECRYPT YOUR DATABASE YOU WILL LOSE ALL YOUR PASSWORDS.")
        key = str(random_salt) + str(password)

        encrypt_content = [str(opt_encrypt(column, key)) for column in database_content]
        return encrypt_content, password, random_salt
    except Exception as e:
        return False


def content_decrypt(database_content, password, salt) -> str:
    key = str(salt) + str(password)
    try:
        encrypt_content = [str(opt_decrypt(eval(column), key)) for column in database_content]
        return encrypt_content
    except Exception as e:
        print(e)
        return False


def content_encrypt(database_content, password, salt) -> bool:
    key = str(salt) + str(password)
    try:
        encrypt_content = [str(opt_encrypt(column, key)) for column in database_content]
        return encrypt_content
    except Exception as e:
        return False
    