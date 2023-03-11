import os 
import sqlite3

# local imports
import handler.cryptohandler as ch


safe_path = "safe/safe.db"


class check():
    def startup_check() -> bool:
        if not os.path("database/safe.db"):
            return False
        else:
            print("Database file found.")
            return True
    
    def check_password(password, salt) -> bool:

        try:
            con = sqlite3.connect(safe_path)
            db = con.cursor()
            db_content = db.execute("SELECT * FROM safe WHERE id = 1").fetchall()
            con.close()
            db_content = db_content[0][1:]
            db_content = ch.content_decrypt(db_content, password, salt)
        
            db_content[0] = db_content[0][2:-1]
            if db_content[0] == "decrypteddecrypteddecrypteddecrypted":
                return True
            return False
            
        
        except Exception as e:
            return False

def create_db(password) -> bool:
    if len(password) > 8:
        if os.path.exists(safe_path):
            return False 
        else:
            db = open(safe_path, "wb")
            db.close()
        
        try: 
            con = sqlite3.connect(safe_path)
            db = con.cursor()
            db.execute("CREATE TABLE IF NOT EXISTS safe (id INTEGER, objectname TEXT, username TEXT, password TEXT, url TEXT, notes TEXT, PRIMARY KEY (id) )")
            #check for manager to check if file whas correctly decrypted
            database_content = "decrypteddecrypteddecrypteddecrypted", "decrypteddecrypteddecrypteddecrypted", "decrypteddecrypteddecrypteddecrypted", "decrypteddecrypteddecrypteddecrypted", "decrypteddecrypteddecrypteddecrypted"
            content = ch.first_time_encrypt(database_content, password)
            db.execute("INSERT INTO safe (objectname, username, password, url, notes) VALUES (?, ?, ?, ?, ?)", (content[0][0], content[0][1], content[0][2], content[0][3], content[0][4]))
            db.execute("")
            con.commit()
            con.close()
            # return password and salt
            return content[1], content[2]

        except Exception as e:
            print(e)
            return False
    else:
        return False

def encrypt_object(content, password, salt):
    try:
        con = sqlite3.connect(safe_path)
        db = con.cursor()
        encrypt_content = ch.content_encrypt(content, password, salt)
        db.execute("INSERT INTO safe (objectname, username, password, url, notes) VALUES (?, ?, ?, ?, ?)", (encrypt_content[0], encrypt_content[1], encrypt_content[2], encrypt_content[3], encrypt_content[4]))
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
            for i in range(len(database_content)):
                database_content[i] = database_content[i][2:-1]
            decrypt_database_content.append(database_content)
        # remove first row because it is the manager
        decrypt_database_content.pop(0)

        con.commit()
        con.close()
        return decrypt_database_content
    except Exception as e:
        return False
    
def delete_object(object, username, password, salt) -> bool:
    try:
        con = sqlite3.connect(safe_path)
        db = con.cursor()
        #encrypt object and username
        content = object, username
        content = ch.content_encrypt(content, password, salt)
    
        db.execute("DELETE FROM safe WHERE objectname = (?) AND username = (?)", (content[0], content[1]))
        con.commit()
        con.close()
        return True
    except Exception as e:
        return False

