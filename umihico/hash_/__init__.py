import hashlib as _hashlib


def hash_text(text):
    sha256 = _hashlib.sha256()
    sha256.update(text.encode())
    hashed_text = sha256.hexdigest()
    return hashed_text


if __name__ == '__main__':
    print(hash_text('text'))
