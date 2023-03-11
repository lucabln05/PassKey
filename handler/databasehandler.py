import os 
import sqlite3

# local imports
import handler.cryptohandler as ch
safe_path = "database/safe.db"

class check():
    def startup_check() -> bool:
        if not os.path("database/safe.db"):
            return False
        else:
            print("Database file found.")
            return True
    
    def check_password(password, salt) -> bool:
        con = sqlite3.connect(safe_path)
        db = con.cursor()
        db_content = db.execute("SELECT * FROM safe WHERE id = 1").fetchall()
        con.close()
        db_content = db_content[0][1:]
        db_content = ch.content_decrypt(db_content, password, salt)
       
        db_content[0] = db_content[0][2:-1]
        if db_content[0] == "decrypted":
            return True
        else:
            return False

def create_db() -> bool:
    db = open(safe_path, "wb")
    db.close()
    
    try: 
        con = sqlite3.connect(safe_path)
        db = con.cursor()
        db.execute("CREATE TABLE IF NOT EXISTS safe (id INTEGER, objectname TEXT, username TEXT, password TEXT, url TEXT, notes TEXT, PRIMARY KEY (id) )")
        #check for manager to check if file whas correctly decrypted
        password = input("Set password: ")
        database_content = "decrypted", "decrypted", "decrypted", "decrypted", "decrypted"
        objectname, username, password, url, notes = ch.first_time_encrypt(database_content, password)
        db.execute("INSERT INTO safe (objectname, username, password, url, notes) VALUES (?, ?, ?, ?, ?)", (objectname, username, password, url, notes))
        db.execute("INSERT INTO safe (objectname, username, password, url, notes) VALUES (?, ?, ?, ?, ?)", (objectname, username, password, url, notes))
        db.execute("")
        con.commit()
        con.close()
        return True

    except Exception as e:
        print(e)
        return False


def decrypt_object(password, salt, id) -> str:
    try:
        con = sqlite3.connect(safe_path)
        db = con.cursor()
        encrypt_db = db.execute("SELECT * FROM safe WHERE id = (?)", str(id)).fetchall()
        encrypt_db = encrypt_db[0][1:]
        database_content = ch.content_decrypt(encrypt_db, password, salt)
        con.commit()
        con.close()
        print(database_content)
        return database_content

    except Exception as e:
        return False

def decrypt_db(password, salt) -> str:
    try:
        con = sqlite3.connect(safe_path)
        db = con.cursor()
        encrypt_db = db.execute("SELECT * FROM safe").fetchall()

        decrypt_database_content = []
        for row in encrypt_db:
            row = list(row)
            row = row[1:]
            database_content = ch.content_decrypt(row, password, salt)
            decrypt_database_content.append(database_content)

        con.commit()
        con.close()
        return decrypt_database_content
    except Exception as e:
        return False
    
print(check.check_password("lucabellon", "9227158459080715"))