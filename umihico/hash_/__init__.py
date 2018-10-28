import hashlib as _hashlib


def hash_text(text):
    sha256 = _hashlib.sha256()
    sha256.update(text)
    hashed_text = sha256.hexdigest()
    return hashed_text
