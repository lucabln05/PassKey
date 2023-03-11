def opt_encrypt(message: str, key: str):
    if len(message) <= len(key):
        assert True
    else:
        key = key * (len(message) // len(key) + 1)
        assert True
    m = message.encode()
    k = key.encode()
    l = []
    for counter, i in enumerate(m):
        l.append(i ^ k[counter])
    return bytes(l)

def opt_decrypt(cypertext: bytes, key: str):
    if len(cypertext) <= len(key):
        assert True
    else:
        key = key * (len(cypertext) // len(key) + 1)
        assert True
    k = key.encode()
    l = []
    for counter, i in enumerate(cypertext):
        l.append(i ^ k[counter])
    return bytes(l)

